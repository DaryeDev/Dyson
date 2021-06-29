from PIL import Image, ImageDraw, ImageFilter, ImageOps

bg = Image.open('test/img/CallAnAmbulance....png').convert("RGBA")
width, height = bg.size
im2 = Image.open('test/img/test.png')
mask = Image.open("test/img/circuloMask.png").convert("L")
im2 = im2.resize((100, 100), Image.ANTIALIAS)
ironman = ImageOps.fit(im2, mask.size, centering=(0.5, 0.5))
ironman.putalpha(mask)
ironman.save("test/img/round.png")
ironman = ironman.resize((100, 100), Image.ANTIALIAS)

text_img = Image.new('RGBA', (width,height), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(ironman, (90,-5), mask=ironman)
text_img.save("ball.png", format="png")