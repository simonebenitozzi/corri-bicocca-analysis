import streamlit as st

import re

import pandas as pd
import plotly.express as px

import utils.utils as utils

st.set_page_config(page_title="CorriBicocca Analysis", page_icon=".\\img\\corri_bicocca.jpg", layout="wide")
template = "plotly_dark"

with st.sidebar:
    distance_str = st.radio("Distance:", ["10km", "5km"], horizontal=True)
    if distance_str=="10km":
        mode = st.radio("Mode:", ["non competitive", "competitive"], horizontal=True)
    else:
        mode = st.radio("Mode:", ["non competitive"], horizontal=True)
    year = st.selectbox("Edition:", [2021, 2019])

distance = int(re.search(r'\d+', distance_str).group())
mode = "comp" if mode=="competitive" else "noncomp"

data_dir = ".\\data\\"
df = pd.read_csv(data_dir+str(year)+"_"+distance_str+"_"+mode+".csv", index_col="position")
participants = len(df)
min_minutes = min(df["minutes"])
max_minutes = max(df["minutes"])
# st.dataframe(df)

col1, col2 = st.columns(2)
# with col1:
filter = st.radio("Filter by:", ["all", "teams", "individuals"], horizontal=True)
filter_df = utils.filter_df(df, filter)

fig = px.scatter(filter_df, "minutes", template=template)
fig.update_layout(yaxis={"range":[-50,participants+50]}, xaxis={"range":[min_minutes-10,max_minutes+10]})
# st.write(fig)
st.plotly_chart(fig, use_container_width=True)

# with col2:
