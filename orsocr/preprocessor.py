import numpy as np
import cv2
from PIL import Image
import pytesseract

"""
    Return a processed version of image in gray
"""


def process(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img = cv2.blur(img, (5, 5))

    #HSV (hue, saturation, value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # Applying threshold on pixels' Value (or Brightness)
    thresh = cv2.adaptiveThreshold(
        v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Finding contours
    image, contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filling contours
    contours = cv2.drawContours(img, np.array(
        contours), -1, (255, 255, 255), -1)

    # To black and white
    grayImage = cv2.cvtColor(contours, cv2.COLOR_BGR2GRAY)

    # And inverting it
    # Setting all `dark` pixels to white
    grayImage[grayImage > 200] = 0
    # Setting relatively clearer pixels to black
    grayImage[grayImage < 100] = 255

    return grayImage


if __name__ == '__main__':
    cv2.imshow("Processed", process('./orsocr/three.png'))
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
