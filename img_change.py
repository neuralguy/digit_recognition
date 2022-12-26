import cv2
import numpy as np


def change(img):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bitwise_not(img)
    img = np.around(np.divide(img, 255.0), decimals=1)
    img = np.expand_dims(img, axis=0)
    return img
