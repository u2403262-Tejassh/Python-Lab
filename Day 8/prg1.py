import pandas as pd

df = pd.read_csv("sales_data.csv")
print("Data Cleaning:")
df["Price"].fillna(df["Price"].median(), inplace=True)
df["Quantity"].fillna(df["Quantity"].median(), inplace=True)
print(df.isnull().sum())
print("Sales Analysis:")
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print(df.groupby("Region").sum())
print(df.groupby("Category").sum().sort_values("Total_Sales",ascending=False))
print("Time-Series Analysis:")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df.groupby(df["OrderDate"].dt.month).sum())
df.to_csv("updated_sales.csv", index=False)
