import pandas as pd


excel = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Support Tickets')
tickets_sheet = pd.DataFrame(excel)
new_tickets_sheet = tickets_sheet.dropna(how='any', subset=['Support Ticket ID'])
tickets_count = new_tickets_sheet['Support Ticket ID'].count()

print('Number of support tickets :', tickets_count)
