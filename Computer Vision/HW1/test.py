import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def laplacian_pyramid(image, num_levels):
    pyramid = [image]
    for i in range(num_levels):
        image = image[::2, ::2]
        pyramid.append(image)
    return pyramid

def reconstruct_laplacian_pyramid(pyramid):
    num_levels = len(pyramid) - 1
    reconstructed = pyramid[num_levels]
    for i in range(num_levels, 0, -1):
        expanded = np.repeat(reconstructed, 2, axis=0)
        expanded = np.repeat(expanded, 2, axis=1)
        reconstructed = pyramid[i - 1] + expanded
    return reconstructed

def blend_images(image1, image2, mask, num_levels):
    # Create Laplacian pyramids for each image
    image1_pyramid = laplacian_pyramid(image1, num_levels)
    image2_pyramid = laplacian_pyramid(image2, num_levels)

    # Create blended pyramid using the mask
    blended_pyramid = []
    for i in range(num_levels):
        mask_resized = np.resize(mask, image1_pyramid[i].shape[:2])
        mask_expanded = np.expand_dims(mask_resized, axis=2)
        blended_level = image1_pyramid[i] * (1 - mask_expanded) + image2_pyramid[i] * mask_expanded
        blended_pyramid.append(blended_level)

    # Reconstruct the blended image from the pyramid
    blended_image = reconstruct_laplacian_pyramid(blended_pyramid)

    # Normalize the blended image to [0, 1]
    blended_image = np.clip(blended_image, 0, 1)

    return blended_image



# Load the images
image1 = np.array(Image.open('apple.png').convert('RGB'))
image2 = np.array(Image.open('orange.png').convert('RGB'))
mask = np.array(Image.open('mask.png').convert('L'))

# Normalize the mask to range [0, 1]
mask = mask / 255.0

# Blend the images
num_levels = 5
blended_image = blend_images(image1, image2, mask, num_levels)

# Display the blended image
plt.imshow(blended_image)
plt.axis('off')
plt.show()