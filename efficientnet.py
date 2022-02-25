
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

from keras.applications.imagenet_utils import decode_predictions
from efficientnet import EfficientNetB0, EfficientNetB3
from efficientnet import center_crop_and_resize, preprocess_input

import os
model = EfficientNetB0(weights='imagenet')
def inference(model,image_path):
    image = imread(image_path)

    image_size = model.input_shape[1]
    cx = center_crop_and_resize(image,image_size=image_size)

    x = preprocess_input(cx)
    x = np.expand_dims(x,0)

    y = model.predict(x)
    dy = decode_predictions(y)[0]

    for idx, label, confidence in dy:
        print('%s: %.2f%%' % (label, confidence * 100))
    plt.figure(figsize=(5,5))
    plt.imshow(cx.astype(np.uint8))
    plt.show()
