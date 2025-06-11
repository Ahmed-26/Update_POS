import io
import textwrap
from PIL import Image, ImageDraw, ImageFont


def receipt_text_to_png(receipt_text):
    MAX_LINE_LENGTH = 60  # max chars per line before wrap

    lines = []
    for line in receipt_text.splitlines():
        wrapped = textwrap.wrap(line, width=MAX_LINE_LENGTH) or [""]
        lines.extend(wrapped)

    font_path = None
    try:
        import sys

        if sys.platform == "win32":
            font_path = "C:\\Windows\\Fonts\\consola.ttf"
        elif sys.platform == "darwin":
            font_path = "/System/Library/Fonts/Menlo.ttc"
        else:
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
        font_size = 16
        font = ImageFont.truetype(font_path, font_size)
    except:
        font_size = 16
        font = ImageFont.load_default()

    max_width = 0
    line_height = None

    def text_size(text, font):
        if hasattr(font, "getsize"):
            return font.getsize(text)
        bbox = font.getbbox(text)
        return (bbox[2] - bbox[0], bbox[3] - bbox[1])

    for line in lines:
        w, h = text_size(line, font)
        max_width = max(max_width, w)
        if line_height is None or h > line_height:
            line_height = h
    if line_height is None:
        line_height = font_size + 2

    padding_x = 15
    padding_y = 15
    img_height = line_height * len(lines) + padding_y * 2
    img_width = max_width + padding_x * 2

    max_img_width = 480
    if img_width > max_img_width:
        img_width = max_img_width

    image = Image.new("RGB", (img_width, img_height), color="white")
    draw = ImageDraw.Draw(image)
    y = padding_y
    for line in lines:
        draw.text((padding_x, y), line, fill="black", font=font)
        y += line_height

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
