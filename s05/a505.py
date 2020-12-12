import pandas as pd

excel = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Customer Table')
customer_sheet = pd.DataFrame(excel)

new_customer_sheet = customer_sheet.replace({'Completed tutorial': {'no': 0, 'yes': 1}})

print(new_customer_sheet.head(10))
