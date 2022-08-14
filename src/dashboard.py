import streamlit as st

import re

import pandas as pd
import plotly.express as px

import utils.utils as utils

st.set_page_config(page_title="CorriBicocca Analysis", page_icon=".\\img\\corri_bicocca.jpg", layout="wide")
template = "plotly_dark"

@st.cache(allow_output_mutation=True)
def load_data(filename):
    return pd.read_csv(filename, index_col="position")

with st.sidebar:
    st.image(".\\img\\corri_bicocca_banner.png", caption=None, width=None, use_column_width="always")
    st.write("---")

    distance_str = st.radio("Distance:", ["10km", "5km"], horizontal=True)
    if distance_str=="10km":
        mode = st.radio("Mode:", ["non competitive", "competitive"], horizontal=True)
    else:
        mode = st.radio("Mode:", ["non competitive"], horizontal=True)
    year = st.selectbox("Edition:", [2021, 2019])

    your_time = st.text_input('Your Time', '0:00:00')
    try:
        your_minutes = utils.time_to_minutes(your_time)
    except:
        st.text("Invalid Format (use h:mm:ss)")
        your_minutes = 0

distance = int(re.search(r'\d+', distance_str).group())
mode = "comp" if mode=="competitive" else "noncomp"

data_dir = ".\\data\\"
df = load_data(data_dir+str(year)+"_"+distance_str+"_"+mode+".csv")
filter_df = df.copy()

participants = len(df)
min_minutes = min(df["minutes"])
max_minutes = max(df["minutes"])

if mode == "noncomp":
    filters = ["all", "teams", "individuals"]
else :
    filters = ["all", "teams"]

filter = st.radio("Filter by:", filters, horizontal=True)
filter_df = utils.filter_df(df.copy(), filter)
filter_df["individual"] = filter_df["individual"].astype(str)

avg_minutes = round(sum(filter_df["minutes"]) / len(filter_df), 2)
avg_time = utils.minutes_to_time(avg_minutes)

best_minutes = min(filter_df["minutes"])
best_time = utils.minutes_to_time(best_minutes)

worst_minutes = max(filter_df["minutes"])
worst_time = utils.minutes_to_time(worst_minutes)

col1, col2 = st.columns([3,1])
with col1:
    color_discrete_map = {'0': '#FFFF00', '1': '#FF0000'}
    fig = px.scatter(filter_df, "minutes", template=template, color="individual", color_discrete_map=color_discrete_map,
                        title="<b>Results Chart", custom_data=[filter_df["time"], filter_df["team"]])
    fig.update_layout(yaxis={"range":[-50,participants+50]}, xaxis={"dtick":15, "range":[min_minutes-10,max_minutes+10]}, 
                        showlegend=False, hovermode="x unified")
    fig.update_traces(hovertemplate="<br>".join([
                            "time: %{customdata[0]}",
                            "position: %{y}",
                            "team: %{customdata[1]}"]))

    fig.add_vline(x=avg_minutes, line_width=0.5, line_dash="dash", line_color="white", annotation_text=f"{avg_time}")
    fig.add_vline(x=best_minutes, line_width=0.5, line_dash="dash", line_color="white", annotation_text=f"{best_time}")
    fig.add_vline(x=worst_minutes, line_width=0.5, line_dash="dash", line_color="white", annotation_text=f"{worst_time}")
    if your_minutes > 0:
        fig.add_vline(x=your_minutes, line_width=3, line_dash="dash", line_color="green")

    st.plotly_chart(fig, use_container_width=True)

with col2:
    summary_df = pd.DataFrame(columns=[" ","  "])
    if your_minutes>0:
        summary_df.loc[len(summary_df)] = ["Your Time:", f"{your_time}"]
        your_position = len(filter_df[filter_df["minutes"]<your_minutes])
        summary_df.loc[len(summary_df)] = ["Expected Position:", f"{your_position}"]
    summary_df.loc[len(summary_df)] = ["Participants:", str(len(filter_df))]
    
    individuals_count = len(filter_df[filter_df["individual"]=="1"])
    individuals_ratio = round(individuals_count / len(filter_df) * 100,1)
    summary_df.loc[len(summary_df)] = ["Individuals:", f"{individuals_count} ({individuals_ratio}%)"]
    
    competitives_count = len(filter_df) - individuals_count
    competitives_ratio = round(100-individuals_ratio, 1)
    summary_df.loc[len(summary_df)] = ["Competitives:", f"{competitives_count} ({competitives_ratio}%)"]

    summary_df.set_index(' ', inplace=True)
    st.dataframe(summary_df)

st.write("---")