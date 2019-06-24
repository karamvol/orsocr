from PIL import Image
import pytesseract

from preprocessor import process


def recognize(image):
    grayImage = process(image)
    pillow_image = Image.fromarray(grayImage.astype('uint8'))
    # Read it with tesseract
    text = pytesseract.image_to_string(
        pillow_image, config='tessedit_char_whitelist=0123456789 -psm 6 ')

    return [''.join([y for y in x if y.isdigit()]) for x in text.split('\n')]


if __name__ == '__main__':
    print(recognize("three.png"))
