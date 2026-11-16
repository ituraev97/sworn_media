from PIL import Image, ImageFilter
E = '/home/claude/sworn_media/episodes/016-rozier/img/'
f = Image.open(E + 'rozier_face.jpg').convert('RGB')
bg = f.resize((1080, 1920), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30))
w = 1080; h = int(f.height * w / f.width)
fr = f.resize((w, h), Image.LANCZOS)
bg.paste(fr, (0, -260))
bg.save(E + 'rozier_hook.jpg', quality=92)
print(bg.size, h)
