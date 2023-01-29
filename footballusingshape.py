#programme to detect football in video using shape detection
import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture("C:\\Users\mariy\Downloads\\leomessi.mp4")

prevCircle = None
dist = lambda x1, y1, x2, y2: (x1-x2)**2+ (y1-y2) ** 2


while True:
    # Read the video frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurframe = cv2.GaussianBlur(gray, (17,17), 0)
    # Apply the Hough Circle Transform
    circles = cv2.HoughCircles(blurframe, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=25, maxRadius=75)

    # Draw the circles on the frame
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen =i
            if prevCircle is not None:
                if dist(chosen[0],chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen

    # Show the frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


