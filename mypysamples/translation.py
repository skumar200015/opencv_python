import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#translation matrix
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down & Right", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, -50, -90)
cv2.imshow("Shifted up and left", shifted)
cv2.waitKey(0)
