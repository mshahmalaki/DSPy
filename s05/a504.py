import pandas as pd
import numpy as np

excel = pd.ExcelFile(r'./customerfeedback.xlsx')
customer_sheet = pd.read_excel(excel, sheet_name='Customer Table')
geography_sheet = pd.read_excel(excel, sheet_name='Geography')

# Left join
new_customer_sheet = customer_sheet.merge(geography_sheet, how='left',
                                          left_on='Geography ID',
                                          right_on='Geography ID')

pvt = new_customer_sheet.pivot_table(
    index='Country-Region',
    columns='Completed tutorial',
    values='Customer ID',
    aggfunc=np.count_nonzero
)
print(pvt)
