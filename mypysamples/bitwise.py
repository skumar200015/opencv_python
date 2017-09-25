import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

#AND: A bitwise AND is true if and only if both pixels are greater than zero.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("bitWiseAnd", bitwiseAnd)
cv2.waitKey(0)

#OR: A bitwise OR is true if either of the two pixels are greater than zero.
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow("bitWiseOR", bitwiseOR)
cv2.waitKey(0)

#XOR: A bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both.
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("bitwiseXOR", bitwiseXOR)
cv2.waitKey(0)

#NOT:A bitwise NOT inverts the “on” and “off” pixels in an image.
bitwiseNOT = cv2.bitwise_not(rectangle, circle)
cv2.imshow("bitwizeNOT", bitwiseNOT)
cv2.waitKey(0)
