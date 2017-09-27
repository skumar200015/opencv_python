import numpy as np
import cv2

#translation matrix
#[1, 0, tx] - firt row of matrix, where tx is the # of pixels to be shifted left(-ve) or right(+ve)
#[1, 0, ty] - firt row of matrix, where ty is the # of pixels to be shifted up(-ve) or down(+ve)
def translate(image, posX, posY):
    M = np.float32([[1, 0, posX], [0, 1, posY]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def resizeImage(image, width=None, height=None, inter=cv2.INTER_AREA):
    #shape[0] - height
    #shape[1] - width

    dim = None
    (h, w) = image.shape[:2] #get both height and width

    if width is None and height is None:
        return image

    if width is None:
        r = height/float(h)
        dim = (int(w * r), height)
    else:
        r = width/float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def flipImage(image, horizontal=None, vertical=None, horizontalAndVertical=None):
    if horizontal is None and vertical is None and horizontalAndVertical is None:
        return image

    if horizontal:
        flipped = cv2.flip(image, 1)
        return flipped

    if vertical:
        flipped = cv2.flip(image, 0)
        return flipped

    if horizontalAndVertical:
        flipped = cv2.flip(image, -1)
        return flipped

