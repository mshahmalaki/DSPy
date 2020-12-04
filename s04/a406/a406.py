import numpy as np


def compare_array(array1, array2):
    if array1.ndim > array2.ndim:
        print('Number of dimensions of the first array is greater than \n'
              'Number of dimensions of the second array')
    elif array2.ndim > array1.ndim:
        print('Number of dimensions of the second array is greater than \n'
              'Number of dimensions of the first array')
    else:
        print('Number of dimensions of the first array is equal \n'
              'Number of dimensions of the second array')


np_array_1 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
np_array_2 = np.array([[[1, 2], [3, 4]],
                       [[5, 6], [7, 8]]])

compare_array(np_array_1, np_array_2)

