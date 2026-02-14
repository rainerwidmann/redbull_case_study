#%%
import pandas as pd

#%%
#Load data

file_path = "../data/Red Bull Case Study Data.xlsx"

df = pd.read_excel(file_path, engine="openpyxl")
#%%
# Quick check
print(df.head())

print("hello world")