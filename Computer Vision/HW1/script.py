import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def laplacian_pyramid(image, num_levels):
    pyramid = [image]
    for i in range(num_levels):
        image = image.resize((image.width // 2, image.height // 2), resample=Image.BILINEAR)
        pyramid.append(image)
    return pyramid

def reconstruct_laplacian_pyramid(pyramid):
    num_levels = len(pyramid) - 1
    reconstructed = pyramid[num_levels]
    for i in range(num_levels, 0, -1):
        expanded = Image.new('RGB', pyramid[i - 1].size)
        expanded.paste(reconstructed, (0, 0, reconstructed.width, reconstructed.height))
        reconstructed = Image.fromarray(np.array(pyramid[i - 1]) + np.array(expanded))
    return reconstructed

# Load the image
image = Image.open('apple.png')

# Convert image to numpy array
image_array = np.array(image)

# Define the number of levels in the pyramid
num_levels = 4

# Create Laplacian pyramid
pyramid = laplacian_pyramid(image, num_levels)

# Display the down-scaled images and residual images
fig, axes = plt.subplots(1, num_levels + 1, figsize=(15, 4))
axes[0].imshow(pyramid[0])
axes[0].set_title('Level 1 Downscaled')

for i in range(1, num_levels + 1):
    residual_shape = pyramid[i - 1].size
    residual = np.array(pyramid[i - 1]) - np.array(pyramid[i].resize(residual_shape, resample=Image.BILINEAR))
    axes[i].imshow(residual + 128, cmap='gray')
    axes[i].set_title(f'Level {i} Residual')

plt.tight_layout()
plt.show()
