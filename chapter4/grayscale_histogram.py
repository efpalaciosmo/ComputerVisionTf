# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image and conver it to grayscale
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)

# Calculate histogram
hist = cv2.calcHist([image], [0], None, [255], [0, 255])

# Plot histogram graph
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.show()
cv2.waitKey(0)