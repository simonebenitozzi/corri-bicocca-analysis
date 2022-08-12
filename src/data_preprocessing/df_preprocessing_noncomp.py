import pandas as pd

filename = ".\\data\\2019_5km_noncomp.csv"

results_df = pd.read_csv(filename)
print(results_df.columns)

if "position" not in results_df.columns:
    results_df.sort_values("minutes", inplace=True)
    results_df.reset_index(drop=True, inplace=True)
    results_df.insert(0, 'position', results_df.index + 1)

    results_df.to_csv(filename, index=False)