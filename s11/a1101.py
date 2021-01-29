import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt


housing = pd.read_csv(r'housing.csv')
housing.dropna(inplace=True)
# print(housing.count())

# Normaliztion
# MinMax method
scaler1 = MinMaxScaler()
minmax_method = pd.DataFrame(scaler1.fit_transform(housing.iloc[:, :-1]))
print(minmax_method.head())

sns.distplot(minmax_method.iloc[:, :-1])
plt.show()
