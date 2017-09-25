import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

flipped = imutils.flipImage(image, horizontal=1)
cv2.imshow("Image flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = imutils.flipImage(image, vertical=0)
cv2.imshow("Image flipped vertically", flipped)
cv2.waitKey(0)

flipped = imutils.flipImage(image, horizontalAndVertical=-1)
cv2.imshow("Image flipped Horizontally & vertically", flipped)
cv2.waitKey(0)