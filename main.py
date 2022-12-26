import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from img_change import change


model = keras.models.load_model("model")

pred = model.predict(change("your path"))
print(np.argmax(pred))
