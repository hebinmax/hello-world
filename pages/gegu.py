import streamlit as st
import pandas as pd
import plotly.express as px
# 三级嵌套布局示例
main = st.container()
with main:
    header = st.container()
    body = st.columns([1, 2])

with header:
        st.title("响应式布局演示")
data = pd.read_csv("1w.csv")
with body[0]:
    with st.container(height=900):
        st.write("侧边控制面板")

with body[1]:
    tab1, tab2 = st.tabs(["图表", "数据"])
    with tab1:
        chart_type = st.selectbox("选择图表类型", ["散点图","折线图", "柱状图"])
        x_axis = st.selectbox("X轴字段", data.columns)
        y_axis = st.selectbox("Y轴字段", data.columns)
        if chart_type == "散点图":
            fig = px.scatter(data, x=x_axis, y=y_axis)
        elif chart_type == "柱状图":
            fig = px.bar(data, x=x_axis, y=y_axis)
        elif chart_type == "折线图":
            fig = px.line(data, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.dataframe(data)