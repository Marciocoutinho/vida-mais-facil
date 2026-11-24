from __future__ import annotations

import re
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "entregas" / "modulo-a" / "Especificacao_Modulo_A_Vida_Mais_Facil.docx"

BLACK = "000000"
WHITE = "FFFFFF"
TEAL = "1F4E5F"
PALE_TEAL = "EAF4F2"
PALE_GRAY = "F5F6F7"
BORDER = "D9D9D9"
MUTED = RGBColor(74, 85, 92)


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def prevent_row_split(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement("w:cantSplit")
    tr_pr.append(cant_split)


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=110, start=110, bottom=110, end=110) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table) -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = f"w:{edge}"
        element = borders.find(qn(tag))
        if element is None:
            element = OxmlElement(tag)
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), "6")
        element.set(qn("w:space"), "0")
        element.set(qn("w:color"), BORDER)


def set_cell_width(cell, width_inches: float) -> None:
    width = Inches(width_inches)
    cell.width = width
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn("w:tcW"))
    if tc_w is None:
        tc_w = OxmlElement("w:tcW")
        tc_pr.append(tc_w)
    tc_w.set(qn("w:w"), str(int(width_inches * 1440)))
    tc_w.set(qn("w:type"), "dxa")


def set_font(run, name="Arial", size=None, bold=None, color=None) -> None:
    run.font.name = name
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:hAnsi"), name)
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if color is not None:
        run.font.color.rgb = color


def add_inline_markdown(paragraph, text: str) -> None:
    pattern = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`)")
    cursor = 0
    for match in pattern.finditer(text):
        if match.start() > cursor:
            set_font(paragraph.add_run(text[cursor : match.start()]))
        token = match.group(0)
        if token.startswith("**"):
            set_font(paragraph.add_run(token[2:-2]), bold=True)
        else:
            set_font(paragraph.add_run(token[1:-1]), name="Consolas", size=9)
        cursor = match.end()
    if cursor < len(text):
        set_font(paragraph.add_run(text[cursor:]))


def add_paragraph(doc: Document, text: str, style=None, italic=False):
    paragraph = doc.add_paragraph(style=style)
    add_inline_markdown(paragraph, text)
    for run in paragraph.runs:
        run.italic = italic
    paragraph.paragraph_format.space_after = Pt(6)
    paragraph.paragraph_format.line_spacing = 1.15
    return paragraph


def table_widths(headers: list[str]) -> list[float]:
    n = len(headers)
    normalized = [re.sub(r"[`*]", "", h).strip().lower() for h in headers]
    if n == 2:
        return [1.65, 4.85]
    if n == 3:
        return [1.0, 2.2, 3.3]
    if n == 4:
        if normalized[0] == "área":
            return [1.1, 2.05, 1.35, 2.0]
        return [0.65, 2.25, 1.25, 2.35]
    if n == 5:
        if "prioridade" in normalized:
            return [0.55, 0.85, 0.9, 1.85, 2.35]
        return [0.55, 1.3, 1.3, 1.0, 2.35]
    if n == 6:
        return [0.5, 0.95, 0.75, 1.45, 2.2, 0.65]
    return [6.5 / n] * n


def add_table_chunk(doc: Document, rows: list[list[str]]) -> None:
    if len(rows) < 2:
        return
    headers = rows[0]
    widths = table_widths(headers)
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)

    header = table.rows[0]
    set_repeat_table_header(header)
    prevent_row_split(header)
    for index, value in enumerate(headers):
        cell = header.cells[index]
        set_cell_width(cell, widths[index])
        set_cell_shading(cell, TEAL)
        set_cell_margins(cell)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        paragraph = cell.paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.space_after = Pt(0)
        paragraph.paragraph_format.line_spacing = 1.0
        run = paragraph.add_run(re.sub(r"[`*]", "", value).strip())
        set_font(run, size=8.5, bold=True, color=RGBColor(255, 255, 255))

    for row_index, values in enumerate(rows[1:], start=1):
        row = table.add_row()
        prevent_row_split(row)
        for index, value in enumerate(values):
            cell = row.cells[index]
            set_cell_width(cell, widths[index])
            set_cell_margins(cell)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if row_index % 2 == 0:
                set_cell_shading(cell, PALE_TEAL)
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.paragraph_format.line_spacing = 1.05
            if index == 0 and len(value) <= 14:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline_markdown(paragraph, value.strip())
            for run in paragraph.runs:
                if run.font.size is None or run.font.size.pt > 8.2:
                    run.font.size = Pt(8.2)

    after = doc.add_paragraph()
    after.paragraph_format.space_before = Pt(3)
    after.paragraph_format.space_after = Pt(9)


