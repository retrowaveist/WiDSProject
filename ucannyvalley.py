#exercise 3.2, pencil sketch of live video footage
import cv2
from matplotlib import pyplot as plt
cv2.namedWindow("Live Video Feed", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    cv2.imshow("Live Video Feed", frame)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    assert img is not None, "file could not be read, check with os.path.exists()"
    edges = cv2.Canny(img, 100, 200)
    img_inv = cv2.bitwise_not(edges)
    cv2.imshow("canny", img_inv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

