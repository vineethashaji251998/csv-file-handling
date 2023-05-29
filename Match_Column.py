import pandas as pd

df1 = pd.read_csv('data.csv')

df2 = pd.read_csv('reference.csv')

merged_df = pd.merge(df1, df2, on='common_column')

print(merged_df)
