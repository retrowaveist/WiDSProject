import cv2

# Create a background subtractor
backSub = cv2.createBackgroundSubtractorMOG2()

# Open a video capture
cap = cv2.VideoCapture("C:\\Users\mariy\Downloads\\leomessi.mp4")

# Read the first frame
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set the template for the ball
template = cv2.imread("C:\\Users\mariy\Pictures\Screenshots\\scr147.png", cv2.IMREAD_GRAYSCALE)

# Get the width and height of the template
w, h = template.shape[::-1]

while True:
    # Read the next frame
    ret, frame = cap.read()

    # If the frame was read successfully
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurframe = cv2.GaussianBlur(gray, (17, 17), 0)
        # Apply background subtraction
        fgMask = backSub.apply(blurframe)

        # Find the location of the ball using brute force matching
        res = cv2.matchTemplate(fgMask, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match is above a certain threshold
        threshold = 0.1
        if max_val > threshold:
            # Draw a rectangle around the ball
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # Show the frame
        cv2.imshow("Frame", frame)

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # If the frame was not read successfully
    else:
        break

cap.release()
cv2.destroyAllWindows()
