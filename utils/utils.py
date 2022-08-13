from datetime import datetime

def time_to_minutes(time):
    pt = datetime.strptime(time,'%H:%M:%S')
    minutes = round(pt.second/60,2) + pt.minute + pt.hour*60    
    return minutes

def filter_df(df, filter):
    if filter == "all":
        return df
    if filter == "teams":
        return df[df["team"] != "INDIVIDUALE"]
    if filter == "individuals":
        return df[df["team"] == "INDIVIDUALE"]
    return df