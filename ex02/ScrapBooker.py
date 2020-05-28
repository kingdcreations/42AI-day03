import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker(object):
    """docstring for ScrapBooker."""

    def __init__(self):
        pass

    def crop(self, arr, dim, pos=(0, 0)):
        if dim[0] > arr.shape[0] or dim[1] > arr.shape[1]:
            raise ValueError(
                f"Dimension too high {dim[0]} > {arr.shape[0]}"
                + f" or {dim[1]} > {arr.shape[1]} ")
        startx = pos[0]
        starty = pos[1]
        cropx = dim[0]
        cropy = dim[1]
        obj = arr[starty:starty+cropy, startx:startx+cropx]
        return obj

    def thin(self, arr, n, axis):
        if axis == 0:
            return np.delete(arr, slice(n-1, None, n), 1)
        elif axis == 1:
            return np.delete(arr, slice(n-1, None, n), 0)

    def juxtapose(self, arr, n, axis):
        obj = arr
        for x in range(0, n):
            obj = np.concatenate((obj, arr), axis=axis)
        return obj

    def mosaic(self, arr, dim):
        dim += (1,)
        return np.tile(arr, dim)


sb = ScrapBooker()
ip = ImageProcessor()

img = ip.load("ahah.png")

cr = sb.crop(img, (img.shape[0]//2, img.shape[1]//2), (0, 0))
ip.display(cr)

ju = sb.thin(img, 2, 0)
ip.display(ju)

ju = sb.juxtapose(img, 3, 0)
ip.display(ju)

ju = sb.mosaic(img, (20, 20))
ip.display(ju)
