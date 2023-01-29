
import cv2
import numpy as np

# Load image
img = cv2.imread("C:\\Users\mariy\Pictures\Saved Pictures\\shapee.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Find contours
#contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours
for cnt in contours:
    # Get the perimeter of the contour
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
    if len(approx) == 3:
        shape = "triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspectRatio = w / float(h)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            shape = "square"
        elif aspectRatio > 1:
            shape = "rectangle"
        elif aspectRatio < 1:
            shape = "rhombus"
    elif len(approx) == 5:
        shape = "pentagon"
    elif len(approx) == 6:
        shape = "hexagon"
    elif len(approx) == 7:
        shape = "heptagon"
    elif len(approx) == 8:
        shape = "octagon"
    else:
        # Use the `minEnclosingCircle` method to get the center coordinates and radius of the enclosing circle of the shape.
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        area = cv2.contourArea(cnt)
        # classify the shape to circle or ellipse
        if abs(1 - (float(area) / (np.pi * radius * radius))) <= 0.2:
            shape = "circle"
        else:
            shape = "ellipse"
    if shape != 'circle' and shape != 'ellipse':
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        center = (cX, cY)
    cv2.putText(img, shape, (center[0], center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

# Show image
cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()