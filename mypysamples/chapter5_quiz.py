import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype='uint8')

for (row, y) in enumerate(range(0, 300, 10)):
    for(col, x) in enumerate(range(0, 300, 10)):
        red=(0,0,255)
        if row % 2 == col % 2:
            red = (0, 0, 0)

        cv2.rectangle(canvas, (x, y), (x+10, y + 10), red, -1)

(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
green=(0, 255, 0)
cv2.circle(canvas, (centerX, centerY), 30, green, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)