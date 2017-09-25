import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

rotated = imutils.rotate(image, 45)
cv2.imshow("Image Rotated by 45 deg", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, -90)
cv2.imshow("Image Rotated by 90 deg", rotated)
cv2.waitKey(0)