from PIL import Image
import pytesseract
im = Image.open('jaune.png')
im = im.convert('L')
im.save('temp.png')
text = pytesseract.image_to_string(Image.open(
    'temp.png'), config='tessedit_char_whitelist=0123456789 -psm 6')
print("####  Raw text ####")
print(text)
print()
print("#### Extracted digits ####")
print([''.join([y for y in x if y.isdigit()]) for x in text.split('\n')])
