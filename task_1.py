import pandas as pd


file_path = 'Task 1.xlsx'

df1 = pd.read_excel(file_path, sheet_name='DF_1')
df2 = pd.read_excel(file_path, sheet_name='DF_2')

df1.columns = ['CIF', 'LD', 'Lsize', 'Date']
df2.columns = ['CIF', 'LD', 'Loan size', 'Date']

df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

merged_df = pd.merge(df1, df2, on='CIF', suffixes=('_df1', '_df2'))

filtered_df = merged_df[merged_df['Date_df2'] < merged_df['Date_df1']]

sum_loans = filtered_df.groupby(['CIF', 'LD_df1'])['Loan size'].sum().reset_index()

result = pd.merge(df1, sum_loans, left_on=['CIF', 'LD'], right_on=['CIF', 'LD_df1'], how='left')
result = result[['CIF', 'LD', 'Loan size']]

result.columns = ['CIF', 'LD', 'Sum of previous loans']

result['Sum of previous loans'] = result['Sum of previous loans'].fillna(0)


print(result)

result.to_excel('Result_1.xlsx', index=False)
