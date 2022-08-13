from datetime import datetime

def time_to_minutes(time):
    try:
        pt = datetime.strptime(time,'%H:%M:%S')
    except:
        pt = datetime.strptime(time,'%M:%S')
    minutes = round(pt.second/60,2) + pt.minute + pt.hour*60    
    return minutes

def minutes_to_time(minutes):
    time = ""

    hours = int(minutes/60)
    if hours > 0:
        time += str(hours) + ":"
    minutes = minutes%60
    time += str("%02d" % (minutes,)) +":"
    seconds = (minutes%1)*60
    time += str("%02d" % (seconds,))

    return time

def filter_df(df, filter):
    if filter == "all":
        return df
    if filter == "teams":
        return df[df["individual"] == 0]
    if filter == "individuals":
        return df[df["individual"] == 1]
    return df