import matplotlib.pyplot as plt
from skimage.io import imread

image = imread('미술.jpg')

plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.show()
