import numpy as np


def flat_array(np_lst):
    np_lst = np_lst.reshape(-1)
    return np_lst


np_list = np.array([[10, 20, 30, 40],
                    [50, 60, 70, 80]])

print(flat_array(np_list))
