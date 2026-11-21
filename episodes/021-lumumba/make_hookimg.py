"""Face crop + 1080x1920 Shorts hook images.
Face: Wikimedia Commons "File:Chokwe Antar Lumumba.jpg" — NatalieMaynor, CC BY 2.0 (May 10, 2017). Uses the original
(2103x2416) when it could be downloaded (/home/claude/dl/face/a_orig.jpg), else the 1280px rendition.
Hook images from the indictment photos (img/ph_*.jpg, made by make_img.py)."""
import os
from PIL import Image, ImageFilter, ImageEnhance
HERE = os.path.dirname(os.path.abspath(__file__)); IMG = os.path.join(HERE, 'img')
src = '/home/claude/dl/face/a_orig.jpg'
try:
    f = Image.open(src); f.load()
except Exception:
    f = Image.open('/home/claude/dl/face/a.jpg')
f = f.convert('RGB'); W, H = f.size
# face + shoulders panel (fractions of the full photo)
face = f.crop((int(0.255 * W), int(0.115 * H), int(0.745 * W), int(0.60 * H)))
face = ImageEnhance.Contrast(face).enhance(1.08)
face.save(os.path.join(IMG, 'lumumba_face.jpg'), quality=93)
print('face', face.size, 'from', f.size)
def hook(im, name, y=0, scale_w=1080):
    im = im.convert('RGB')
    bg = im.resize((1080, 1920), Image.LANCZOS).filter(ImageFilter.GaussianBlur(34))
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    h = int(im.height * scale_w / im.width); fr = im.resize((scale_w, h), Image.LANCZOS)
    bg.paste(fr, ((1080 - scale_w) // 2, y))
    bg.save(os.path.join(IMG, name), quality=92); print(name, h)
hook(face, 'h_face.jpg', y=40)                                  # eyes ~ y 430
ph = Image.open(os.path.join(IMG, 'ph_call.jpg'))
hook(ph.crop((0, 0, int(ph.width * 0.62), ph.height)), 'h_call.jpg', y=60)   # the man on the phone (left of the still)
hook(Image.open(os.path.join(IMG, 'ph_book.jpg')), 'h_book.jpg', y=120)
