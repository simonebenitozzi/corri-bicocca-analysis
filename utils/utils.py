from datetime import datetime

def time_to_minutes(time):
    pt = datetime.strptime(time,'%H:%M:%S')
    minutes = round(pt.second/60,2) + pt.minute + pt.hour*60    
    return minutes