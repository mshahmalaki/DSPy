import pandas as pd


housing = pd.read_csv(r'housing.csv')
housing.dropna(inplace=True)
print(housing.count())

