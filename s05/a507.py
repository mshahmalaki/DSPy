import pandas as pd

excel = pd.ExcelFile(r'./customerfeedback.xlsx')
customer_sheet = pd.read_excel(excel, sheet_name='Customer Table')
role_sheet = pd.read_excel(excel, sheet_name='Role')
clean_customer_sheet = customer_sheet.dropna(how='any', subset=['Customer ID'])
new = clean_customer_sheet.merge(role_sheet, how='left', left_on='Role', right_on='Role ID')
filtered_customer_sheet = new[(new['Original Score'] == 10) & (new['Role in Org'] == 'administrator')]
print(filtered_customer_sheet['Customer ID'].count())
