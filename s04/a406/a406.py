import numpy as np


np_array_1 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
np_array_2 = np.array([[[1, 2], [3, 4]],
                       [[5, 6], [7, 8]]])
print(np_array_1.shape)
print(np_array_2.shape)
if np_array_1.ndim > np_array_2.ndim:
    print('Number of dimensions of the first array is greater than \n'
          'Number of dimensions of the second array')
elif np_array_2.ndim > np_array_1.ndim:
    print('Number of dimensions of the second array is greater than \n'
          'Number of dimensions of the first array')
else:
    print('Number of dimensions of the first array is equal \n'
          'Number of dimensions of the second array')
