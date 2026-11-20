"""World-news front page for Thursday 19 November 2026 -> assets/entry.png (v2, dense layout).

Build-time only (Pillow + Windows fonts); main.py copies the PNG. Drawn at 2x, then downsampled for
crisp type at 1024 px. Stories and sources live in stories.py and research.md.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from stories import ALSO, DATE_CHECK, FIGURES, LEADS, SECOND, SOURCES

S = 2                       # supersampling factor
W = H = 1024
PAPER = (247, 242, 231); INK = (24, 24, 30); GREY = (96, 96, 104); RULE = (196, 186, 168)
REGION = {'ASIA': (196, 70, 40), 'MIDDLE EAST': (150, 40, 50), 'EUROPE': (40, 80, 160), 'AFRICA': (40, 130, 70),
          'AMERICAS': (120, 60, 150), 'OCEANIA': (20, 130, 140), 'GLOBAL': (90, 90, 100)}
FD = Path('C:/Windows/Fonts')


def F(name, size):
    return ImageFont.truetype(str(FD / name), int(size * S))


serif_b = lambda s: F('georgiab.ttf', s)
serif = lambda s: F('georgia.ttf', s)
sans_b = lambda s: F('arialbd.ttf', s)
sans = lambda s: F('arial.ttf', s)
cond_b = lambda s: F('ARIALNB.TTF', s)


class Pen:
    """Coordinates in 1024-px units; everything is scaled by S."""

    def __init__(self, d):
        self.d = d

    def rect(self, x0, y0, x1, y1, **k):
        if 'width' in k: k['width'] = int(k['width'] * S)
        self.d.rectangle([x0 * S, y0 * S, x1 * S, y1 * S], **k)

    def rrect(self, x0, y0, x1, y1, r, **k):
        if 'width' in k: k['width'] = int(k['width'] * S)
        self.d.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S], radius=r * S, **k)

    def line(self, pts, fill, width=1):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=max(1, int(width * S)))

    def poly(self, pts, **k):
        if 'width' in k: k['width'] = int(k['width'] * S)
        self.d.polygon([(x * S, y * S) for x, y in pts], **k)

    def circle(self, x, y, r, **k):
        if 'width' in k: k['width'] = int(k['width'] * S)
        self.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], **k)

    def text(self, x, y, t, font, fill=INK, anchor='la'):
        self.d.text((x * S, y * S), t, font=font, fill=fill, anchor=anchor)

    def tw(self, t, font):
        return self.d.textlength(t, font=font) / S

    def wrap(self, x, y, t, font, width, fill=INK, lead=1.18, max_lines=9):
        words, line, lines = t.split(), '', []
        for w in words:
            trial = (line + ' ' + w).strip()
            if self.tw(trial, font) <= width: line = trial
            else: lines.append(line); line = w
        lines.append(line)
        for ln in lines[:max_lines]:
            self.text(x, y, ln, font, fill); y += font.size / S * lead
        return y


# ------------------------------------------------------------------ icons (all original, drawn in code)
def flag(p, x, y, w, h, kind):
    if kind == 'us':
        for i in range(7): p.rect(x, y + i * h / 7, x + w, y + (i + .5) * h / 7, fill=(178, 34, 52))
        p.rect(x, y, x + w * .42, y + h * .54, fill=(60, 59, 110))
    elif kind == 'cn':
        p.rect(x, y, x + w, y + h, fill=(222, 41, 16)); p.circle(x + w * .22, y + h * .3, h * .14, fill=(255, 222, 0))
    elif kind == 'ru':
        for i, c in enumerate([(255, 255, 255), (0, 57, 166), (213, 43, 30)]): p.rect(x, y + i * h / 3, x + w, y + (i + 1) * h / 3, fill=c)
    elif kind == 'dk':
        p.rect(x, y, x + w, y + h, fill=(198, 12, 48)); p.rect(x + w * .3, y, x + w * .42, y + h, fill='white'); p.rect(x, y + h * .42, x + w, y + h * .58, fill='white')
    p.rect(x, y, x + w, y + h, outline=INK, width=.6)


def icon(p, kind, x0, y0, x1, y1, accent):
    w, h = x1 - x0, y1 - y0; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    p.rect(x0, y0, x1, y1, fill=(234, 227, 212))
    if kind == 'summit':
        p.rect(x0 + w * .08, y0 + h * .62, x1 - w * .08, y0 + h * .74, fill=(120, 80, 50))
        for i, (f, name) in enumerate((('us', 'TRUMP'), ('cn', 'XI'), ('ru', 'PUTIN'))):
            fx = x0 + w * (.12 + i * .3)
            flag(p, fx, y0 + h * .12, w * .2, h * .18, f)
            p.circle(fx + w * .1, y0 + h * .45, h * .1, fill=(226, 190, 160)); p.rect(fx + w * .03, y0 + h * .53, fx + w * .17, y0 + h * .64, fill=(40, 50, 70))
            p.text(fx + w * .1, y0 + h * .86, name, cond_b(11), fill=INK, anchor='mm')
    elif kind == 'scales':
        p.line([(cx, y0 + h * .15), (cx, y0 + h * .85)], INK, 3); p.line([(cx - w * .3, y0 + h * .28), (cx + w * .3, y0 + h * .28)], INK, 3)
        for sx in (cx - w * .3, cx + w * .3):
            p.line([(sx, y0 + h * .28), (sx - w * .09, y0 + h * .55)], INK, 1); p.line([(sx, y0 + h * .28), (sx + w * .09, y0 + h * .55)], INK, 1)
            p.d.chord([(sx - w * .11) * S, (y0 + h * .45) * S, (sx + w * .11) * S, (y0 + h * .65) * S], 0, 180, fill=accent)
        p.text(cx, y0 + h * .93, 'ICJ  9 \u2013 6  MYANMAR', serif_b(12), fill=accent, anchor='mm')
    elif kind == 'stock':
        pts = [(x0 + w * (.08 + .84 * i / 7), y0 + h * (.8 - .55 * v)) for i, v in enumerate([.1, .15, .12, .3, .28, .5, .62, .7])]
        p.line(pts, (30, 130, 80), 3); p.text(x0 + w * .08, y0 + h * .1, 'ANT +17%', sans_b(13), fill=(30, 130, 80))
        dn = [(x0 + w * (.08 + .84 * i / 7), y0 + h * (.35 + .5 * v)) for i, v in enumerate([.0, .05, .02, .15, .22, .3, .42, .5])]
        p.line(dn, (190, 30, 40), 3); p.text(x1 - w * .06, y1 - h * .08, 'DOW −2.2%', sans_b(12), fill=(190, 30, 40), anchor='rs')
    elif kind == 'bridge':
        p.rect(x0, y0 + h * .7, x1, y1, fill=(90, 140, 190))
        p.line([(x0, y0 + h * .45), (cx - w * .08, y0 + h * .45)], INK, 3); p.line([(cx + w * .08, y0 + h * .52), (x1, y0 + h * .45)], INK, 3)
        for t in (.15, .35, .65, .85): p.line([(x0 + w * t, y0 + h * .45), (x0 + w * t, y0 + h * .7)], INK, 2)
        p.circle(cx, y0 + h * .35, h * .12, fill=(240, 140, 40))
    elif kind == 'arctic':
        p.poly([(x0 + w * .1, y1 - h * .2), (x0 + w * .35, y0 + h * .2), (x0 + w * .6, y0 + h * .35), (x1 - w * .1, y1 - h * .2)], fill=(214, 230, 240), outline=INK, width=1)
        flag(p, x0 + w * .62, y0 + h * .12, w * .2, h * .2, 'dk')
    elif kind == 'missile':
        p.rect(x0, y0 + h * .7, x1, y1, fill=(214, 196, 160))
        for i in range(5): p.rect(x0 + w * (.1 + i * .17), y0 + h * (.45 - .05 * (i % 2)), x0 + w * (.22 + i * .17), y0 + h * .72, fill=(150, 140, 120))
        p.line([(x1 - w * .1, y0 + h * .1), (cx, y0 + h * .4)], (190, 30, 40), 3); p.circle(cx, y0 + h * .4, h * .07, fill=(240, 140, 40))
    elif kind == 'game':
        p.rrect(cx - w * .32, cy - h * .2, cx + w * .32, cy + h * .25, 12, fill=INK)
        p.text(cx, cy + h * .02, 'VI', serif_b(20), fill=(255, 170, 60), anchor='mm')
    elif kind == 'cyclone':
        for r in (.12, .22, .32): p.d.arc([(cx - w * r) * S, (cy - h * r * 1.2) * S, (cx + w * r) * S, (cy + h * r * 1.2) * S], 30, 300, fill=accent, width=3 * S)
    elif kind == 'gavel':
        p.rect(x0 + w * .2, y1 - h * .22, x1 - w * .2, y1 - h * .12, fill=(120, 80, 50))
        p.poly([(cx - w * .2, y0 + h * .2), (cx + w * .05, y0 + h * .05), (cx + w * .15, y0 + h * .2), (cx - w * .1, y0 + h * .35)], fill=(150, 100, 60))
        p.line([(cx - w * .02, y0 + h * .25), (cx + w * .25, y0 + h * .65)], (150, 100, 60), 4)
    elif kind == 'climate':
        p.circle(cx - w * .12, cy, h * .3, fill=(90, 150, 200)); p.rect(cx + w * .18, y0 + h * .15, cx + w * .26, y0 + h * .75, fill='white', outline=INK, width=1)
        p.circle(cx + w * .22, y0 + h * .78, h * .09, fill=(200, 40, 40)); p.rect(cx + w * .2, y0 + h * .4, cx + w * .24, y0 + h * .75, fill=(200, 40, 40))
    elif kind == 'march':
        for i in range(6):
            px = x0 + w * (.1 + i * .15); p.circle(px, cy - h * .05, h * .08, fill=(70, 60, 60)); p.rect(px - w * .04, cy + h * .03, px + w * .04, cy + h * .3, fill=(70, 60, 60))
        p.rect(x0 + w * .1, y0 + h * .1, x1 - w * .1, y0 + h * .28, fill=(250, 220, 90)); p.text(cx, y0 + h * .19, 'STRIKE', cond_b(10), anchor='mm')
    elif kind == 'runner':
        p.circle(cx, y0 + h * .25, h * .09, fill=(80, 50, 40)); p.line([(cx, y0 + h * .33), (cx - w * .05, y0 + h * .6)], (80, 50, 40), 4)
        p.line([(cx - w * .05, y0 + h * .6), (cx - w * .2, y0 + h * .85)], (80, 50, 40), 4); p.line([(cx - w * .05, y0 + h * .6), (cx + w * .12, y0 + h * .82)], (80, 50, 40), 4)
        p.text(x1 - w * .06, y0 + h * .18, 'BANNED', cond_b(10), fill=(190, 30, 40), anchor='rm')
    elif kind == 'vote':
        p.rect(cx - w * .16, y0 + h * .15, cx + w * .16, y1 - h * .15, fill='white', outline=INK, width=1)
        p.line([(cx - w * .08, cy), (cx - w * .02, cy + h * .12), (cx + w * .1, cy - h * .15)], (40, 130, 70), 3)
    elif kind == 'expel':
        p.rect(cx - w * .22, cy - h * .2, cx + w * .22, cy + h * .2, fill='white', outline=INK, width=1)
        p.line([(cx - w * .22, cy - h * .2), (cx, cy + h * .02), (cx + w * .22, cy - h * .2)], INK, 1)
        p.text(cx + w * .3, cy, '72h', cond_b(12), fill=(190, 30, 40), anchor='mm')
    elif kind == 'jobs':
        for i, v in enumerate([.3, .35, .33, .45, .6]): p.rect(x0 + w * (.12 + i * .16), y1 - h * (.12 + v * .7), x0 + w * (.24 + i * .16), y1 - h * .12, fill=accent)
    else:
        p.circle(cx, cy, h * .25, outline=accent, width=3)


# ------------------------------------------------------------------ map
CONTINENTS = [
    [(-168, 65), (-140, 70), (-95, 72), (-75, 62), (-55, 50), (-80, 25), (-97, 18), (-82, 8), (-105, 20), (-125, 40), (-130, 55)],
    [(-80, 10), (-60, 10), (-35, -7), (-40, -22), (-58, -38), (-70, -55), (-75, -40), (-70, -18), (-81, -5)],
    [(-10, 36), (-9, 44), (-5, 48), (5, 52), (10, 58), (20, 70), (40, 68), (40, 45), (28, 41), (15, 38), (0, 38)],
    [(-17, 15), (-5, 36), (10, 37), (33, 31), (43, 12), (51, 12), (40, -15), (32, -28), (20, -35), (13, -20), (9, 4), (-8, 5)],
    [(40, 45), (40, 68), (70, 73), (110, 77), (140, 72), (180, 68), (160, 58), (140, 45), (122, 30), (108, 18), (100, 10), (80, 8), (72, 20), (58, 25), (48, 30), (35, 32), (28, 41)],
    [(35, 30), (43, 12), (52, 15), (57, 22), (50, 30)], [(95, 5), (120, -5), (140, -8), (105, -8)],
    [(113, -22), (130, -12), (142, -11), (153, -27), (146, -39), (135, -35), (115, -35)],
    [(-55, 60), (-20, 70), (-30, 83), (-60, 80)], [(-6, 50), (2, 51), (-2, 58), (-6, 56)],
    [(130, 31), (141, 36), (142, 45), (138, 40)], [(166, -46), (178, -37), (174, -41)],
]


def world_map(p, x0, y0, x1, y1, pins):
    p.rect(x0, y0, x1, y1, fill=(222, 234, 240))
    def at(lon, lat): return x0 + (lon + 180) / 360 * (x1 - x0), y0 + (78 - lat) / 135 * (y1 - y0)
    for poly in CONTINENTS: p.poly([at(*pt) for pt in poly], fill=(232, 222, 196), outline=(170, 160, 140), width=.6)
    for n, lon, lat, region in pins:
        x, y = at(lon, lat); p.circle(x, y, 7, fill=REGION[region], outline='white', width=1)
        p.text(x, y, str(n), sans_b(8), fill='white', anchor='mm')


# ------------------------------------------------------------------ page
def tally_regions(items):
    t = {r: 0 for r in REGION}
    for st in items: t[st['region']] += 1
    return t


def story_card(p, x0, y0, x1, n, st, big=False):
    ih = 112 if big else 62
    icon(p, st['icon'], x0, y0, x1, y0 + ih, REGION[st['region']])
    y = y0 + ih + 5
    p.circle(x0 + 6, y + 6, 6, fill=REGION[st['region']]); p.text(x0 + 6, y + 6, str(n), sans_b(8), fill='white', anchor='mm')
    p.text(x0 + 16, y + 1, (st['place'] + ' \u00b7 ' + st['field']).upper(), sans_b(8.5 if not big else 9.5), fill=REGION[st['region']])
    y += 15
    y = p.wrap(x0, y, st['head'], serif_b(19 if big else 13.5), x1 - x0, lead=1.12, max_lines=3)
    y = p.wrap(x0, y + 2, st['dek'] + ' \u2014 ' + st['src'], sans(10.5 if big else 9), x1 - x0, fill=GREY, lead=1.22, max_lines=4)
    return y


def main():
    img = Image.new('RGB', (W * S, H * S), PAPER)
    p = Pen(ImageDraw.Draw(img))
    stories = LEADS + SECOND
    count = len(stories) + len(ALSO)
    # masthead
    p.text(16, 10, 'THE WORLD IN ONE PAGE', sans_b(11), fill=(180, 30, 40))
    p.text(1008, 10, f'{count} STORIES \u00b7 {sum(1 for v in tally_regions(stories + ALSO).values() if v)} REGIONS \u00b7 EACH ONE DATED 19 NOV', sans_b(10), anchor='ra')
    p.text(512, 50, 'Thursday 19 November 2026', serif_b(54), anchor='mm')
    p.line([(16, 84), (1008, 84)], INK, 2)
    # region bar
    tally = tally_regions(stories + ALSO)
    x = 16
    for r, c in tally.items():
        w = 992 / len(REGION)
        p.rect(x, 89, x + w - 3, 104, fill=REGION[r]); p.text(x + w / 2 - 1.5, 96.5, f'{r} {c}', sans_b(9), fill='white', anchor='mm'); x += w
    # key figures
    fw = 992 / len(FIGURES)
    for i, (num, lab) in enumerate(FIGURES):
        fx = 16 + i * fw
        p.text(fx + 2, 108, num, serif_b(17), fill=(180, 30, 40)); p.text(fx + 2, 130, lab, sans(8.5), fill=GREY)
        if i: p.line([(fx - 3, 110), (fx - 3, 140)], RULE, 1)
    p.line([(16, 146), (1008, 146)], RULE, 1)
    # leads
    lw = (992 - 2 * 14) / 3
    for i, st in enumerate(LEADS):
        story_card(p, 16 + i * (lw + 14), 152, 16 + i * (lw + 14) + lw, i + 1, st, big=True)
    p.line([(16, 384), (1008, 384)], RULE, 1)
    # second tier: 2 rows of 5
    sw = (992 - 4 * 10) / 5
    for i, st in enumerate(SECOND):
        r, c = divmod(i, 5)
        story_card(p, 16 + c * (sw + 10), 390 + r * 156, 16 + c * (sw + 10) + sw, len(LEADS) + i + 1, st)
    p.line([(16, 704), (1008, 704)], RULE, 1)
    # map + also list
    p.text(16, 711, 'WHERE IT HAPPENED', sans_b(10.5)); p.text(140, 712, 'numbers match the stories', serif(9), fill=GREY)
    pins = [(i + 1, st['lon'], st['lat'], st['region']) for i, st in enumerate(stories) if st['lon'] is not None]
    pins += [(len(stories) + i + 1, a['lon'], a['lat'], a['region']) for i, a in enumerate(ALSO)]
    world_map(p, 16, 728, 316, 912, pins)
    p.text(330, 711, 'ALSO ON THURSDAY 19 NOVEMBER 2026', sans_b(10.5))
    half = (len(ALSO) + 1) // 2
    for i, a in enumerate(ALSO):
        col, row = divmod(i, half)
        x, y = 330 + col * 340, 729 + row * 20.5
        n = len(stories) + i + 1
        p.circle(x + 7, y + 7, 7, fill=REGION[a['region']]); p.text(x + 7, y + 7, str(n), sans_b(8), fill='white', anchor='mm')
        p.text(x + 18, y, a['place'], sans_b(10.5)); off = p.tw(a['place'] + ' ', sans_b(10.5))
        p.text(x + 18 + off, y, a['text'], sans(10.5)); off2 = p.tw(a['text'] + ' ', sans(10.5))
        p.text(x + 18 + off + off2, y + 1.5, a['src'], serif(8.5), fill=GREY)
    # date check + footer
    p.rect(16, 922, 1008, 992, outline=(180, 30, 40), width=1.2)
    p.text(24, 929, 'DATE CHECK', sans_b(11), fill=(180, 30, 40))
    p.wrap(112, 929, DATE_CHECK, sans(10.5), 886, lead=1.3, max_lines=3)
    p.text(512, 1010, 'Claims are attributed, not stated as fact \u00b7 Pictures and map: original, drawn in code \u00b7 Sources: ' + SOURCES, sans(8), fill=GREY, anchor='mm')
    out = Path(__file__).parent / 'assets' / 'entry.png'
    img.resize((W, H), Image.LANCZOS).save(out, optimize=True)
    print(out, out.stat().st_size, 'bytes,', count, 'stories')


if __name__ == '__main__':
    main()
