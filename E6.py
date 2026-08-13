import pandas as pd

df = pd.read_excel("MOSFET_ID_VDS.xlsx")

print(df.columns)
print(df.shape)
print(df.describe())