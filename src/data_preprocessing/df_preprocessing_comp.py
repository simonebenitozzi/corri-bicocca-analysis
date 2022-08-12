import pandas as pd
from utils.utils import time_to_minutes

filename = ".\\data\\2019_10km_comp.csv"

results_df = pd.read_csv(filename)

if "minutes" not in results_df.columns:
    minutes_list = []
    for i in range(len(results_df)):
        time = results_df.loc[i]["time"]
        minutes_list.append(time_to_minutes(time))

    results_df["minutes"] = minutes_list
    print(results_df.columns)

    results_df.to_csv(filename, index=False)