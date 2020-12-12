import numpy as np
import pandas as pd


excel = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Customer Table')
df = pd.DataFrame(excel)

new_customer_id = df.dropna(how='any', subset=['Customer ID'])

print(new_customer_id.head(10))
