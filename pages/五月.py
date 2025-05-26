import streamlit as st
import pymysql
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from streamlit_echarts import st_pyecharts
from pyecharts.options import TitleOpts

st.title(':rainbow[电影分析]')
t1, t2 = st.tabs(["电影数据", "电影数据分析"])

# 数据库连接
db_config = st.secrets.connections.mysql
conn = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)

with conn.cursor() as cur:
    cur.execute("SELECT * FROM movies;")
    result = cur.fetchall()

df_news = pd.DataFrame(result)
df_news['rating'] = pd.to_numeric(df_news['rating'], errors='coerce')
# 按评分升序排序
df_news = df_news.sort_values(by='rating', ascending=True)

with t1:
    st.dataframe(df_news)

with t2:
    # Streamlit 内置柱状图
    st.bar_chart(df_news, x='title', y='rating')
    st.line_chart(df_news, x='title', y='rating', use_container_width=True)
