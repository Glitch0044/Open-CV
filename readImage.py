import cv2
image = cv2.imread('kahve.jpeg')

h,w=image.shape[:2]
cv2.imshow('image',image)
cv2.waitKey(0)
print("Height of image:{}, Width of image:{}".format(h,w))

img=cv2.imread('rgb.jpg')
cv2.imshow('image',img)
(B, G, R) = img[500,500]
print("B={},G={},R:{}".format(B,G,R))
B=img[100,100,0]
print("B={}".format(B))
cv2.waitKey(0)
