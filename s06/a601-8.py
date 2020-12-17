import pandas as pd


pbc = pd.read_csv(r'./pedestrian-and-bicyclist-counts.csv')
pbc['People'] = pbc['Pedestrians'] + pbc['Cyclists']
print('---------------Answer of question 01---------------')
print(pbc.head())
print('---------------Answer of question 02---------------')
pbc02 = pbc.copy()
pbc02 = pbc02[(pbc02['Cyclists'] > pbc02['Pedestrians'])]
count_days = pbc02['Date'].count()
print('The number of days that has more cyclists than pedestrians :', count_days, 'day(s)')
