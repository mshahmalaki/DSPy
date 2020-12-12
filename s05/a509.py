import pandas as pd

excel = pd.ExcelFile(r'./customerfeedback.xlsx')
customer = pd.read_excel(excel, sheet_name='Customer Table')
device = pd.read_excel(excel, sheet_name='Device')

# clean customer
new_customer = customer.dropna(how='any', subset=['Customer ID'])
customer_count = new_customer['Customer ID'].count()
tablet_count = device[device['device'] == 'tablet']['ID'].count()
tablet_percent = tablet_count / customer_count
print('Percentage of customer have tablet :', '{:.2%}'.format(tablet_percent))
