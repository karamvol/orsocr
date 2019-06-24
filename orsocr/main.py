from recognizer import recognize


def orsocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    return recognize(filename)


if __name__ == '__main__':
    print(orsocr_core('./orsocr/three.png'))
