import numpy as np

np_list = np.array([4, 3, 1, 8, 6, 7, 5, 4, 5])
result = np_list[(np_list >= 4) * (np_list <= 8)]
print(result)
