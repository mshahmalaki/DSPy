import pandas as pd


company_sheet = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Company')
new_company_sheet = company_sheet
new_company_sheet['Company Type'] = pd.Series(['Small', 'Medium', 'Large'])
print(new_company_sheet)
