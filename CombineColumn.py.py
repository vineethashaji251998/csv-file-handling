import pandas as pd

# Create a sample DataFrame with multiple columns
data = pd.read_csv('SeqPDB.csv')
df=pd.DataFrame(data) 

# Combine all columns into a single column
df_combined = df.stack().reset_index(drop=True)

# Rename the combined column
df_combined.columns = ['Combined Column']

# Display the combined DataFrame
print(df_combined)
df_combined.to_csv("outputfilemerge.csv", index=False)