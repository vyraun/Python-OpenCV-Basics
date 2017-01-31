import cv2

image = cv2.imread("jj.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Shape of the image matrix
print image.shape

# Value of a pixel (Grayscale has only one channel, so only 1 value)
print image[0][0]


cv2.imshow('Picture',image)


cv2.waitKey(0)
cv2.destroyAllWindows()