def add_table(doc: Document, rows: list[list[str]]) -> None:
    if len(rows) < 2:
        return
    # Cada tabela lógica permanece única. As linhas não são divididas, e o Word
    # faz a paginação natural sem criar cabeçalhos ou rótulos artificiais.
    add_table_chunk(doc, rows)


def add_list_item(doc: Document, text: str, marker: str = "-"):
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.left_indent = Inches(0.25)
    paragraph.paragraph_format.first_line_indent = Inches(0)
    paragraph.paragraph_format.space_before = Pt(2)
    paragraph.paragraph_format.space_after = Pt(4)
    paragraph.paragraph_format.line_spacing = Pt(14)
    paragraph.paragraph_format.keep_together = True
    paragraph.paragraph_format.widow_control = True
    marker_run = paragraph.add_run(f"{marker}  ")
    set_font(marker_run, size=10.5, bold=marker != "-")
    add_inline_markdown(paragraph, text)
    return paragraph


def configure_styles(doc: Document) -> None:
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    title = styles["Title"]
    title.font.name = "Arial"
    title._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
    title._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
    title.font.size = Pt(28)
    title.font.bold = True
    title.font.color.rgb = RGBColor(0, 0, 0)
    title.paragraph_format.space_after = Pt(18)
    title_p_pr = title._element.get_or_add_pPr()
    title_border = title_p_pr.find(qn("w:pBdr"))
    if title_border is not None:
        title_p_pr.remove(title_border)

    for style_name, size, before, after in (
        ("Heading 1", 18, 16, 8),
        ("Heading 2", 14, 12, 6),
        ("Heading 3", 11.5, 10, 4),
        ("Heading 4", 10.5, 8, 3),
    ):
        style = styles[style_name]
        style.font.name = "Arial"
        style._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
        style._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)

def add_page_field(paragraph) -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    value = OxmlElement("w:t")
    value.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instruction, separate, value, end])
    set_font(run, size=8, color=MUTED)


def configure_page(doc: Document) -> None:
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.72)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)
    section.header_distance = Inches(0.3)
    section.footer_distance = Inches(0.3)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = footer.add_run("Vida+Fácil  |  Módulo A  |  Página ")
    set_font(run, size=8, color=MUTED)
    add_page_field(footer)


def load_font(size: int, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered_text(draw, box, text, font, fill="#000000"):
    x1, y1, x2, y2 = box
    lines = wrap_text(draw, text, font, x2 - x1 - 28)
    heights = [draw.textbbox((0, 0), line, font=font)[3] for line in lines]
    total = sum(heights) + max(0, len(lines) - 1) * 6
    y = y1 + (y2 - y1 - total) / 2
    for line, height in zip(lines, heights):
        bounds = draw.textbbox((0, 0), line, font=font)
        width = bounds[2] - bounds[0]
        draw.text((x1 + (x2 - x1 - width) / 2, y), line, font=font, fill=fill)
        y += height + 6


def rounded_box(draw, box, text, fill, outline, font, radius=22, width=4):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    draw_centered_text(draw, box, text, font)


def arrow(draw, start, end, fill="#4A555C", width=4, dashed=False):
    x1, y1 = start
    x2, y2 = end
    if dashed:
        segments = 14
        for index in range(segments):
            if index % 2 == 0:
                a = index / segments
                b = (index + 1) / segments
                draw.line((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a, x1 + (x2 - x1) * b, y1 + (y2 - y1) * b), fill=fill, width=width)
    else:
        draw.line((x1, y1, x2, y2), fill=fill, width=width)
    angle = 0.55
    length = 18
    import math

    theta = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - length * math.cos(theta - angle), y2 - length * math.sin(theta - angle))
    p2 = (x2 - length * math.cos(theta + angle), y2 - length * math.sin(theta + angle))
    draw.polygon([(x2, y2), p1, p2], fill=fill)


