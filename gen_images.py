"""Generate textured product images for the Hunza Handicrafts site.

These are procedurally drawn — woven cloth, wood grain, felt, stone — rather
than clip art. Output: PNG files into images/.
"""

from PIL import Image, ImageDraw, ImageFilter, ImageChops
import random, math, os

random.seed(11)
OUT = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT, exist_ok=True)

W, H = 900, 675  # 4:3

SLATE = (43, 58, 66)
APRICOT = (232, 163, 61)
SNOW = (247, 245, 240)
WALNUT = (92, 64, 51)
PINE = (63, 94, 76)


def noise(size, amount=18):
    w, h = size
    img = Image.new("L", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            px[x, y] = 128 + random.randint(-amount, amount)
    return img


def add_grain(img, amount=10):
    g = noise(img.size, amount).convert("RGB")
    return ImageChops.overlay(img, g)


def vignette(img, strength=0.42):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-w * 0.25, -h * 0.3, w * 1.25, h * 1.3], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(w * 0.16))
    dark = Image.new("RGB", (w, h), (20, 24, 28))
    return Image.composite(img, Image.blend(img, dark, strength), mask)


def backdrop(base, warm=True):
    """Soft studio backdrop with a light falloff."""
    img = Image.new("RGB", (W, H), base)
    d = ImageDraw.Draw(img)
    for i in range(H):
        t = i / H
        c = tuple(int(base[j] * (1 - t * 0.18)) for j in range(3))
        d.line([(0, i), (W, i)], fill=c)
    # pool of light upper-left
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-W * 0.1, -H * 0.35, W * 0.75, H * 0.75], fill=90)
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    light = Image.new("RGB", (W, H), (255, 250, 240) if warm else (245, 248, 255))
    img = Image.composite(light, img, glow.point(lambda v: v))
    return img


def soft_shadow(img, box, blur=28, opacity=95):
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).ellipse(box, fill=opacity)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    dark = Image.new("RGB", img.size, (60, 52, 44))
    return Image.composite(dark, img, sh)


# ---------------------------------------------------------------- textiles

