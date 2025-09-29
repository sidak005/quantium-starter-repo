import pandas as pd
import glob

files = glob.glob("daily_sales_data_*.csv")
dfs = []

for file in files:
    df = pd.read_csv(file)
    df = df[df["product"] == "pink morsel"]
    df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)
    df["sales"] = df["quantity"] * df["price"]
    df = df[["sales", "date", "region"]]

    dfs.append(df)
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv("processed_sales.csv", index=False)

print("File saved as processed_sales.csv")
