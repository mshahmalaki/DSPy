import numpy as np
from math_functions.functions import list_average, compare_avg


np_list = np.array([[10, 20, 30, 40],
                    [50, 60, 70, 80]])
sum_columns = np_list.sum(axis=0)
sum_rows = np_list.sum(axis=1)

print(compare_avg(list_average(sum_columns), list_average(sum_rows)))