def woven(size, warp, weft, pitch=7, jitter=1):
    """Plain-weave cloth: interlacing warp/weft with fibre jitter."""
    w, h = size
    img = Image.new("RGB", (w, h), warp)
    d = ImageDraw.Draw(img)
    for y in range(0, h, pitch):
        for x in range(0, w, pitch):
            over = ((x // pitch) + (y // pitch)) % 2 == 0
            c = weft if over else warp
            c = tuple(max(0, min(255, v + random.randint(-12, 12))) for v in c)
            jx = random.randint(-jitter, jitter)
            d.rectangle([x + jx, y, x + pitch - 1 + jx, y + pitch - 1], fill=c)
    img = img.filter(ImageFilter.GaussianBlur(0.6))
    return add_grain(img, 12)


def shawl():
    img = backdrop((238, 232, 220))
    cloth = woven((640, 470), (222, 210, 188), (200, 186, 162), pitch=6)
    cd = ImageDraw.Draw(cloth)
    # apricot stripe bands
    for x in (90, 320, 550):
        for k in range(10):
            a = 200 - k * 12
            cd.line([(x + k, 0), (x + k, 470)], fill=(232, 163, 61), width=1)
    for x in (86, 316, 546):
        cd.line([(x, 0), (x, 470)], fill=(150, 100, 40), width=2)
    # fringe
    fr = Image.new("RGB", (640, 40), (238, 232, 220))
    fd = ImageDraw.Draw(fr)
    for x in range(0, 640, 4):
        fd.line([(x, 0), (x + random.randint(-2, 2), random.randint(20, 38))],
                fill=(214, 202, 180), width=2)
    cloth.paste(fr, (0, 430))

    # drape: shear the cloth slightly
    cloth = cloth.transform((640, 470), Image.AFFINE, (1, 0.06, -14, 0.02, 1, 0),
                            resample=Image.BICUBIC, fillcolor=(238, 232, 220))
    img = soft_shadow(img, [140, 150, 790, 570], blur=34)
    img.paste(cloth, (130, 100))
    return vignette(add_grain(img, 8))


def cap():
    img = backdrop((236, 231, 222))
    img = soft_shadow(img, [270, 400, 640, 520], blur=26)
    d = ImageDraw.Draw(img)
    # crown
    d.pieslice([300, 190, 600, 470], 180, 360, fill=(233, 227, 214),
               outline=(120, 110, 96), width=3)
    # felt texture on crown
    crown = woven((300, 140), (233, 227, 214), (219, 212, 197), pitch=4)
    mask = Image.new("L", (300, 140), 0)
    ImageDraw.Draw(mask).pieslice([0, 0, 300, 280], 180, 360, fill=255)
    img.paste(crown, (300, 190), mask)
    d.pieslice([300, 190, 600, 470], 180, 360, outline=(120, 110, 96), width=3)
    # rolled band
    d.rounded_rectangle([280, 330, 620, 420], radius=22, fill=(63, 94, 76),
                        outline=(38, 58, 47), width=3)
    band = woven((330, 80), (63, 94, 76), (52, 78, 63), pitch=4)
    img.paste(band, (285, 335))
    d.rounded_rectangle([280, 330, 620, 420], radius=22, outline=(38, 58, 47), width=3)
    # silk embroidery on band
    for i, x in enumerate(range(310, 600, 30)):
        d.ellipse([x, 366, x + 12, 378], fill=APRICOT, outline=(150, 100, 30))
        d.line([(x + 6, 350), (x + 6, 366)], fill=(214, 190, 150), width=2)
    return vignette(add_grain(img, 8))


def rug():
    img = backdrop((240, 235, 224))
    felt = Image.new("RGB", (660, 470), (236, 228, 212))
    fd = ImageDraw.Draw(felt)
    # matted fibre texture
    for _ in range(9000):
        x, y = random.randint(0, 660), random.randint(0, 470)
        a = random.random() * math.pi
        L = random.randint(4, 14)
        c = random.choice([(225, 216, 198), (243, 236, 222), (214, 204, 184)])
        fd.line([(x, y), (x + L * math.cos(a), y + L * math.sin(a))], fill=c, width=2)
    felt = felt.filter(ImageFilter.GaussianBlur(0.8))
    # appliqué border
    fd = ImageDraw.Draw(felt)
    fd.rectangle([0, 0, 659, 469], outline=(92, 64, 51), width=8)
    fd.rectangle([40, 40, 619, 429], outline=PINE, width=6)
    # centre medallion
    cx, cy = 330, 235
    fd.ellipse([cx - 92, cy - 92, cx + 92, cy + 92], fill=APRICOT, outline=(150, 100, 35), width=4)
    star = []
    for i in range(16):
        a = math.pi * 2 * i / 16 - math.pi / 2
        r = 78 if i % 2 == 0 else 34
        star.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    fd.polygon(star, fill=(247, 245, 240), outline=(150, 100, 35))
    fd.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=PINE)
    # corner motifs
    for (ox, oy) in [(90, 90), (570, 90), (90, 380), (570, 380)]:
        fd.polygon([(ox, oy - 26), (ox + 22, oy), (ox, oy + 26), (ox - 22, oy)],
                   fill=PINE, outline=(92, 64, 51))
    img = soft_shadow(img, [110, 130, 800, 580], blur=30)
    img.paste(felt, (120, 100))
    return vignette(add_grain(img, 9))


# ---------------------------------------------------------------- wood

def wood_texture(size, base=(139, 101, 71), dark=(92, 64, 51), rings=True):
    w, h = size
    img = Image.new("RGB", (w, h), base)
    d = ImageDraw.Draw(img)
    cx, cy = w * 0.5, h * 0.5
    if rings:
        for r in range(4, int(max(w, h) * 0.9), random.randint(5, 11)):
            t = random.uniform(0.25, 0.85)
            c = tuple(int(base[i] + (dark[i] - base[i]) * t) for i in range(3))
            wob = random.uniform(0.9, 1.1)
            d.ellipse([cx - r * wob, cy - r * 0.72, cx + r * wob, cy + r * 0.72],
                      outline=c, width=random.randint(2, 4))
    for _ in range(400):  # grain streaks
        y = random.randint(0, h)
        x = random.randint(0, w)
        L = random.randint(20, 90)
        c = tuple(int(base[i] + (dark[i] - base[i]) * random.uniform(0.1, 0.5)) for i in range(3))
        d.line([(x, y), (x + L, y + random.randint(-3, 3))], fill=c, width=1)
    img = img.filter(ImageFilter.GaussianBlur(0.7))
    return add_grain(img, 10)


def bowl():
    img = backdrop((236, 230, 220))
    img = soft_shadow(img, [190, 430, 740, 560], blur=30)
    d = ImageDraw.Draw(img)
    # outer body
    d.chord([190, 180, 720, 540], 0, 180, fill=(104, 74, 55))
    body = wood_texture((530, 360))
    m = Image.new("L", (530, 360), 0)
    ImageDraw.Draw(m).chord([0, 0, 530, 360], 0, 180, fill=255)
    img.paste(body, (190, 180), m)
    d.chord([190, 180, 720, 540], 0, 180, outline=(58, 40, 30), width=3)
    # rim
    d.ellipse([190, 140, 720, 240], fill=(150, 112, 80), outline=(58, 40, 30), width=3)
    # interior
    d.ellipse([214, 152, 696, 228], fill=(88, 61, 46))
    inner = wood_texture((482, 76), base=(112, 80, 58), dark=(64, 44, 33))
    im = Image.new("L", (482, 76), 0)
    ImageDraw.Draw(im).ellipse([0, 0, 482, 76], fill=255)
    img.paste(inner, (214, 152), im)
    d.ellipse([214, 152, 696, 228], outline=(58, 40, 30), width=2)
    # specular highlight on rim
    hl = Image.new("L", (W, H), 0)
    ImageDraw.Draw(hl).arc([200, 145, 710, 245], 190, 260, fill=120, width=12)
    hl = hl.filter(ImageFilter.GaussianBlur(9))
    img = Image.composite(Image.new("RGB", (W, H), (255, 240, 214)), img, hl)
    return vignette(add_grain(img, 8))


def panel():
    img = backdrop((234, 227, 216))
    plank = wood_texture((600, 480), base=(158, 118, 80), dark=(96, 66, 46), rings=False)
    d = ImageDraw.Draw(plank)

    def carve(pts, depth=9):
        # dark recessed groove
        for k in range(depth, 0, -1):
            v = 46 + (depth - k) * 4
            d.polygon([(x, y) for x, y in pts], outline=(v, int(v * 0.7), int(v * 0.52)), width=5)
            pts = [(x, y) for x, y in pts]
        # lit upper-left bevel, shadowed lower-right
        d.polygon([(x - 3, y - 3) for x, y in pts], outline=(206, 162, 116), width=2)
        d.polygon([(x + 3, y + 3) for x, y in pts], outline=(64, 42, 30), width=2)
        d.polygon(pts, outline=(52, 34, 24), width=3)

    # interlocking Altit-style geometry
    cx, cy = 300, 240
    for scale in (150, 100, 52):
        carve([(cx, cy - scale), (cx + scale, cy), (cx, cy + scale), (cx - scale, cy)])
    for scale in (130, 84):
        carve([(cx - scale, cy - scale), (cx + scale, cy - scale),
               (cx + scale, cy + scale), (cx - scale, cy + scale)])
    # border rails
    d.rectangle([14, 14, 585, 465], outline=(74, 50, 36), width=6)
    d.rectangle([30, 30, 569, 449], outline=(104, 74, 52), width=3)
    for x in range(50, 570, 40):  # dentil band
        d.rectangle([x, 36, x + 20, 52], outline=(74, 50, 36))
        d.rectangle([x, 428, x + 20, 444], outline=(74, 50, 36))
    plank = plank.filter(ImageFilter.SMOOTH)
    img = soft_shadow(img, [140, 110, 780, 590], blur=30)
    img.paste(plank, (150, 98))
    return vignette(add_grain(img, 9))


# ---------------------------------------------------------------- jewellery

def metal_gradient(size, light=(228, 228, 224), dark=(120, 122, 124)):
    w, h = size
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = abs(math.sin(y / h * math.pi * 1.6))
        c = tuple(int(dark[i] + (light[i] - dark[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    return img


def pendant():
    img = backdrop((228, 229, 228), warm=False)
    d = ImageDraw.Draw(img)
    # chain: two catenary strands meeting at the bail
    for side in (-1, 1):
        for i in range(30):
            t = i / 29
            x = 450 + side * (1 - t) * 300
            # catenary sag toward the bail
            y = 96 + (1 - math.cos(t * math.pi * 0.5)) * 150 + math.sinh(t * 1.2) * 14
            r = 6 + t * 1.5
            d.ellipse([x - r, y - r, x + r, y + r], outline=(176, 178, 178), width=3)
            d.arc([x - r, y - r, x + r, y + r], 200, 320, fill=(232, 233, 231), width=2)
    # bail
    d.ellipse([428, 232, 472, 284], outline=(150, 152, 152), width=7)
    d.arc([428, 232, 472, 284], 190, 300, fill=(228, 229, 227), width=3)
    # body
    pts = [(450, 286), (566, 400), (450, 592), (334, 400)]
    d.polygon(pts, fill=(196, 198, 196), outline=(96, 98, 98))
    met = metal_gradient((240, 310))
    mm = Image.new("L", (240, 310), 0)
    ImageDraw.Draw(mm).polygon([(x - 334, y - 286) for x, y in pts], fill=255)
    img.paste(met, (334, 286), mm)
    d.polygon(pts, outline=(88, 90, 90), width=3)
    # granulation
    for i in range(22):
        t = i / 22
        a = t * math.pi * 2
        d.ellipse([450 + 96 * math.cos(a) - 3, 400 + 132 * math.sin(a) - 3,
                   450 + 96 * math.cos(a) + 3, 400 + 132 * math.sin(a) + 3],
                  fill=(232, 233, 231), outline=(140, 142, 142))
    # rough ruby
    ruby = [(450, 350), (500, 400), (450, 470), (400, 400)]
    d.polygon(ruby, fill=(150, 32, 46), outline=(72, 12, 20))
    d.polygon([(450, 362), (486, 400), (450, 452), (414, 400)], fill=(182, 44, 60))
    d.polygon([(450, 372), (466, 398), (450, 424), (434, 398)], fill=(214, 76, 92))
    d.line([(438, 386), (452, 372)], fill=(250, 200, 205), width=3)
    return vignette(add_grain(img, 7))


def cuff():
    img = backdrop((230, 230, 229), warm=False)
    img = soft_shadow(img, [230, 470, 690, 570], blur=26)
    d = ImageDraw.Draw(img)
    # band
    d.ellipse([230, 200, 690, 500], fill=(206, 208, 206), outline=(96, 98, 98), width=4)
    met = metal_gradient((460, 300), light=(236, 236, 232), dark=(146, 148, 148))
    mm = Image.new("L", (460, 300), 0)
    ImageDraw.Draw(mm).ellipse([0, 0, 460, 300], fill=255)
    img.paste(met, (230, 200), mm)
    d.ellipse([230, 200, 690, 500], outline=(90, 92, 92), width=4)
    # opening / inner face
    d.ellipse([300, 250, 620, 450], fill=(238, 237, 234), outline=(120, 122, 122), width=3)
    d.ellipse([300, 250, 620, 450], outline=(150, 152, 152), width=2)
    # brushed streaks
    for _ in range(500):
        a = random.uniform(0, math.pi * 2)
        r = random.uniform(0, 1)
        x = 460 + math.cos(a) * (160 + r * 60)
        y = 350 + math.sin(a) * (110 + r * 40)
        d.line([(x, y), (x + 6, y)], fill=(220, 221, 219), width=1)
    # stone setting along the top
    stones = [(-0.55, "lapis"), (-0.3, "jade"), (0, "lapis"), (0.3, "jade"), (0.55, "lapis")]
    for off, kind in stones:
        x = 460 + off * 210
        y = 350 - math.cos(off) * 140 - 6
        col = (46, 78, 143) if kind == "lapis" else (63, 110, 84)
        hi = (86, 122, 190) if kind == "lapis" else (104, 156, 122)
        d.ellipse([x - 20, y - 20, x + 20, y + 20], fill=(176, 178, 176), outline=(96, 98, 98), width=2)
        d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=col)
        d.ellipse([x - 8, y - 10, x + 2, y + 0], fill=hi)
        d.ellipse([x - 6, y - 8, x - 1, y - 3], fill=(226, 232, 244))
    return vignette(add_grain(img, 7))


# ---------------------------------------------------------------- pantry

def apricots():
    img = backdrop((240, 232, 216))
    img = soft_shadow(img, [200, 440, 720, 570], blur=28)
    d = ImageDraw.Draw(img)

    def fruit(cx, cy, r, base, wrinkled=True):
        # body
        for i in range(r, 0, -1):
            t = i / r
            c = tuple(int(base[j] * (0.55 + 0.45 * (1 - t))) for j in range(3))
            d.ellipse([cx - i, cy - i * 0.94, cx + i, cy + i * 0.94], fill=c)
        # crease
        d.arc([cx - r * 0.25, cy - r, cx + r * 0.25, cy + r], 250, 290,
              fill=tuple(int(c * 0.7) for c in base), width=3)
        if wrinkled:
            for _ in range(50):
                a = random.uniform(0, math.pi * 2)
                rr = random.uniform(0.2, 0.85) * r
                x, y = cx + math.cos(a) * rr, cy + math.sin(a) * rr * 0.94
                d.arc([x - 9, y - 6, x + 9, y + 6], random.randint(0, 180),
                      random.randint(180, 360),
                      fill=tuple(int(c * 0.74) for c in base), width=2)
        # highlight
        hl = Image.new("L", (W, H), 0)
        ImageDraw.Draw(hl).ellipse([cx - r * 0.5, cy - r * 0.7, cx - r * 0.05, cy - r * 0.25], fill=90)
        return hl

    # sun-dried = brown, not orange
    spots = [(360, 400, 92, (150, 92, 46)), (520, 360, 84, (168, 106, 52)),
             (470, 470, 78, (138, 84, 42)), (620, 440, 70, (158, 98, 48)),
             (300, 480, 62, (166, 104, 50)), (560, 262, 56, (146, 90, 44))]
    hls = Image.new("L", (W, H), 0)
    for cx, cy, r, base in spots:
        h = fruit(cx, cy, r, base)
        hls = ImageChops.lighter(hls, h)
    hls = hls.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (255, 236, 200)), img, hls)
    # a couple of kernels
    for kx, ky in [(700, 520), (742, 496)]:
        d.ellipse([kx - 22, ky - 15, kx + 22, ky + 15], fill=(198, 176, 140),
                  outline=(150, 130, 96), width=2)
        d.line([(kx - 14, ky), (kx + 14, ky)], fill=(160, 138, 104), width=2)
    return vignette(add_grain(img, 9))


def bottle():
    img = backdrop((238, 234, 224))
    img = soft_shadow(img, [300, 560, 620, 630], blur=24)
    d = ImageDraw.Draw(img)
    # glass body
    body = [352, 180, 568, 590]
    d.rounded_rectangle(body, radius=26, fill=(214, 186, 132), outline=(96, 84, 60), width=3)
    # oil fill with gradient
    for y in range(250, 588):
        t = (y - 250) / 338
        c = (int(236 - t * 44), int(172 - t * 46), int(64 - t * 20))
        d.line([(356, y), (564, y)], fill=c)
    d.rounded_rectangle([352, 240, 568, 590], radius=24, outline=(120, 96, 50), width=2)
    # neck + cork
    d.rectangle([428, 118, 492, 190], fill=(206, 190, 150), outline=(96, 84, 60), width=3)
    d.rounded_rectangle([420, 92, 500, 128], radius=8, fill=(150, 112, 72), outline=(90, 62, 40), width=3)
    for yy in range(98, 124, 7):
        d.line([(424, yy), (496, yy)], fill=(126, 92, 58), width=1)
    # glass highlights
    hl = Image.new("L", (W, H), 0)
    hd = ImageDraw.Draw(hl)
    hd.rounded_rectangle([372, 210, 398, 560], radius=12, fill=110)
    hd.rounded_rectangle([534, 260, 550, 520], radius=8, fill=60)
    hl = hl.filter(ImageFilter.GaussianBlur(7))
    img = Image.composite(Image.new("RGB", (W, H), (255, 252, 240)), img, hl)
    # label
    d.rectangle([368, 330, 552, 470], fill=(247, 245, 240), outline=(120, 110, 92), width=2)
    d.line([(368, 356), (552, 356)], fill=PINE, width=3)
    d.line([(368, 446), (552, 446)], fill=PINE, width=3)
    # label lettering suggestion
    for i, yy in enumerate(range(376, 440, 14)):
        wdt = [130, 96, 112, 70][i % 4]
        d.line([(384, yy), (384 + wdt, yy)], fill=(120, 112, 96), width=3)
    d.ellipse([500, 372, 536, 408], outline=APRICOT, width=3)
    return vignette(add_grain(img, 8))


# ---------------------------------------------------------------- hero

def hero():
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (206, 222, 236))
    d = ImageDraw.Draw(img)
    # sky gradient
    for y in range(h):
        t = y / h
        c = (int(150 + 80 * t), int(178 + 62 * t), int(206 + 34 * t))
        d.line([(0, y), (w, y)], fill=c)

    def ridge(base_y, amp, colr, seed, detail=6):
        random.seed(seed)
        pts = [(0, base_y)]
        x = 0
        while x < w:
            step = random.randint(40, 110)
            x += step
            base_y += random.randint(-amp, amp)
            pts.append((x, base_y))
        # jagged peaks
        out = [(0, h)]
        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            for k in range(detail):
                t = k / detail
                out.append((x0 + (x1 - x0) * t,
                            y0 + (y1 - y0) * t + random.randint(-14, 14)))
        out.append((w, h))
        d.polygon(out, fill=colr)
        return out

    ridge(430, 46, (150, 166, 182), 3)
    ridge(500, 54, (112, 132, 150), 7)
    peaks = ridge(560, 62, (74, 94, 112), 13)
    # snow caps on the near ridge
    for i in range(0, len(peaks) - 1, 3):
        x, y = peaks[i]
        if 0 < x < w and y < 620:
            d.polygon([(x, y), (x + 26, y + 34), (x - 26, y + 34)], fill=(238, 242, 246))
    # valley floor
    d.polygon([(0, h), (0, 700), (w, 660), (w, h)], fill=(96, 116, 86))
    # terraced fields
    for i, yy in enumerate(range(700, 900, 26)):
        c = (108 + i * 5, 130 + i * 4, 92 + i * 3)
        d.polygon([(0, yy), (w, yy - 34), (w, yy - 34 + 18), (0, yy + 18)], fill=c)
    # apricot trees
    random.seed(21)
    for _ in range(60):
        x = random.randint(0, w)
        y = random.randint(710, 890)
        r = random.randint(6, 16)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(72, 96, 62))
        d.line([(x, y), (x, y + r)], fill=(62, 44, 34), width=2)
    img = img.filter(ImageFilter.SMOOTH)
    img = add_grain(img, 6)
    # haze
    haze = Image.new("RGB", (w, h), (226, 234, 240))
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle([0, 380, w, 620], fill=70)
    m = m.filter(ImageFilter.GaussianBlur(70))
    img = Image.composite(haze, img, m)
    return img


# ---------------------------------------------------------------- run

JOBS = {
    "shawl": shawl, "cap": cap, "rug": rug,
    "bowl": bowl, "panel": panel,
    "pendant": pendant, "cuff": cuff,
    "apricots": apricots, "bottle": bottle,
}

for name, fn in JOBS.items():
    im = fn()
    im.save(os.path.join(OUT, f"{name}.jpg"), quality=86, optimize=True)
    print("wrote", name)

hero().save(os.path.join(OUT, "hero-valley.jpg"), quality=84, optimize=True)
print("wrote hero-valley")
