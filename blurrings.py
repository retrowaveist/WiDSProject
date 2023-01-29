import cv2

# Load the image
image = cv2.imread("C:\\Users\mariy\Pictures\Screenshots\\yeetus.png")

# Apply Gaussian Blur
kernel_size = (13, 13)
blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

# Apply Median Blur
kernel_size = 5
median_blurred_image = cv2.medianBlur(image, kernel_size)

# Show the median blurred image
cv2.imshow("Median Blurred Image", median_blurred_image)

# Show the gaussian blurred image
cv2.imshow("Gaussian Blurred Image", blurred_image)
cv2.waitKey(0)


