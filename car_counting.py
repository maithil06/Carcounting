import cv2
import numpy as np

# Background subtractor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

# Counting line position and vehicle counter
count_line_position = 550
offset = 6
counter = 0

# Minimum rectangle size for detected vehicle
min_width = 80
min_height = 80

def center_handle(x, y, w, h):
    """Return the center point of the rectangle."""
    cx = int(x + w / 2)
    cy = int(y + h / 2)
    return cx, cy

# List of detected centers
detect = []

# Capture video
cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (25, count_line_position), (1200, count_line_position), (0, 255, 0), 2)

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w < min_width or h < min_height:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame, center, 4, (0, 0, 255), -1)

    for (cx, cy) in detect[:]:
        if count_line_position - offset < cy < count_line_position + offset:
            counter += 1
            cv2.line(frame, (25, count_line_position), (1200, count_line_position), (225, 125, 0), 4)
            detect.remove((cx, cy))
            print('Number of vehicles:' + str(counter))

    cv2.putText(frame, "NUMBER OF VEHICLES :" + str(counter), (250, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow('Video Frame', frame)
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
