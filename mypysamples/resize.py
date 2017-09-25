import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

resized = imutils.resizeImage(image, width=150)
cv2.imshow("resized (width) image", resized)
cv2.waitKey(0)

resized = imutils.resizeImage(image, height=50)
cv2.imshow("resized (height) image", resized)
cv2.waitKey(0)