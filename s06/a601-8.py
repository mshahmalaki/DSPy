import pandas as pd


pbc = pd.read_csv(r'./pedestrian-and-bicyclist-counts.csv')
print('---------------Answer of question 01---------------')
pbc01 = pbc.copy()
pbc01['People'] = pbc01['Pedestrians'] + pbc01['Cyclists']
print(pbc.head())
print('---------------Answer of question 02---------------')
pbc02 = pbc.copy()
pbc02 = pbc02[(pbc02['Cyclists'] > pbc02['Pedestrians'])]
count_days = pbc02['Date'].count()
print('The number of days that has more cyclists than pedestrians :', count_days, 'day(s)')
print('---------------Answer of question 03---------------')
pbc03 = pbc.copy()
print('Average number of cyclists and pedestrians observed per day:')
print(pbc03.mean())
