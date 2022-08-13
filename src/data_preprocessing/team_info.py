import pandas as pd

filename = ".\\data\\2019_5km_noncomp.csv"
df = pd.read_csv(filename)
df["individual"] = [1 if team == "INDIVIDUALE" else 0 for team in df["team"]]
df.to_csv(filename, index=False)