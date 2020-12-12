import pandas as pd


subscription = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Subscription')
print(subscription)
new_subscription = subscription.drop('Subscription New', axis=1)
print(new_subscription)
