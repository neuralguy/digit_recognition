import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from img_change import change


model = keras.models.load_model("models/classnumber/conv_model")


def class_img(img):
    img = change(img)
    pred = model.predict(img)
    print(np.argmax(pred))

    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()


if __name__ == '__main__':
    img = "imgs/numbers/2.png"    # path to your image
    class_img(img)
