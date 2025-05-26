import streamlit as st
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


st.title(":rainbow[欢迎来到一月的数据展示]")
st.write("使用左侧的导航菜单来浏览不同的页面。")
b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

st.divider()
if st.button("GoTo Page 2"):
    st.switch_page("pages/二月.py")
t1, t2 = st.tabs(["数据展示", "柱状图"])
with t1:
    df = pd.read_excel("pages/一月分数统计.xlsx")
    st.dataframe(df)
with t2:
    st.write(st.bar_chart(df.T))