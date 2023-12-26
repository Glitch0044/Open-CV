import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# cv2.addWeighted is applied over the
# image inputs with applied parameters
resize1 = cv2.resize(image1,(800,600))
resize2 = cv2.resize(image2,(800,600))
weightedSum = cv2.addWeighted(resize1, 0.5, resize2, 0.6, 0)

# the window showing output image
# with the weighted sum
cv2.imshow('Weighted Image', weightedSum)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
