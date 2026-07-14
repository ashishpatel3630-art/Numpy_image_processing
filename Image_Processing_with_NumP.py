import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


img = Image.open("/Users/aashishmewada/Desktop/p2/Numpy_projects/ImageNumPy/sample.jpg")
img_array = np.array(img)


def grayscale(image):
    gray = np.dot(image[..., :3], [0.299, 0.587, 0.114])
    return gray.astype(np.uint8)

def blur(image):
    kernel = np.ones((3, 3)) / 9

    padded = np.pad(image, ((1,1),(1,1)), mode='edge')
    result = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+3, j:j+3]
            result[i, j] = np.sum(region * kernel)

    return result


def flip_horizontal(image):
    return np.fliplr(image)

def flip_vertical(image):
    return np.flipud(image)


def rotate_90(image):
    return np.rot90(image)


gray = grayscale(img_array)


blurred = blur(gray)


flipped = flip_horizontal(gray)


rotated = rotate_90(gray)


plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")

plt.subplot(2,2,2)
plt.imshow(blurred, cmap='gray')
plt.title("Blurred")

plt.subplot(2,2,3)
plt.imshow(flipped, cmap='gray')
plt.title("Flipped")

plt.subplot(2,2,4)
plt.imshow(rotated, cmap='gray')
plt.title("Rotated")

plt.show()