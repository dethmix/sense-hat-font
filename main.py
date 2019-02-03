# This Python file uses the following encoding: utf-8
from PIL import Image, ImageDraw, ImageFont

original_letters = u' +-*/!"#$><0123456789.=)(ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?,;:|@%[&_\']\~'
letters = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя" #cyrillic letters
full_list = original_letters + letters.upper() + letters
img = Image.new('1', (1000, 8))
font = ImageFont.truetype("PTMono.ttc", 10, encoding="unic")
d = ImageDraw.Draw(img)
d.text((0, -2.5), full_list, fill=1, font=font)
img = img.transpose(Image.ROTATE_270)
img.save("sense_hat_text.png")
with open('sense_hat_text.txt', 'w') as f:
    f.write(full_list)
