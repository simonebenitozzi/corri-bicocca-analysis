import pandas as pd
import datetime

results_df = pd.read_csv("CorriBicoccaResults.csv")

seconds_list = []

for i in range(len(results_df)):
    pt = datetime.strptime(results_df.loc[i]["time"],'%H:%M:%S')
    total_seconds = pt.second + pt.minute*60 + pt.hour*3600
    seconds_list.append(total_seconds)

results_df["seconds"] = seconds_list
results_df["minutes"] = round(results_df["seconds"]/60, 2)

results_df.sort_values("seconds", inplace=True)
results_df = results_df.reset_index(drop=True)
results_df.drop(results_df.columns[0], axis=1, inplace=True)

results_df.to_csv("CorriBicoccaResults.csv", index=False)

print(len(results_df))
results_df.head()