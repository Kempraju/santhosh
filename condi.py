import pandas as pd

# Assuming you have a DataFrame named "df" with a column named "ship_mode" and "sales_profit"

def calculate_surcharge(row):
    if row["ship_mode"] == "Same Day":
        return 0.2
    elif row["ship_mode"] == "First Class":
        return 0.1
    elif row["ship_mode"] == "Standard Class":
        return 0.05
    else:
        return 0

df["surcharge"] = df.apply(calculate_surcharge, axis=1)
df["total_cost"] = df["sales_profit"] * (1 + df["surcharge"])