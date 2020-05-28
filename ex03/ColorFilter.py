import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter(object):
    """docstring for ColorFilter."""

    def __init__(self):
        pass

    def invert(self, arr):
        for x in arr:
            for y in x:
                y[0] = 1.0 - y[0]
                y[1] = 1.0 - y[1]
                y[2] = 1.0 - y[2]
        return arr

    def to_blue(self, arr):
        for x in arr:
            for y in x:
                y[1] = 0
                y[0] = 0
        return arr

    def to_red(self, arr):
        for x in arr:
            for y in x:
                y[1] = 0
                y[2] = 0
        return arr

    def to_green(self, arr):
        for x in arr:
            for y in x:
                y[0] = 0
                y[2] = 0
        return arr

    def celluloid(self, arr):
        space = np.linspace(1, 0, 5)
        for x in arr:
            for y in x:
                y[0] = self.getcolor(y[0], space)
                y[1] = self.getcolor(y[1], space)
                y[2] = self.getcolor(y[2], space)
        return arr

    def getcolor(self, color, space):
        for x in space:
            if color >= x:
                return x


cf = ColorFilter()
ip = ImageProcessor()

img = ip.load("musk.png")

ju = cf.celluloid(img)
ip.display(ju)
