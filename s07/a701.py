import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


csv = pd.read_csv(r'./pedestrian-and-bicyclist-counts.csv')
pbc = pd.DataFrame(csv)

print('---------------Answer of question 01-01---------------')
fig, axes = plt.subplots(4, 2, figsize=(15, 10), sharex=True)
sns.boxplot(pbc['Pedestrians'], ax=axes[0, 0])
sns.boxenplot(pbc['Pedestrians'], ax=axes[1, 0])
sns.histplot(pbc['Pedestrians'], ax=axes[2, 0])
sns.kdeplot(pbc['Pedestrians'], ax=axes[3, 0])

sns.boxplot(pbc['Cyclists'], ax=axes[0, 1])
sns.boxenplot(pbc['Cyclists'], ax=axes[1, 1])
sns.histplot(pbc['Cyclists'], ax=axes[2, 1])
sns.kdeplot(pbc['Cyclists'], ax=axes[3, 1])

plt.show()

print('\n---------------Answer of question 01-02---------------\n')


def find_outliers(df, label, min_iqr, max_iqr):
    loc = 0
    count = 1
    print(f'----------lookup outlier(s) in {label} ...')
    for item in df:
        if not(min_iqr <= item <= max_iqr):
            print(f'{count}- outlier in location {loc} found: ', item)
            count += 1
        loc += 1
    if count == 1:
        print(f'Woo, There isn\'t any outliers in {label}')


ped_q1 = np.percentile(pbc['Pedestrians'], q=25)
ped_q3 = np.percentile(pbc['Pedestrians'], q=75)
cyc_q1 = np.percentile(pbc['Cyclists'], q=25)
cyc_q3 = np.percentile(pbc['Cyclists'], q=75)

ped_iqr = ped_q3 - ped_q1
cyc_iqr = cyc_q3 - cyc_q1

min_ped_iqr = ped_q1 - 1.5 * ped_iqr
max_ped_iqr = ped_q3 + 1.5 * ped_iqr
min_cyc_iqr = cyc_q1 - 1.5 * cyc_iqr
max_cyc_iqr = cyc_q3 + 1.5 * cyc_iqr

print('---------------Find outliers via IQR method:\n')
find_outliers(pbc['Pedestrians'], 'Pedestrians', min_ped_iqr, max_ped_iqr)
find_outliers(pbc['Cyclists'], 'Cyclists', min_cyc_iqr, max_cyc_iqr)

print('\n---------------Answer of question 01-03---------------\n')
ped_avg = pbc['Pedestrians'].mean()
ped_std = pbc['Pedestrians'].std()
cyc_avg = pbc['Cyclists'].mean()
cyc_std = pbc['Cyclists'].std()

min_ped_schw = ped_avg - 3 * ped_std
max_ped_schw = ped_avg + 3 * ped_std
min_cyc_schw = cyc_avg - 3 * cyc_std
max_cyc_schw = cyc_avg + 3 * cyc_std

print('---------------Find outliers via Schwartz method:\n')
find_outliers(pbc['Pedestrians'], 'Pedestrians', min_ped_schw, max_ped_schw)
find_outliers(pbc['Cyclists'], 'Cyclists', min_cyc_schw, max_cyc_schw)

print('\n---------------Answer of question 01-04---------------\n')
ped_zscore = (pbc['Pedestrians'] - ped_avg) / ped_std
cyc_zscore = (pbc['Cyclists'] - cyc_avg) / cyc_std

print('---------------Find outliers via ZScore method:\n')
find_outliers(abs(ped_zscore), 'Pedestrians', float('0'), float('3'))
find_outliers(abs(cyc_zscore), 'Cyclists', float('0'), float('3'))
