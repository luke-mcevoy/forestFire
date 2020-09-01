import cv2
import matplotlib.pyplot as plt

forest = cv2.imread('test2.JPG', 0)
th2 = cv2.adaptiveThreshold(forest, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
# plt.imshow(th2, cmap='gray')
plt.imshow(th2)
plt.show()

