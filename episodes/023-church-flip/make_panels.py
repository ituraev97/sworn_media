"""Thumbnail panels (640x720) and Shorts hook backgrounds (1080x1920) for 023.
Face = the defendant's photo embedded in the government trial exhibit (summary chart p.2, media/1473651), used at its NATIVE size
(306x336 px, never enlarged). Charts = img/f_*.jpg (private names blacked out by make_img.py)."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os
HERE = os.path.dirname(os.path.abspath(__file__)); IMG = os.path.join(HERE, 'img')
FACE = Image.open('/home/claude/work/023/ras/face-000.png').convert('RGB')
SLATE = (54, 65, 75)
F = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def font(n): return ImageFont.truetype(F, n)
def framed(face, b=8):
    w, h = face.size; c = Image.new('RGB', (w + 2 * b, h + 2 * b), (0, 0, 0)); c.paste(face, (b, b)); return c
def backdrop(W, H, src='f_never', dark=0.45):
    im = Image.open(f'{IMG}/{src}.jpg').convert('RGB')
    s = max(W / im.width, H / im.height); im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x = (im.width - W) // 2; y = (im.height - H) // 2; im = im.crop((x, y, x + W, y + H)).filter(ImageFilter.GaussianBlur(18))
    return Image.blend(im, Image.new('RGB', (W, H), (0, 0, 0)), dark)
def t_face():
    W, H = 640, 720; c = Image.new('RGB', (W, H), SLATE); f = framed(FACE)
    c.paste(f, ((W - f.width) // 2, 26)); d = ImageDraw.Draw(c)
    d.text((W // 2, 26 + f.height + 14), 'RICHARD GARCIA', font=font(30), fill=(235, 235, 235), anchor='mt')
    c.save(f'{IMG}/t_face.jpg', quality=93)
def t_never():
    im = Image.open(f'{IMG}/f_never.jpg'); c = im.crop((60, 400, 1000, 800))  # Hazel + Queens boxes, PROCEEDS $0
    W, H = 640, 720; s = W / c.width; c = c.resize((W, int(c.height * s)), Image.LANCZOS)
    out = Image.new('RGB', (W, H), SLATE); out.paste(c, (0, 60)); d = ImageDraw.Draw(out)
    d.text((W // 2, 18), 'GOV\'T TRIAL EXHIBIT (DRAFT CHART)', font=font(22), fill=(200, 200, 200), anchor='mt')
    out.save(f'{IMG}/t_never.jpg', quality=93)
def hook(name, src='f_never'):
    W, H = 1080, 1920; c = backdrop(W, H, src); f = framed(FACE, 10)
    c.paste(f, ((W - f.width) // 2, 370)); d = ImageDraw.Draw(c)
    d.text((W // 2, 370 + f.height + 12), 'RICHARD GARCIA · GOV\'T TRIAL EXHIBIT', font=font(30), fill=(240, 240, 240), anchor='mt')
    c.save(f'{IMG}/{name}.jpg', quality=92)
if __name__ == '__main__':
    t_face(); hook('h_face', 'f_tx1'); hook('h_face2', 'f_rg2'); hook('h_face3', 'f_lub')
    print('ok')
