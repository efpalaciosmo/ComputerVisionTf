# Imoport histogram
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read and image and convert it into grayscale
image = cv2.imread("images/nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)

# Calculate histogram of the original image
hist = cv2.calcHist([image], [0], None, [256], [0, 255])

# Plot histogram graph
plt.figure()
plt.title("Grayscale histogram of otiginal image")
plt.xlabel("Bins")
plt.ylabel("Equalized image")
plt.plot(hist)
plt.show()

# Equalizing image
equalizedImage = cv2.equalizeHist(image)
cv2.imshow("Equalized image", equalizedImage)

# Calculate histogram of the original image
histEqualized = cv2.calcHist([equalizedImage], [0], None, [256], [0,255])

# Plot histogram graph
plt.title("Grayscale histogram of equalized image")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(histEqualized)
plt.show()
cv2.waitKey(0)