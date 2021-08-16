import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reeading and showing the rgb image
image = cv2.imread("images/nature.jpg")
cv2.imshow("Original color image", image)

# Calculate the histogram
colors = ("blue", "green", "red")

for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [32], [0, 256])
    # Plot the graph
    plt.plot(hist, color=color)

plt.title("BGR color histogram")
plt.xlabel("Bins")
plt.ylabel("Numbers of pixels")
plt.show()
cv2.waitKey(0)