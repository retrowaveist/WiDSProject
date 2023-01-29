import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(hsv, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        # Detect eyes in the grayscale region of interest
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Draw a circular border around each detected eye
        for (ex, ey, ew, eh) in eyes:
            cv2.circle(frame, (x + ex + int(ew / 2), y + ey + int(eh / 2)), int(ew / 2), (0, 255, 0), 2)

    # Display the output
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()