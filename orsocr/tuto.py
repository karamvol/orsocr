import cv2

one = cv2.imread('./one.jpg', cv2.COLOR_RGB2GRAY)
cv2.imshow("One.jpg", one)

cv2.waitKey(0)
cv2.destroyAllWindows()
# print(one)
