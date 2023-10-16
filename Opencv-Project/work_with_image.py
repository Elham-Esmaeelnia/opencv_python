import cv2
import numpy
img = cv2.imread("ax.jpg")
cv2.imshow("img",img)
print(img.shape)
print(img.dtype)
px = img[100,100]
print(px)
blue = img[150,150,0]
print(blue)
#-----ROI------#
ball = img[300:500,450:600]
#---------------------------------#
cv2.waitKey(0)
cv2.destroyAllWindows()