def create_use_case_diagram(path: Path) -> None:
    image = Image.new("RGB", (1800, 1180), "white")
    draw = ImageDraw.Draw(image)
    heading = load_font(38, bold=True)
    actor_font = load_font(27, bold=True)
    item_font = load_font(24)
    note_font = load_font(20)
    draw.text((70, 38), "Atores e casos de uso do MVP", font=heading, fill="#000000")

    lanes = [
        ("Visitante", 130, ["Consultar conteúdo", "Criar conta", "Entrar", "Enviar contato"], "#F5F6F7", "#9AA3A8"),
        ("Paciente", 390, ["Ver dashboard", "Buscar horário", "Agendar", "Gerenciar indicadores", "Ver histórico"], "#E4F2FF", "#3DADFF"),
        ("Cuidador", 680, ["Consultar conteúdo", "Contato provisório"], "#FFF4D6", "#D4A62A"),
        ("Profissional", 920, ["Entrar", "Consultar agenda", "Manter disponibilidade"], "#EFE7FF", "#874FFF"),
    ]
    for actor, y, items, lane_fill, lane_outline in lanes:
        draw.rounded_rectangle((40, y - 35, 1760, y + 170), radius=24, fill=lane_fill, outline=lane_outline, width=3)
        actor_box = (75, y + 20, 355, y + 115)
        rounded_box(draw, actor_box, actor, "#FFFFFF", lane_outline, actor_font)
        count = len(items)
        available = 1320
        gap = 18
        width = (available - gap * (count - 1)) / count
        x = 405
        for item in items:
            item_box = (int(x), y + 18, int(x + width), y + 118)
            pending = "validar" in item.lower() or "provisório" in item.lower()
            rounded_box(draw, item_box, item, "#FFF3CE" if pending else "#FFFFFF", "#C49200" if pending else lane_outline, item_font)
            arrow(draw, (355, y + 68), (int(x), y + 68), dashed=pending)
            x += width + gap

    draw.line((70, 1135, 145, 1135), fill="#4A555C", width=4)
    draw.text((165, 1120), "Fluxo confirmado", font=note_font, fill="#4A555C")
    for x in range(500, 575, 16):
        draw.line((x, 1135, min(x + 8, 575), 1135), fill="#4A555C", width=4)
    draw.text((595, 1120), "Fluxo provisório ou a validar", font=note_font, fill="#4A555C")
    image.save(path, dpi=(220, 220))


def create_navigation_diagram(path: Path) -> None:
    image = Image.new("RGB", (1800, 1250), "white")
    draw = ImageDraw.Draw(image)
    heading = load_font(38, bold=True)
    font = load_font(23)
    small = load_font(20)
    draw.text((70, 35), "Mapa de navegação proposto", font=heading, fill="#000000")

    boxes = {
        "home": (710, 105, 1090, 190, "Início", "#FFFFFF", "#1F4E5F"),
        "content": (90, 300, 340, 385, "Conteúdos", "#F5F6F7", "#9AA3A8"),
        "register": (385, 300, 635, 385, "Cadastro", "#F5F6F7", "#9AA3A8"),
        "login": (680, 300, 930, 385, "Entrar", "#F5F6F7", "#9AA3A8"),
        "contact": (975, 300, 1225, 385, "Contato", "#F5F6F7", "#9AA3A8"),
        "article": (1270, 300, 1520, 385, "Artigo", "#F5F6F7", "#9AA3A8"),
        "patient": (355, 535, 755, 630, "Dashboard do paciente", "#E4F2FF", "#3DADFF"),
        "professional": (1045, 535, 1445, 630, "Painel profissional", "#EFE7FF", "#874FFF"),
        "appointments": (100, 790, 370, 875, "Atendimentos", "#E4F2FF", "#3DADFF"),
        "newAppointment": (405, 790, 675, 875, "Novo atendimento", "#E4F2FF", "#3DADFF"),
        "indicators": (710, 790, 980, 875, "Indicadores", "#E4F2FF", "#3DADFF"),
        "agenda": (1085, 790, 1355, 875, "Agenda", "#EFE7FF", "#874FFF"),
        "availability": (1390, 790, 1660, 875, "Disponibilidade", "#EFE7FF", "#874FFF"),
        "newIndicator": (485, 1030, 755, 1115, "Novo registro", "#E4F2FF", "#3DADFF"),
        "history": (800, 1030, 1070, 1115, "Histórico", "#E4F2FF", "#3DADFF"),
    }
    centers = {}
    for key, (x1, y1, x2, y2, label, fill, outline) in boxes.items():
        centers[key] = ((x1 + x2) / 2, (y1 + y2) / 2)
        rounded_box(draw, (x1, y1, x2, y2), label, fill, outline, font)

    def connect(source, target, dashed=False):
        sx, sy = centers[source]
        tx, ty = centers[target]
        source_box = boxes[source]
        target_box = boxes[target]
        start = (sx, source_box[3]) if ty > sy else (source_box[2], sy)
        end = (tx, target_box[1]) if ty > sy else (target_box[0], ty)
        arrow(draw, start, end, dashed=dashed)

    for target in ("content", "register", "login", "contact", "article"):
        connect("home", target)
    connect("login", "patient")
    connect("login", "professional")
    for target in ("appointments", "newAppointment", "indicators"):
        connect("patient", target)
    connect("professional", "agenda")
    connect("professional", "availability")
    connect("indicators", "newIndicator")
    connect("indicators", "history")

    draw.text((80, 1185), "A área profissional permite manter horários e consultar a própria agenda.", font=small, fill="#4A555C")
    image.save(path, dpi=(220, 220))


