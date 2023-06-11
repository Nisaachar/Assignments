import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# line detection method in vectorized format
def line_detection_vectorized(image, edge_image, num_rhos=180, num_thetas=180, t_count=220):
  # Get the dimensions of the edge image
  edge_height, edge_width = edge_image.shape[:2]
  edge_height_half, edge_width_half = edge_height / 2, edge_width / 2

  # Calculate the maximum distance from the origin to the image corners
  d = np.sqrt(np.square(edge_height) + np.square(edge_width))

  # Calculate the increments of theta and rho
  dtheta = 180 / num_thetas
  drho = (2 * d) / num_rhos

  # Generate arrays of theta and rho values
  thetas = np.arange(0, 180, step=dtheta)
  rhos = np.arange(-d, d, step=drho)

  # Precompute cosine and sine values of theta
  cos_thetas = np.cos(np.deg2rad(thetas))
  sin_thetas = np.sin(np.deg2rad(thetas))

  # Create an accumulator array to store Hough transform values
  accumulator = np.zeros((len(rhos), len(rhos)))

  # Create a figure and subplots for visualization
  figure = plt.figure(figsize=(12, 12))
  subplot1 = figure.add_subplot(1, 4, 1)
  subplot2 = figure.add_subplot(1, 4, 2)
  subplot3 = figure.add_subplot(1, 4, 3)
  subplot4 = figure.add_subplot(1, 4, 4)

  # Display the original image and edge image
  subplot1.imshow(image)
  subplot2.imshow(edge_image, cmap="gray")

  # Set the background color of the Hough space subplot
  subplot3.set_facecolor((0, 0, 0))

  # Display the original image in the last subplot
  subplot4.imshow(image)

  # Adjust edge points based on the center of the image
  edge_points = np.argwhere(edge_image != 0)
  edge_points = edge_points - np.array([[edge_height_half, edge_width_half]])

  # Compute rho values for edge points
  rho_values = np.matmul(edge_points, np.array([sin_thetas, cos_thetas]))

  # Perform 2D histogram accumulation
  accumulator, theta_vals, rho_vals = np.histogram2d(
      np.tile(thetas, rho_values.shape[0]),
      rho_values.ravel(),
      bins=[thetas, rhos]
  )
  accumulator = np.transpose(accumulator)

  # Find lines with sufficient votes in the accumulator
  lines = np.argwhere(accumulator > t_count)
  rho_idxs, theta_idxs = lines[:, 0], lines[:, 1]
  r, t = rhos[rho_idxs], thetas[theta_idxs]

  # Plot the detected lines in Hough space
  for ys in rho_values:
    subplot3.plot(thetas, ys, color="white", alpha=0.05)
  subplot3.plot([t], [r], color="yellow", marker='o')

  # Plot the detected lines on the original image
  for line in lines:
    y, x = line
    rho = rhos[y]
    theta = thetas[x]
    a = np.cos(np.deg2rad(theta))
    b = np.sin(np.deg2rad(theta))
    x0 = (a * rho) + edge_width_half
    y0 = (b * rho) + edge_height_half
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    subplot3.plot([theta], [rho], marker='o', color="yellow")
    subplot4.add_line(mlines.Line2D([x1, x2], [y1, y2]))

  # Invert y-axis and x-axis for Hough space plot
  subplot3.invert_yaxis()
  subplot3.invert_xaxis()

  # Set titles for the subplots
  subplot1.title.set_text("Original Image")
  subplot2.title.set_text("Edge Image")
  subplot3.title.set_text("Hough Space")
  subplot4.title.set_text("Detected Lines")

  # Show the plot
  plt.show()

  # Return the accumulator, rhos, and thetas for further analysis if needed
  return accumulator, rhos, thetas


if __name__ == "__main__":
  # Process three images for line detection
  for i in range(1):
    # Read an image file
    image = cv2.imread(f"circle.jpg")

    # Convert the image to grayscale
    edge_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    edge_image = cv2.GaussianBlur(edge_image, (3, 3), 1)

    # Apply Canny edge detection
    edge_image = cv2.Canny(edge_image, 100, 200)

    # Dilate the edges for better line detection
    edge_image = cv2.dilate(
        edge_image,
        cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
        iterations=1
    )

    # Erode the edges to reduce thickness
    edge_image = cv2.erode(
        edge_image,
        cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
        iterations=1
    )

    # Perform line detection using the vectorized method
    line_detection_vectorized(image, edge_image)
