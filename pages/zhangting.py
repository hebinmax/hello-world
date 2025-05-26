import streamlit as st

st.header("这是页面 2")

if st.button("GoTo Page 1"):
    st.switch_page("home.py")

if "dataset" not in st.session_state or st.session_state.dataset == "":
    st.write("当前尚未选择数据集")
else:
    st.write("开始分析数据集: 【", st.session_state.dataset, "】")
