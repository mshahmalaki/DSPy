import numpy as np
import matplotlib.pyplot as plt


city_list = np.array(['Tehran', 'Karaj'])
pop_1390 = np.array([12183391, 2412513])
pop_1395 = np.array([13267637, 2712400])

width = 0.3
plt.bar(city_list, pop_1395, color='g', width=width)
plt.bar(city_list, pop_1390, color='y', width=width)
plt.show()
