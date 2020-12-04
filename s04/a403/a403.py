import numpy as np
from matplotlib import pyplot as plt


# Inflation rate in 1396 in the order of Jalali months
inflation_rates = np.array([9.5, 9.8, 10,
                            10.1, 10, 9.9,
                            9.8, 9.9, 10,
                            10, 9.9, 9.6])

plt.plot(np.arange(1, len(inflation_rates) + 1), inflation_rates)
plt.plot(np.arange(1, len(inflation_rates) + 1), inflation_rates, 'rs')
plt.xlabel('Month')
plt.ylabel('Inflation rate in 1396')
plt.show()
