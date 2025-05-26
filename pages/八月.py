import streamlit as st
import pandas as pd
import numpy as np
t1,  t2, t3 =st.tabs(['上传文件','数据集预览','数据分析'])

with t1:
    uploaded_file = st.file_uploader("上传你的CSV或Excel文件", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        # 判断文件类型
        if uploaded_file.name.endswith('.csv'):
            # 读取 CSV 文件
            df = pd.read_csv(uploaded_file, on_bad_lines='skip', encoding='utf-8')
        elif uploaded_file.name.endswith('.xlsx'):
            # 读取 Excel 文件
            df = pd.read_excel(uploaded_file)
        else:
            st.error("不支持的文件格式")
            st.stop()
    if '设备评分' in df.columns:
        # 填充 NaN 为 0 或者删除包含 NaN 的行
        df['设备评分'] = df['设备评分'].replace([np.inf, -np.inf], np.nan)  # 替换无穷值为 NaN
        df['设备评分'] = df['设备评分'].fillna(0)  # 填充 NaN 为 0（也可以用 dropna() 删除空行）
        # 转换为整型
        df['设备评分'] = df['设备评分'].round().astype(int)

    # 展示数据
    st.write("数据集预览：")
    st.write(df)
with t2:
    # 数据概览
    st.write("数据集概览：")
    st.write("行数：", df.shape[0])
    st.write("列数：", df.shape[1])
    st.write("缺失值统计：", df.isnull().sum())

    # 数据分布
    st.write(":blue[数据分布：]")
    x = st.selectbox("选择x轴", df.columns,key='x')
    y = st.selectbox("选择y轴", df.columns,key='y')
    st.bar_chart(df, x=x, y=y)
