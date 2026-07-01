import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\AI-Data-Analytics-Assistant\Data\Sample - Superstore.csv", encoding="cp1252")
print(df.head())

# basic cleaning
df=df.drop_duplicates()

#save for Power BI
df.to_csv("clean_superstore.csv", index=False)
print("clean.file ready for Power BI")

print("TOTAL ROWS:",df.shape[0])
print("TOTAL COLUMNS:",df.shape[1])

print("\nTOTAL SALES:",df["Sales"].sum())
print("TOTAL PROFIT:",df["Profit"].sum())

print("\nTOP 5 MOST PROFITABLE ORDERS:")
print(df.sort_values("Profit",ascending=False).head())

## BUSINESS INSIGHTS

print("\nREGION WISE SALES:")
print(df.groupby("Region")["Sales"].sum())

print("\nCATEGORY WISE PROFIT:")
print(df.groupby("Category")["Profit"].sum())

## CHECK CLEAN DATASET

print("\nMISSING VLUES:")
print(df.isnull().sum())
