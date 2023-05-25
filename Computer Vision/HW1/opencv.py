import cv2
import numpy as np

def laplacian_pyramid(image, num_levels):
    pyramid = [image]
    for i in range(num_levels):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

def reconstruct_laplacian_pyramid(pyramid):
    num_levels = len(pyramid) - 1
    reconstructed = pyramid[num_levels]
    for i in range(num_levels, 0, -1):
        expanded = cv2.pyrUp(reconstructed)
        expanded = cv2.resize(expanded, pyramid[i - 1].shape[::-1])
        reconstructed = cv2.add(pyramid[i - 1], expanded)
    return reconstructed

def blend_images(image1, image2, mask, num_levels):
    # Create Laplacian pyramids for each image
    image1_pyramid = laplacian_pyramid(image1, num_levels)
    image2_pyramid = laplacian_pyramid(image2, num_levels)

    # Create blended pyramid using the mask
    blended_pyramid = []
    for i in range(num_levels):
        height, width = image1_pyramid[i].shape[:2]
        mask_resized = cv2.resize(mask, (width, height))
        mask_normalized = mask_resized / 255.0

        blended_level = image1_pyramid[i] * (1 - mask_normalized) + image2_pyramid[i] * mask_normalized
        blended_pyramid.append(blended_level)

    # Reconstruct the blended image from the pyramid
    blended_image = reconstruct_laplacian_pyramid(blended_pyramid)

    return blended_image




# Load the images
image1 = cv2.imread('apple.png')
image2 = cv2.imread('orange.png')
mask = cv2.imread('mask.png', 0)

# Normalize the mask to range [0, 1]
mask = mask / 255.0

# Blend the images
num_levels = 5
blended_image = blend_images(image1, image2, mask, num_levels)

# Display the blended image
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
