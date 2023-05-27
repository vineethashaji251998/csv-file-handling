import csv
import pandas as pd

data = pd.read_csv('Split.csv')
df=pd.DataFrame(data)   
df["Compound"] = df["Compound"].apply(lambda x: str(x).strip(';'))
df["Compound"] = df["Compound"].str.split(";") 
df = df.explode("Compound").agg(pd.Series.tolist) 
df.to_csv("output_File.csv", index=False)
