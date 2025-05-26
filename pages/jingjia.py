import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# plt.rcParams['font.sans-serif'] = ['SimHei']
# SimHeiplt.rcParams['axes.unicode_minus'] = False
st.set_page_config(layout="wide")
st.title("数据仪表盘示例")
st.write("这是一个简单的数据仪表盘，展示了 Streamlit 的核心组件和布局方式。")
st.sidebar.title("设置")
char_type = st.sidebar.selectbox("选择图表类型", ["折线图", "柱状图"])
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
col1, col2 = st.columns([1,2])
with col1:
    st.write("数据")
    st.dataframe(data)
with  col2:
    st.write("图表")
    if char_type == "折线图":
        st.line_chart(data)
    else:
        st.bar_chart(data)
tab1, tab2, tab3 = st.tabs(["数据", "图表", "设置"])
with tab1:
    st.write("数据")
    px.line(data)
    st.write("图表")
    fig = px.bar(data, x="A", y="B", title="柱状图")
    st.plotly_chart(fig)

