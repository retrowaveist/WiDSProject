import cv2
import numpy as np
# Load the image
image = cv2.imread("C:\\Users\mariy\Pictures\Screenshots\\yeetus.png")

# Convert image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Get the saturation channel
saturation = hsv_image[:, :, 1]

# Increase saturation by 30
saturation += 30

# Clipping the saturation value between 0 and 255
saturation = np.clip(saturation, 0, 255)

# Update the saturation channel
hsv_image[:, :, 1] = saturation

# Convert image back to BGR color space
saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Show the saturated image
cv2.imshow("Saturated Image", saturated_image)
cv2.waitKey(0)

# Save the saturated image
cv2.imwrite("saturated_image.jpg", saturated_image)
