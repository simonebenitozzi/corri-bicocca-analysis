import pandas as pd
from datetime import datetime

def time_to_minutes(time):
    pt = datetime.strptime(time,'%H:%M:%S')
    minutes = round(pt.second/60,2) + pt.minute + pt.hour*60    
    return minutes

def edit_lines(file_lines, min_cols):
    
    for i in range(len(file_lines)):
        line = file_lines[i]
        line_parts = line.split(" ")
        
        time_index = -2 if min_cols==3 else -1
        time = line_parts[time_index].rstrip()
        
        if len(line_parts) > min_cols:
            team = line_parts[0:time_index-1]
            team = ' '.join(team)
        else:
            team = "INDIVIDUALE"
        
        file_lines[i] = team + "," + str(time_to_minutes(time)) + "\n"

    return file_lines

# TODO: use os.path

source = ".\\data\\raw_data\\2019_10km_noncomp"
target = ".\\data\\2019_10km_noncomp.csv"
file = open(source, "r")
file_lines = file.readlines()

if "2021" in source:
    min_cols = 3
else:
    min_cols = 2

new_lines = edit_lines(file_lines,min_cols)

file = open(target, "w")
file.writelines(new_lines)
file.close()

# results_df = pd.read_csv(filename)

# for each line:
    # read and split by " "
    # use negative indexes for: (average if 2021), time, nation, (team: [0:-3 or -4])
    # store all in variables
    # rewrite with commas (ignore nation)


# results_df["minutes"] = minutes_list

# results_df.sort_values("seconds", inplace=True)
# results_df = results_df.reset_index(drop=True)
# results_df.drop(results_df.columns[0], axis=1, inplace=True)

# results_df.to_csv("CorriBicoccaResults.csv", index=False)

# print(len(results_df))
# results_df.head()


