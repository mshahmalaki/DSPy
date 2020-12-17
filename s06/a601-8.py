import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

csv = pd.read_csv(r'./pedestrian-and-bicyclist-counts.csv')
pbc = pd.DataFrame(csv)
print('---------------Answer of question 01---------------')
pbc01 = pbc.copy()
pbc01['People'] = pbc01['Pedestrians'] + pbc01['Cyclists']
print(pbc01.head())
print('---------------Answer of question 02---------------')
pbc02 = pbc.copy()
pbc02 = pbc02[(pbc02['Cyclists'] > pbc02['Pedestrians'])]
count_days = pbc02['Date'].count()
print('The number of days that has more cyclists than pedestrians :', count_days, 'day(s)')
print('---------------Answer of question 03---------------')
pbc03 = pbc.copy()
print('Average number of cyclists and pedestrians observed per day:')
print(pbc03.mean())
print('---------------Answer of question 04---------------')
sns.kdeplot(pbc['Pedestrians'])
plt.show()
print('---------------Answer of question 05---------------')
ped_avg_04 = pbc['Pedestrians'].mean()
ped_std_04 = pbc['Pedestrians'].std()
min_range = ped_avg_04 - (3 * ped_std_04)
max_range = ped_avg_04 + (3 * ped_std_04)
if min_range >= 0:
    ped_count_04 = pbc[(pbc['Pedestrians'] >= min_range) & (pbc['Pedestrians'] <= max_range)]['Pedestrians'].count()
else:
    ped_count_04 = pbc[(pbc['Pedestrians'] >= 0) & (pbc['Pedestrians'] <= max_range)]['Pedestrians'].count()
print('99.7% of pedestrian observations', ped_count_04)