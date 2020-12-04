import numpy as np


transaction_list = np.array([1500, 1100, 200, -300, -2000, 1300])

cum_sum = transaction_list.cumsum()
print(cum_sum)