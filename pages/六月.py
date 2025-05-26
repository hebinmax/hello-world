import streamlit as st
import pandas as pd
import numpy as np
# 绘图的类型放在session中
if "graph" not in st.session_state:
    st.session_state.graph = ""

# 第一列
def column_1():
    st.header("1. 选择数据")
    st.selectbox(
        "选择数据集?",
        (
            "手写数字数据",
            "房屋成交数据",
            "股市交易数据",
        ),
    )
    # 随机模拟的数据
    data = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
    st.table(data)


def column_2():
    st.header("2. 配置数据")
    graph = st.radio(
        "图形类型: ",
        ("折线图", "柱状图", "散点图"),
    )

    st.session_state.graph = graph


def column_3():
    st.header("3. 绘制图形")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    if st.session_state.graph == "散点图":
        st.scatter_chart(chart_data)

    if st.session_state.graph == "折线图":
        st.line_chart(chart_data)

    if st.session_state.graph == "柱状图":
        st.bar_chart(chart_data)

col1, col2, col3 = st.tabs(["1. 选择数据", "2. 配置数据", "3. 绘制图形"])

with col1:
    column_1()

with col2:
    c1, c2 =st.columns(2)
    with c1:
        column_2()
    with c2:
        column_3()

with col3:
    column_3()
