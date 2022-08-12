def edit_lines(file_lines, min_cols):
    
    for i in range(len(file_lines)):
        line = file_lines[i]
        line_parts = line.split(" ")
        
        time_index = -2 if min_cols==3 else -1
        time = line_parts[time_index].rstrip()
        nation = line_parts[time_index-1]

        if len(line_parts) > min_cols:
            team = line_parts[0:time_index-1]
            team = ' '.join(team)
        else:
            team = "INDIVIDUALE"
        
        file_lines[i] = team + "," + nation + "," + time + "," + str(time_to_minutes(time)) + "\n"

    return ["team,nation,time,minutes\n"]+file_lines

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


