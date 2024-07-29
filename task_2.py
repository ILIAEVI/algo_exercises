import pandas as pd

file_path = 'Task 2.xlsx'

df1 = pd.read_excel(file_path, sheet_name='DF1')
df2 = pd.read_excel(file_path, sheet_name='DF2')

income_summary = df1.groupby(['CIF', 'Income_type'])['Income'].sum().reset_index()
income_summary = income_summary.sort_values(['CIF', 'Income'], ascending=[True, False])

largest_income_type = income_summary.drop_duplicates('CIF').set_index('CIF')
largest_income_type = largest_income_type.rename(columns={'Income': 'Largest_Income', 'Income_type': 'Largest_Income_Type'})

total_income = df1.groupby('CIF')['Income'].sum().rename('Total_Income')

result = df2.drop_duplicates('CIF').set_index('CIF').join(largest_income_type[['Largest_Income_Type', 'Largest_Income']]).join(total_income)

result = result.reset_index()

result = result[['CIF', 'Total_Income', 'Largest_Income_Type', 'RisckGrade', 'married']]

print(result)

result.to_excel('Result_2.xlsx', index=False)
