import numpy as np
import cv2
cam = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cam.read()
    if ret is False:
        break
    # Shrink the frame
    frame = cv2.resize(frame, (480, 360))
    # Convert the frame to Grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    trapezoid = np.empty_like(frame)
    # Add a named window
    cv2.namedWindow("trapezoid", cv2.WINDOW_NORMAL)
    # cv2.imshow("trapezoid")
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()