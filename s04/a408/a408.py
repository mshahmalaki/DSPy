import numpy as np
import profile


a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)


def np_concat(np_list1, np_list2):
    # Method 1:
    # Join a sequence of arrays along an existing axis.
    np.concatenate([np_list1, np_list2], axis=1)


def np_hstack(np_list1, np_list2):
    # Method 2:
    # Stack arrays in sequence horizontally (column wise).
    np.hstack([np_list1, np_list2])


def np_c(np_list1, np_list2):
    # Method 3:
    # Translates slice objects to concatenation along the second axis.
    np.c_[np_list1, np_list2]


profile.run('np_concat(a, b)')
profile.run('np_hstack(a, b)')
profile.run('np_c(a, b)')
