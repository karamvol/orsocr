import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("three.png")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temporary.jpg')
text = pytesseract.image_to_string(Image.open('temporary.jpg'))
print(text)
