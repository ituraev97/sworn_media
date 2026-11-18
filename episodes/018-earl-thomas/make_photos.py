"""Photos of Earl Thomas from Wikimedia Commons (downloaded as upload.wikimedia.org thumbnails; originals rate-limited):
  earl_2014 / earl_face / earl_hook: "Earl Thomas vs. Redskins 2014.jpg" (Oct 6, 2014), Keith Allison, CC BY-SA 2.0 (1920px)
  earl_2018: "Earl Thomas (defensive back)—2018.JPG", Jeffrey Beall, CC BY 4.0 (1280px)
  earl_2011: "Earl Thomas (defensive back).JPG", Jeffrey Beall, CC BY-SA 3.0 (960px)
  earl_back: "Earl Thomas vs Rams 2013.jpg", Mike Morris, CC BY-SA 2.0 (1280px)"""
from PIL import Image, ImageFilter
import os
S = '/home/claude/dl18/wm2/'; O = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img/')
r = Image.open(S + 'redskins_full.jpg').convert('RGB')
r.crop((640, 60, 1800, 1500)).save(O + 'earl_2014.jpg', quality=92)
face = r.crop((900, 220, 1620, 1100)); face.save(O + 'earl_face.jpg', quality=93)
bg = face.resize((1080, 1920), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
fr = face.resize((1080, int(face.height * 1080 / face.width)), Image.LANCZOS)
bg.paste(fr, (0, -60)); bg.save(O + 'earl_hook.jpg', quality=92)
Image.open(S + 'Earl_Thomas_%28defensive_back%29%E2%80%942018.JPG').convert('RGB').save(O + 'earl_2018.jpg', quality=90)
Image.open(S + 'Earl_Thomas_%28defensive_back%29.JPG').convert('RGB').save(O + 'earl_2011.jpg', quality=90)
Image.open(S + 'rams2013.jpg').convert('RGB').crop((0, 0, 1280, 1700)).save(O + 'earl_back.jpg', quality=90)
print('ok', face.size, fr.size)
