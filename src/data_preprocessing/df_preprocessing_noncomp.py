import pandas as pd

filename = ".\\data\\2021_10km_noncomp.csv"

results_df = pd.read_csv(filename)
print(results_df.columns)

results_df.sort_values("minutes", inplace=True)
results_df["position"] += 1

results_df.to_csv(filename, index=False)