def add_picture_with_alt(doc: Document, image_path: Path, alt_text: str, width=6.5):
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    run.add_picture(str(image_path), width=Inches(width))
    drawing = run._r.find(qn("w:drawing"))
    if drawing is not None:
        doc_pr = drawing.find(".//" + qn("wp:docPr"))
        if doc_pr is not None:
            doc_pr.set("descr", alt_text)
            doc_pr.set("title", alt_text.split(".")[0])
    paragraph.paragraph_format.space_after = Pt(4)
    return paragraph


def parse_table(lines: list[str], start: int):
    raw = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        raw.append(lines[index].strip())
        index += 1
    rows = []
    for line_index, line in enumerate(raw):
        parts = [part.strip() for part in line.strip("|").split("|")]
        if line_index == 1 and all(re.fullmatch(r":?-{3,}:?", part) for part in parts):
            continue
        rows.append(parts)
    return rows, index


def add_markdown_file(doc: Document, path: Path, section_title: str, diagram_path: Path | None = None, diagram_alt: str | None = None):
    doc.add_page_break()
    doc.add_heading(section_title, level=1)
    lines = path.read_text(encoding="utf-8").splitlines()
    index = 1
    paragraph_buffer: list[str] = []
    skipping_section = False

    def flush_paragraph():
        nonlocal paragraph_buffer
        if paragraph_buffer:
            add_paragraph(doc, " ".join(part.strip() for part in paragraph_buffer))
            paragraph_buffer = []

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if stripped.startswith("## "):
            flush_paragraph()
            title = stripped[3:].strip()
            skipping_section = title == "Próxima etapa"
            if not skipping_section:
                doc.add_heading(title, level=2)
            index += 1
            continue
        if skipping_section:
            index += 1
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            doc.add_heading(stripped[4:].strip(), level=3)
            index += 1
            continue
        if stripped.startswith("#### "):
            flush_paragraph()
            doc.add_heading(stripped[5:].strip(), level=4)
            index += 1
            continue
        if stripped == "```mermaid":
            flush_paragraph()
            index += 1
            while index < len(lines) and lines[index].strip() != "```":
                index += 1
            index += 1
            if diagram_path and diagram_alt:
                add_picture_with_alt(doc, diagram_path, diagram_alt)
                caption = doc.add_paragraph("Figura. Representação visual acompanhada pelas tabelas e descrições desta seção.")
                caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
                caption.paragraph_format.space_after = Pt(8)
                for run in caption.runs:
                    set_font(run, size=8.5, color=MUTED)
                    run.italic = True
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            rows, index = parse_table(lines, index)
            add_table(doc, rows)
            continue
        if re.match(r"^-\s+", stripped):
            flush_paragraph()
            add_list_item(doc, re.sub(r"^-\s+", "", stripped))
            index += 1
            continue
        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            match = re.match(r"^(\d+)\.\s+(.*)$", stripped)
            add_list_item(doc, match.group(2), f"{match.group(1)}.")
            index += 1
            continue
        if stripped.startswith(">"):
            flush_paragraph()
            paragraph = add_paragraph(doc, stripped.lstrip("> "), italic=True)
            paragraph.paragraph_format.left_indent = Inches(0.25)
            index += 1
            continue
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        paragraph_buffer.append(stripped)
        index += 1
    flush_paragraph()


