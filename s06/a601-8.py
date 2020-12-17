import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

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
ped_avg_03 = pbc['Pedestrians'].mean()
ped_median_03 = pbc['Pedestrians'].median()
sns.displot(pbc['Pedestrians'])
plt.axvline(ped_avg_03, color='y')
plt.axvline(ped_median_03, color='r')
plt.legend({'Mean': ped_avg_03, 'Median': ped_median_03})
plt.show()

print('---------------Answer of question 05---------------')
ped_std_04 = pbc['Pedestrians'].std()
min_range = ped_avg_03 - (3 * ped_std_04)
max_range = ped_avg_03 + (3 * ped_std_04)
if min_range >= 0:
    ped_count_04 = pbc[(pbc['Pedestrians'] >= min_range) & (pbc['Pedestrians'] <= max_range)]['Pedestrians'].count()
else:
    ped_count_04 = pbc[(pbc['Pedestrians'] >= 0) & (pbc['Pedestrians'] <= max_range)]['Pedestrians'].count()
print('99.7% of pedestrian observations', ped_count_04)

print('---------------Answer of question 06---------------')
ped_count_05 = pbc[(pbc['Pedestrians'] <= np.percentile(pbc['Pedestrians'], q=75))]['Pedestrians'].count()
print('75% of pedestrian observations:', ped_count_05, 'people')

print('---------------Answer of question 07---------------')
print('Standard deviation of pedestrians:', '{:.2f}'.format(ped_std_04))
print('Range of observation:', np.ptp(pbc['Pedestrians']))

print('---------------Answer of question 08---------------')
cyclists_skew = pbc['Cyclists'].skew()
cyclists_kurt = pbc['Cyclists'].kurtosis()
print('Skewness of cyclists distribution', '{:.2f}'.format(cyclists_skew))
print('Kurtosis of cyclists distribution', '{:.2f}'.format(cyclists_kurt))
if (abs(cyclists_skew) <= float('2')) & (abs(cyclists_kurt) <= float('2')):
    print('The cyclists distribution is normal')
