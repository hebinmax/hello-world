import streamlit as st
import pandas as pd
import numpy as np
import time
st.title(":rainbow[欢迎来到二月的数据展示]")
st.write("使用左侧的导航菜单来浏览不同的页面。")
tab1,  tab2 = st.tabs(["数据展示", "数据统计"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with (col1):
        st.write("分数统计")
        df = pd.read_excel("pages/一月分数统计.xlsx")
        st.dataframe(df.head(), 200,100)
        st.write(df)
        st.bar_chart(df)
    with (col2):
        st.write("分数统计")
        df = pd.read_excel("pages/一月分数统计.xlsx")
        st.dataframe(df.head(), 200,100)
        st.write(df)
        st.bar_chart(df)

with tab2:
    x = st.slider('x')
    st.write(x, 'squared is', x * x)


    @st.fragment
    def release_the_balloons():
        st.button("Release the balloons", help="Fragment rerun")
        st.balloons()


    # with st.spinner("Inflating balloons..."):
    #     time.sleep(1)
    # release_the_balloons()
    # st.button("Inflate more balloons", help="Full rerun")

    left, right = st.columns([3, 1])
    with left:
        st.write("主内容区")
    with right:
        st.write("侧边栏")
    top = st.container()
    bottom = st.container()
    with top:
        st.write("先显示这部分内容")
    with bottom:
        st.write("后填充这部分内容")

    # 假设数据集
    data = pd.DataFrame(
        {
            "日期": pd.date_range(start="2023-01-01", periods=100, freq="D"),
            "类别": np.random.choice(["A", "B", "C"], 100),
            "销售额": np.random.randint(100, 1000, 100),
            "利润": np.random.randint(10, 100, 100),
        }
    )

    # 标题
    st.title("数据分析项目仪表板")

    # 文本输入框：输入项目名称
    project_name = st.text_input("请输入项目名称：")

    # 下拉单选框：选择分析类别
    analysis_category = st.selectbox("请选择分析类别：", data["类别"].unique())

    # 下拉多选框：选择显示的列
    display_columns = st.multiselect("请选择要显示的列：", data.columns)
    selected_data = data[display_columns]

    # 单选按钮组：选择汇总方式
    agg = st.radio("请选择汇总方式：", ["总和", "平均值", "最大值", "最小值"])
    agg_dict = {
        "总和": "sum",
        "平均值": "mean",
        "最大值": "max",
        "最小值": "min",
    }

    # 复选框：是否按类别汇总
    group_by_category = st.checkbox("是否按类别汇总？")

    # 按钮：执行分析
    if st.button("执行分析"):
        # 根据用户选择进行分析
        if group_by_category:
            grouped_data = (
                selected_data.groupby("类别")
                .agg({col: agg_dict[agg] for col in selected_data.columns if col != "类别"})
                .reset_index()
            )
        else:
            grouped_data = (
                selected_data.agg({col: agg_dict[agg] for col in selected_data.columns})
                .to_frame()
                .T
            )

        # 显示分析结果
        st.subheader("分析结果：")
        st.dataframe(grouped_data)


