import streamlit as st
import pandas as pd

st.title("欢迎来到二月的数据展示")
st.write("使用左侧的导航菜单来浏览不同的页面。")
st.tabs(["数据展示", "数据统计"])
col1, col2, col3 = st.columns(3)
with (col1):
    st.write("分数统计")
    df = pd.read_excel("pages/一月分数统计.xlsx")
    st.dataframe(df.head(), 200,100)
    st.write(df)
    st.write(st.bar_chart(df))