def add_cover(doc: Document) -> None:
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(70)
    title = doc.add_paragraph(style="Title")
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    title.add_run("Especificação do Módulo A")
    for run in title.runs:
        set_font(run, size=28, bold=True, color=RGBColor(0, 0, 0))
    title_p_pr = title._p.get_or_add_pPr()
    title_border = title_p_pr.find(qn("w:pBdr"))
    if title_border is not None:
        title_p_pr.remove(title_border)

    subtitle = doc.add_paragraph()
    subtitle.paragraph_format.space_after = Pt(12)
    run = subtitle.add_run("Vida+Fácil")
    set_font(run, size=22, bold=True, color=RGBColor(0, 0, 0))

    description = doc.add_paragraph()
    description.paragraph_format.space_after = Pt(34)
    run = description.add_run("Pesquisa e experiência para o cenário InovaVida Digital")
    set_font(run, size=13, color=MUTED)

    for label, value in (
        ("Autor", "Marcio Coutinho"),
        ("Duração oficial", "4 horas"),
        ("Data", "10 de novembro de 2026"),
        ("Estado", "Entrega consolidada para avaliação"),
    ):
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(5)
        label_run = paragraph.add_run(f"{label}: ")
        set_font(label_run, size=10.5, bold=True)
        value_run = paragraph.add_run(value)
        set_font(value_run, size=10.5)

    doc.add_page_break()


def add_opening(doc: Document) -> None:
    doc.add_heading("Visão geral da entrega", level=1)
    add_paragraph(
        doc,
        "Esta especificação consolida os resultados do Módulo A do Vida+Fácil. O MVP é uma plataforma web acessível e responsiva para pessoas idosas, cuidadores e profissionais de saúde, com conteúdo educativo, agendamento de atendimentos e registro manual de indicadores pelo paciente.",
    )
    add_paragraph(
        doc,
        "A pesquisa confirmou o núcleo do produto e também identificou decisões que não podem ser inventadas durante a implementação. Em especial, o acesso do cuidador, medicamentos, cancelamento e reagendamento, unidades dos indicadores e o uso de e-mail permanecem condicionados a regras explícitas.",
    )

    doc.add_heading("Conteúdo", level=2)
    for number, item in enumerate((
        "Pesquisa e evidências",
        "Matriz CSD",
        "Proto-personas",
        "Requisitos e regras de negócio",
        "Casos de uso",
        "Mapa de navegação",
        "Verificação e evidências de entrega",
    ), start=1):
        add_list_item(doc, item, f"{number}.")

    doc.add_heading("Decisões centrais", level=2)
    decisions = [
        ["Decisão", "Tratamento"],
        ["Duração", "Usar 4 horas como referência oficial; 2 horas permanece apenas como roteiro adaptado."],
        ["Personas", "Tratar os três perfis como proto-personas até validação com usuários."],
        ["Indicadores", "Limitar o MVP a glicemia, pressão arterial, frequência cardíaca e peso."],
        ["Cuidador", "Não conceder acesso delegado sem vínculo, consentimento e permissões definidos."],
        ["Conteúdo clínico", "Apresentar material educativo sem diagnóstico ou recomendação personalizada."],
    ]
    add_table(doc, decisions)


