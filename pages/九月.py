import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 数据分析中心")

# 上传数据
with st.expander("数据上传", expanded=True):
    uploaded_file = st.file_uploader("选择CSV文件", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    else:
        data = None

# 双列布局
    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("数据预览")
        if data:
            st.dataframe(data.head(10))
        else:
            st.write("请上传CSV文件")

    with col2:
        st.subheader("可视化分析")
        chart_type = st.selectbox("图表类型", ["散点图", "柱状图", "折线图"])
        x_axis = st.selectbox("X轴字段", data.columns)
        y_axis = st.selectbox("Y轴字段", data.columns)

    if chart_type == "散点图":
        fig = px.scatter(data, x=x_axis, y=y_axis)
    elif chart_type == "柱状图":
        fig = px.bar(data, x=x_axis, y=y_axis)
    elif chart_type == "折线图":
        fig = px.line(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig, use_container_width=True)