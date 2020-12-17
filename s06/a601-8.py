import pandas as pd


pbc = pd.read_csv(r'./pedestrian-and-bicyclist-counts.csv')
pbc['People'] = pbc['Pedestrians'] + pbc['Cyclists']
print('---------------Answer of question 01---------------')
print(pbc.head())
