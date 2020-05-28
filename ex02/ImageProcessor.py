import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageProcessor():
    """docstring for ImageProcessor."""

    def __init__(self):
        pass

    def load(self, path):
        img = mpimg.imread(path)
        print(f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
        return (img)

    def display(self, img):
        plt.imshow(img)
        plt.show()

#
# img = ImageProcessor()
# arr = img.load('ahah.png')
# img.display(arr)
