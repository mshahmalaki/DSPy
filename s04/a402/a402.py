import numpy as np
import matplotlib.pyplot as plt


city_list = np.array(['Tehran', 'Karaj'])
pop_1390 = np.array([12183391, 2412513])
pop_1395 = np.array([13267637, 2712400])

plt.barh(city_list, pop_1395, color='g')
plt.barh(city_list, pop_1390, color='y')
plt.show()
