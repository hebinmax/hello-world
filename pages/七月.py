import streamlit as st
import pandas as pd

dataset = st.sidebar.selectbox(
    "选择数据集?",
    (
        "手写数字数据",
        "房屋成交数据",
        "股市交易数据",
    ),
)

# 侧边栏中选择数据分类
data_type = st.sidebar.radio(
    "数据分类: ",
    ("测试集", "验证集", "所有数据"),
)

# 右侧页面中的模拟操作
st.title(f"数据集： {dataset}")
st.divider()
st.write(f"数据分类： 【{data_type}】")
if data_type == '测试集':
    st.write(f"TODO！！！: 操作数据的功能")

