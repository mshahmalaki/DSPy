import pandas as pd

excel = pd.ExcelFile(r'./customerfeedback.xlsx')
customer_sheet = pd.read_excel(excel, sheet_name='Customer Table')
geography_sheet = pd.read_excel(excel, sheet_name='Geography')

# Left join
new_customer_sheet_01 = customer_sheet.merge(geography_sheet, how='left',
                                             left_on='Geography ID',
                                             right_on='Geography ID')
print(new_customer_sheet_01.head(10))

# Fuzzy matching
new_customer_sheet_02 = customer_sheet['Geography ID'].replace(
    geography_sheet.set_index('Geography ID').Continent.to_dict())
print(new_customer_sheet_02.head(10))
