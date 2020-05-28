import numpy as np


class NumPyCreator(object):
    """docstring for NumPyCreator."""

    def __init__(self):
        pass

    def from_list(self, arg):
        return np.array(arg)

    def from_tuple(self, arg):
        return np.array(arg)

    def from_iterable(self, arg):
        return np.array(arg)

    def from_shape(self, arg):
        return np.zeros(arg)

    def random(self, arg):
        return np.random.rand(arg[0], arg[1])

    def identity(self, arg):
        return np.identity(arg)


# npc = NumPyCreator()
# print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
# print(npc.from_tuple(("a", "b", "c")))
#
# print(npc.from_iterable(range(5)))
#
# shape = (3, 5)
# print(npc.from_shape(shape))
#
# print(npc.random(shape))
#
# print(npc.identity(4))
