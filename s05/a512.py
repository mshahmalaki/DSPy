import pandas as pd


customer_sheet = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Customer Table')
# clean Customer Table sheet
new_customer_sheet = customer_sheet.dropna(how='any', subset=['Customer ID', 'Original Score'])
# Write new customer sheet to excel file
new_customer_sheet.to_excel('Customer.xlsx', sheet_name='Customer Table')
