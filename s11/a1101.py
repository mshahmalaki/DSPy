import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


housing = pd.read_csv(r'housing.csv')
housing.dropna(inplace=True)
# print(housing.count())

# Normalization
# MinMax method
scaler1 = MinMaxScaler()
minmax_method = pd.DataFrame.copy(housing)
minmax_method.iloc[:, :-1] = scaler1.fit_transform(housing.iloc[:, :-1])
print(minmax_method.iloc[:, :-1].head)
# sns.distplot(minmax_method.iloc[:, :-1])


# Normalization
# ZScore method
scaler2 = StandardScaler()
zscore_method = pd.DataFrame.copy(housing)
zscore_method.iloc[:, :-1] = scaler2.fit_transform((housing.iloc[:, :-1]))
print(zscore_method.iloc[:, :-1].head)
sns.distplot(zscore_method.iloc[:, :-1])
plt.show()
