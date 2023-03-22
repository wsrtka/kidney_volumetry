"""All things used to vizualize the algorithm."""

import matplotlib.pyplot as plt


def plot_image(image):
    plt.figure(figsize=(12,7))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_two_images(image1, image2):
    plot, ax = plt.subplots(1, 2, figsize=(12, 7))
    ax[0].imshow(image1, cmap='gray')
    ax[0].axis('off')
    ax[1].imshow(image2, cmap='gray')
    ax[1].axis('off')
    plt.show()
