import numpy as np


np_list = np.array([[10, 20, 30, 40],
                    [50, 60, 70, 80]])
np_list_new = np_list.reshape(4, -1)
print(np_list_new)
print('Number of dimensions :', np_list_new.ndim)
print('Shape :', np_list_new.shape)
