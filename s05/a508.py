import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

excel = pd.ExcelFile(r'./customerfeedback.xlsx')
customer_sheet = pd.read_excel(excel, sheet_name='Customer Table')
geography_sheet = pd.read_excel(excel, sheet_name='Geography')
# Clean customer table on Original Score Column
new_customer_sheet = customer_sheet.dropna(how='any', subset=['Original Score'])
# Left join
merged_sheet = new_customer_sheet.merge(geography_sheet, how='left',
                                        left_on='Geography ID',
                                        right_on='Geography ID')

new_df = merged_sheet[['Continent', 'Original Score']]
new_df.groupby('Continent')['Original Score'].agg(np.average).plot(kind='bar')
plt.show()
