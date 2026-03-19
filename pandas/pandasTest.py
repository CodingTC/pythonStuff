import pandas as pd

df = pd.read_csv("orders.csv")

data = [100, 200, 300, 400, 500]

series = pd.Series(data)

print(series[2])
print(series.iloc[2])
print(series.loc[2])

