import numpy as np
import matplotlib.pyplot as plt
import cv2

depth_forest = cgv2.imread('test2.jpg')
sample = cv2.cvtColor(depth_forest, cv2.COLOR_BGR2RGB)

# convert from RGB to HSV
hsv = cv2.cvtColor(depth_forest, cv2.COLOR_RGB2HSV)

# 1. define our color selection criteria in HSV value
lower_hue = np.array([50, 50, 50])
upper_hue = np.array([200, 200, 200])

# 2. mask the image using HSV
mask_hsv = cv2.inRange(hsv, lower_hue, upper_hue)
masked_image = np.copy(sample)
masked_image[mask_hsv==0] = [0,0,0]

plt.imshow(masked_image)
plt.show()