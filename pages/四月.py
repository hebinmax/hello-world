from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import streamlit as st
import numpy as np

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

code = '''def hello():
  print("Hello, Streamlit!")'''
st.code(code, language='python')
st.latex(r'''
  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
  \sum_{k=0}^{n-1} ar^k =
  a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.json({
    'foo': 'bar',
    'stuff': [
        'stuff 1',
        'stuff 2',
    ],
})