def add_delivery_checklist(doc: Document) -> None:
    doc.add_page_break()
    doc.add_heading("7 Verificação e evidências de entrega", level=1)
    add_paragraph(doc, "A verificação abaixo relaciona os seis itens do Módulo A na matriz de treinamento aos artefatos produzidos no repositório.")
    rows = [
        ["Item", "Resultado", "Evidência principal"],
        ["REQ-01 Fontes", "Atendido", "Inventário e evidências de pesquisa"],
        ["REQ-02 Personas", "Atendido com ressalva", "Três proto-personas; entrevistas não disponíveis"],
        ["REQ-03 CSD", "Atendido", "15 certezas, 10 suposições e 12 dúvidas"],
        ["REQ-04 Requisitos", "Atendido", "14 RF, 10 RNF e 9 regras de negócio"],
        ["REQ-05 Casos e navegação", "Atendido", "13 casos de uso e mapa com 18 páginas propostas"],
        ["REQ-06 README", "Atendido", "Contexto, estado, tecnologias e links atualizados"],
    ]
    add_table(doc, rows)

    doc.add_heading("Verificações realizadas", level=2)
    for item in (
        "rastreabilidade entre evidências, CSD, personas, requisitos, casos de uso e páginas;",
        "unicidade e sequência dos identificadores de requisitos e casos de uso;",
        "integridade UTF-8, títulos, tabelas e links dos arquivos Markdown;",
        "equivalentes textuais para os diagramas;",
        "critérios de acessibilidade para teclado, foco, semântica, contraste, zoom e mensagens;",
        "auditoria estrutural de acessibilidade e inspeção visual deste documento Word.",
    ):
        add_list_item(doc, item)

    doc.add_heading("Síntese do módulo", level=2)
    add_paragraph(doc, "Aprendizado: separar fato, hipótese e dúvida evita que lacunas do briefing se transformem em funcionalidades ou permissões inseguras.")
    add_paragraph(doc, "Entrega: pesquisa consolidada, matriz CSD, três proto-personas, requisitos priorizados, regras de negócio, casos de uso e mapa de navegação.")
    add_paragraph(doc, "Pendências: validar o papel do cuidador, cancelamento e reagendamento, campos pessoais, unidades dos indicadores, observações ou sintomas e o canal de e-mail.")
    add_paragraph(doc, "Próximo módulo: Módulo B, com wireframes, protótipo navegável e design system no Figma, somente após a revisão desta especificação.")

    doc.add_heading("Referências do pacote", level=2)
    for item in (
        "PT- Tecnologias Web.docx",
        "Briefing INFORMAÇÕES.docx",
        "Rascunho Briefing.docx",
        "Textos competição.docx",
        "Timetable_Aplições Web e Mobile_2025_VF.docx",
        "Matriz_Requisitos_e_Evidencias_Vida_Mais_Facil.xlsx",
        "Dados_Iniciais_Vida+Facil - Sugestão.xlsx",
        "Conteúdos educativos e textos institucionais da pasta TEXTOS",
    ):
        add_list_item(doc, item)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = Document()
    configure_styles(doc)
    configure_page(doc)
    doc.core_properties.title = "Especificação do Módulo A Vida+Fácil"
    doc.core_properties.subject = "Pesquisa e experiência"
    doc.core_properties.author = "Marcio Coutinho"
    doc.core_properties.keywords = "Vida+Fácil, Módulo A, pesquisa, requisitos, acessibilidade"
    doc.core_properties.comments = "Documento consolidado do projeto de referência Vida+Fácil"

    with tempfile.TemporaryDirectory(prefix="vida_mais_facil_modulo_a_") as temporary:
        temp = Path(temporary)
        use_case_diagram = temp / "casos-de-uso.png"
        navigation_diagram = temp / "mapa-navegacao.png"
        create_use_case_diagram(use_case_diagram)
        create_navigation_diagram(navigation_diagram)

        add_cover(doc)
        add_opening(doc)
        add_markdown_file(doc, ROOT / "docs" / "02-evidencias-pesquisa.md", "1 Pesquisa e evidências")
        add_markdown_file(doc, ROOT / "docs" / "03-matriz-csd.md", "2 Matriz CSD")
        add_markdown_file(doc, ROOT / "docs" / "04-personas.md", "3 Proto-personas")
        add_markdown_file(doc, ROOT / "docs" / "05-requisitos.md", "4 Requisitos e regras de negócio")
        add_markdown_file(
            doc,
            ROOT / "docs" / "06-casos-de-uso.md",
            "5 Casos de uso",
            use_case_diagram,
            "Diagrama dos atores e casos de uso. Visitante acessa conteúdo, cadastro, login e contato. Paciente acessa dashboard, busca, agendamento, indicadores e histórico. Cuidador permanece restrito ao conteúdo público e contato provisório. Profissional acessa login, mantém disponibilidade e consulta a própria agenda.",
        )
        add_markdown_file(
            doc,
            ROOT / "docs" / "07-mapa-navegacao.md",
            "6 Mapa de navegação",
            navigation_diagram,
            "Mapa de navegação hierárquico. A página inicial leva a conteúdo, cadastro, login e contato. O login direciona ao dashboard do paciente ou painel profissional. A área do paciente inclui atendimentos, novo atendimento, indicadores, novo registro e histórico. A área profissional inclui agenda e disponibilidade.",
        )
        add_delivery_checklist(doc)
        doc.save(OUTPUT)

    print(OUTPUT)


if __name__ == "__main__":
    main()
