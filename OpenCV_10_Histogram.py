import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img =  cv.imread('C:/Users/User 2/Desktop/park.jpg')
cv.imshow('Meow', img)
cv.waitKey(0)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)
cv.imshow("mask", mask)
cv.waitKey(0)

##For grayscale image

hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


##For BGR image
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist_color = cv.calcHist([img], [i], None, [256], [0, 256])
    
    plt.xlabel("Bins")
    plt.ylabel("Number of pixels")
    plt.plot(hist_color, color=col)
    plt.xlim([0, 256])
plt.show()