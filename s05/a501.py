import numpy as np
import pandas as pd


excel = pd.read_excel(r'./customerfeedback.xlsx', sheet_name='Customer Table')
df = pd.DataFrame(excel)

sum_original_score = df['Original Score'].sum()
count_original_score = df['Original Score'].count()
avg_original_score = sum_original_score / count_original_score

new_df = df['Original Score'].replace(np.nan, avg_original_score)
print(new_df.head())
