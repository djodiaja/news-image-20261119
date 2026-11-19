"""Draw the world-news front page for Thursday 19 November 2026 to assets/entry.png.

Build-time only (Pillow + Windows system fonts). main.py copies the PNG, so the entry
runs with no network. Facts and sources: research.md.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 242, 233)
INK = (22, 22, 26)
GREY = (90, 90, 98)
RULE = (198, 190, 176)
RED = (186, 22, 38)
NAVY = (26, 62, 140)
TEAL = (16, 112, 120)
OCHRE = (176, 120, 20)
PLUM = (110, 40, 110)

FONT_DIR = Path("C:/Windows/Fonts")
OUT = Path(__file__).parent / "assets" / "entry.png"


def f(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def serif_b(s):
    return f("georgiab.ttf", s)


def serif(s):
    return f("georgia.ttf", s)


def sans_b(s):
    return f("arialbd.ttf", s)


def sans(s):
    return f("arial.ttf", s)


def lines_for(d, text, font, width):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            out.append(cur)
            cur = w
    out.append(cur)
    return out


def para(d, x, y, text, font, width, fill=INK, lead=4):
    for ln in lines_for(d, text, font, width):
        d.text((x, y), ln, font=font, fill=fill)
        y += font.size + lead
    return y


def tag(d, x, y, label, colour):
    font = sans_b(15)
    w = d.textlength(label, font=font)
    d.rectangle((x, y, x + w + 12, y + 22), fill=colour)
    d.text((x + 6, y + 3), label, font=font, fill=PAPER)
    return y + 30


def arrowhead(d, a, b, colour, width=5, head=13):
    d.line((a, b), fill=colour, width=width)
    t = math.atan2(b[1] - a[1], b[0] - a[0])
    p1 = (b[0] - head * math.cos(t - 0.45), b[1] - head * math.sin(t - 0.45))
    p2 = (b[0] - head * math.cos(t + 0.45), b[1] - head * math.sin(t + 0.45))
    d.polygon((b, p1, p2), fill=colour)


# ---------------------------------------------------------------- masthead + lead
def masthead(d):
    d.text((32, 22), "THE WORLD IN ONE PAGE", font=sans_b(18), fill=RED)
    d.text((32, 44), "Thursday 19 November 2026", font=serif_b(50), fill=INK)
    d.line((32, 112, W - 32, 112), fill=INK, width=3)
    d.line((32, 117, W - 32, 117), fill=INK, width=1)


def lead(d):
    top = 134
    # Three leaders at one table: a triangle of named nodes.
    nodes = {"XI": (190, top + 40, RED), "TRUMP": (80, top + 230, NAVY), "PUTIN": (300, top + 230, PLUM)}
    pts = [(x, y) for x, y, _ in nodes.values()]
    d.polygon(pts, outline=GREY, width=3)
    d.ellipse((150, top + 128, 230, top + 208), fill=(232, 224, 208), outline=GREY, width=2)
    d.text((166, top + 157), "3-way", font=sans_b(17), fill=INK)
    for name, (x, y, c) in nodes.items():
        d.ellipse((x - 36, y - 36, x + 36, y + 36), fill=c)
        fn = sans_b(18 if len(name) > 2 else 24)
        d.text((x - d.textlength(name, font=fn) / 2, y - fn.size / 2 - 2), name, font=fn, fill=PAPER)
    d.text((58, top + 290), "SHENZHEN, CHINA", font=sans_b(18), fill=GREY)

    x, width = 370, W - 32 - 370
    y = tag(d, x, top + 4, "APEC · FIRST-EVER SUMMIT", RED)
    y = para(d, x, y, "Trump, Xi and Putin hold first three-way summit", serif_b(44), width, lead=6)
    y += 10
    para(
        d, x, y,
        "90-minute talks on nuclear arms, Ukraine and Iran. Trump: the three are "
        "\u201cuniquely positioned\u201d to cut nuclear arsenals. Xi warns US on Taiwan. "
        "No joint statement.",
        serif(22), width, fill=GREY,
    )
    d.line((32, 476, W - 32, 476), fill=RULE, width=2)


# ---------------------------------------------------------------- middle row
def icj(d, x0, y0, x1):
    y = tag(d, x0, y0, "WORLD COURT · ASIA", TEAL)
    y = para(d, x0, y, "UN court rules Myanmar committed genocide against Rohingya", serif_b(28), x1 - x0)
    # scales of justice
    cx, cy = x0 + 60, y + 50
    d.line((cx, cy - 34, cx, cy + 34), fill=INK, width=4)
    d.line((cx - 46, cy - 24, cx + 46, cy - 24), fill=INK, width=4)
    for sx in (cx - 46, cx + 46):
        d.line((sx, cy - 24, sx - 16, cy + 6), fill=INK, width=2)
        d.line((sx, cy - 24, sx + 16, cy + 6), fill=INK, width=2)
        d.chord((sx - 18, cy - 6, sx + 18, cy + 16), 0, 180, fill=TEAL)
    d.rectangle((cx - 22, cy + 34, cx + 22, cy + 40), fill=INK)
    d.text((x0 + 150, y + 18), "9\u20136", font=serif_b(46), fill=TEAL)
    d.text((x0 + 152, y + 72), "ruling on 2016\u201317 killings; final", font=sans(18), fill=GREY)


def gta(d, x0, y0, x1):
    y = tag(d, x0, y0, "CULTURE · GAMING", OCHRE)
    y = para(d, x0, y, "Grand Theft Auto VI goes on sale worldwide", serif_b(28), x1 - x0)
    d.rounded_rectangle((x0, y + 14, x0 + 110, y + 92), radius=14, fill=INK)
    d.text((x0 + 22, y + 22), "VI", font=serif_b(52), fill=(255, 170, 60))
    d.text((x0 + 128, y + 18), "17m+", font=serif_b(46), fill=OCHRE)
    d.text((x0 + 130, y + 72), "copies pre-sold, reports say", font=sans(18), fill=GREY)


# ---------------------------------------------------------------- bottom row
def small(d, x0, y0, x1, label, colour, head, body, icon):
    y = tag(d, x0, y0, label, colour)
    icon(d, x0, y, x1)
    y += 60
    y = para(d, x0, y, head, serif_b(22), x1 - x0, lead=3)
    para(d, x0, y + 4, body, sans(17), x1 - x0, fill=GREY, lead=3)


def bridge_icon(d, x0, y, x1):
    mid = (x0 + x1) // 2
    d.line((x0, y + 30, mid - 14, y + 30), fill=INK, width=6)
    d.line((mid + 14, y + 36, x1 - 10, y + 30), fill=INK, width=6)
    for px in (x0 + 30, mid - 30, mid + 40, x1 - 40):
        d.line((px, y + 30, px, y + 50), fill=INK, width=4)
    d.line((mid - 9, y + 6, mid + 9, y + 24), fill=RED, width=4)
    d.line((mid - 9, y + 24, mid + 9, y + 6), fill=RED, width=4)


def arctic_icon(d, x0, y, x1):
    d.polygon(((x0 + 10, y + 46), (x0 + 40, y + 6), (x0 + 74, y + 18), (x0 + 96, y + 46)), fill=(205, 222, 232), outline=NAVY)
    d.text((x0 + 108, y + 8), "109\u20130", font=serif_b(30), fill=NAVY)


def missile_icon(d, x0, y, x1):
    arrowhead(d, (x1 - 20, y + 4), (x0 + 60, y + 40), RED, width=5)
    for i, r in enumerate((10, 16, 22)):
        d.arc((x0 + 40 - r, y + 40 - r, x0 + 40 + r, y + 40 + r), 0, 360, fill=OCHRE, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    lead(d)
    icj(d, 32, 492, 500)
    d.line((512, 492, 512, 716), fill=RULE, width=2)
    gta(d, 528, 492, W - 32)
    d.line((32, 730, W - 32, 730), fill=RULE, width=2)
    cols, gap = 3, 22
    cw = (W - 64 - gap * (cols - 1)) // cols
    stories = (
        ("UKRAINE WAR · EUROPE", PLUM, "Third strike in four days halts trains on Kerch Bridge",
         "Ukrainian drones hit the rail span linking Russia to Crimea.", bridge_icon),
        ("ARCTIC", NAVY, "Denmark ratifies US\u2013Greenland security deal",
         "Parliament votes 109\u20130; US can expand bases on the island.", arctic_icon),
        ("MIDDLE EAST", RED, "Missile debris damages Riyadh",
         "Saudi-led coalition blames Yemen\u2019s Houthis.", missile_icon),
    )
    for i, (label, colour, head, body, icon) in enumerate(stories):
        x0 = 32 + i * (cw + gap)
        small(d, x0, 746, x0 + cw, label, colour, head, body, icon)
        if i:
            d.line((x0 - gap // 2, 746, x0 - gap // 2, 990), fill=RULE, width=1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, optimize=True)
    print(OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
