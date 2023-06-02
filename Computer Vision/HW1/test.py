import cv2
import numpy as np

# Loading the images
apple = cv2.imread('orange.png')
orange = cv2.imread('apple.png')

# Resizing the images
apple = cv2.resize(apple, (400, 400))
orange = cv2.resize(orange, (400, 400))

# Loading the binary mask
mask = cv2.imread('mask.png', 0)

# Blending using Laplacian pyramids and binary mask
apple_copy = apple.copy()
orange_copy = orange.copy()

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    orange_copy = cv2.pyrDown(orange_copy)

for i in range(5, -1, -1):
    apple_expanded = cv2.pyrUp(apple_copy)
    orange_expanded = cv2.pyrUp(orange_copy)

    laplacian_apple = cv2.subtract(apple_copy, apple_expanded)
    laplacian_orange = cv2.subtract(orange_copy, orange_expanded)

    blended = cv2.add(cv2.multiply(laplacian_apple, mask), cv2.multiply(laplacian_orange, 255 - mask))

    apple_copy = cv2.add(apple_expanded, blended)
    orange_copy = cv2.add(orange_expanded, blended)

apple_orange_reconstruct = apple_copy

cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
