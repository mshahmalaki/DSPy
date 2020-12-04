import numpy as np

a = np.arange(1, 7)
b = a.reshape(3, 2)
print('3 * 2 numpy array :\n', b)
b[[0, 1]] = b[[1, 0]]
print('3 * 2 numpy array with swapped rows :\n', b)
