import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract


moniteur = "two.png"

image = cv2.imread(moniteur, 1)


# Extraction seulement des chiffres
# Lower bounds: [ 34 115   0]
# Upper bounds: [255 255 255]

# ou
# Lower bounds: [ 34 115   0]
# Upper bounds: [255 255 255]

# vert 157.02° 59.12% 62.35%  --> 171.54° 51.66% 59.22%

#imageHSV= cv2.cvtColor(image,cv2.COLOR_BGR2HSV);

#low_vert = np.array( [157,59,62])
#up_vert = np.array( [171,51,60])

# vert presque OK
#low_vert = np.array( [100,145,30])
#up_vert = np.array( [140,255,255])

# BGR optimized
low_vert = np.array([82, 116, 0])
up_vert = np.array([152, 255, 86])


# bleu 197.63° 93.16% 74.51%  -> 201.88° 89.6% 79.22%
#low_bleu = np.array([187,100,0] )
#up_bleu = np.array( [206,150,255])

# BGR optimiazed
low_bleu = np.array([153, 73, 0])
up_bleu = np.array([255, 255, 69])


# jaune  84.66° 49.32% 58.04% -> 86.36° 44% 58.82%
#low_jaune = np.array([33,57,25] )
#up_jaune = np.array( [85,255,255])

# BGR Optimized Jaune

low_jaune = np.array([0, 111, 86])
up_jaune = np.array([151, 255, 255])


mask_vert = cv2.inRange(image, low_vert, up_vert)
mask_bleu = cv2.inRange(image, low_bleu, up_bleu)
mask_jaune = cv2.inRange(image, low_jaune, up_jaune)
#mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
#image_bleu = mask


#kernel = np.ones((1,1), np.uint8);

#image2 = cv2.dilate(image2,kernel,iterations=1);
#image2 = cv2.erode(image2, kernel, iterations=1);
imageb = cv2.bitwise_and(image, image, mask=mask_bleu)
#imageb = cv2.adaptiveThreshold(imageb, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2 )


#cv2.imwrite("3_treated.png", image2)

#cv2.imshow('imadge dilated', np.hstack((mask_bleu, mask_vert, mask_jaune)))

cv2.imshow('Original', image)
cv2.imshow('Jaune', mask_jaune)
cv2.imshow('Vert', mask_vert)
cv2.imshow("bleu", imageb)

#resltat = pytesseract.image_to_string(Image.open("3_treated.png"))

# print(resltat)

# image_dilated =

# cv2.imshow('image',image)


cv2.waitKey(0)
cv2.destroyAllWindows()
