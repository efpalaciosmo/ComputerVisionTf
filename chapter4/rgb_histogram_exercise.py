# Here’s an exercise for you: create a histogram of a masked image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading and showing the rgb image
image = cv2.imread("images/nature.jpg")
cv2.imshow("Original color image", image)
cv2.waitKey(-1)

# Creating a maks
mask = cv2.rectangle(np.zeros(image.shape[:2], dtype="uint8"),
                       (50, 50), (int(image.shape[1])-50,int(image.shape[0] / 2)-50),
                       (255, 255, 255), -1)
cv2.imshow("Mask  image", mask)
cv2.waitKey(-1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked  image", masked)
cv2.waitKey(-1)

# Calculate the histogram
colors = ("blue", "green", "red")

for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [32], [0, 256])
    # Plot the graph
    plt.plot(hist, color=color)

plt.title("BGR color histogram")
plt.xlabel("Bins")
plt.ylabel("Numbers of pixels")

for i, color in enumerate(colors):
    maskedHist = cv2.calcHist([masked], [i], None, [32], [0, 256])
    # Plot the graph
    plt.plot(maskedHist, color=color)

plt.title("BGR color histogram for maked image")
plt.xlabel("Bins")
plt.ylabel("Numbers of pixels")
plt.show()

cv2.waitKey(0) 