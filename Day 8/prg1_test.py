import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Data Cleaning:\n")
df["Price"].fillna(df["Price"].median(), inplace=True)
df["Quantity"].fillna(df["Quantity"].median(), inplace=True)
print(df.isnull().sum())

print("\n\nSales Analysis:\n")
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print(df.groupby("Region").sum())
print(df.groupby("Category").sum().sort_values("Total_Sales",ascending=False))
print("\n\nTime-Series Analysis:\n")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df.groupby(df["OrderDate"].dt.month).sum())

df.to_csv("updated_sales.csv", index=False)

print("\n\nData Visualization:\n")
region_sales = df.groupby("Region")["Total_Sales"].sum()
plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
df["Month"] = df["OrderDate"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
