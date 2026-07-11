# Loaded data into Pandas df, variance calculation and materiality flag

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\User\Documents\Python Projects\Variance Analysis\Data\budget_vs_actual_2025.csv")


# Variance by monetary value

df["pound_variance"] = df["Actual"] - df["Budget"]

# Variance by %

df["percentage_variance"] = (((df["Actual"] - df["Budget"]) / df["Budget"]) * 100).round(2)

# Split revenues from costs

df["is_revenues"] = df["Line_Item"] == "Revenue"


# Converted signs for simplicity
df["signed_variance"] = np.where(df["is_revenues"], df["pound_variance"], -df["pound_variance"])

df["signed_pct_variance"] = np.where(df["is_revenues"], df["percentage_variance"], -df["percentage_variance"])

df["variance_type"] = np.where(df["signed_variance"] > 0, "favourable", "Unfavourable" )



df = df.drop(columns = ["is_revenues"])

print(f"Full data set with calculations")
print(df)

# Manually set boundaries: either greater than abs(10%) or greater than abs(£5,000)

material =  (df["signed_pct_variance"].abs() > 10) | (df["signed_variance"].abs() > 5000)
material_df = df[material]
print(f"\nMaterial variances")
print(material_df)


