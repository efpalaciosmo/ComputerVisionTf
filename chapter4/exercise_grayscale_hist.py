# plot a histogram of an image with 32 bins. Try to interpret
# the output graph.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)

hist = cv2.calcHist([image], [0], None, [32], [0, 255])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.show()
cv2.waitKey(0)