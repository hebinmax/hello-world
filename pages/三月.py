import streamlit as st
import pandas as pd
# 模拟项目数据
project_data = pd.DataFrame(
    {
        "Project Name": ["Project A", "Project B", "Project C"],
        "Status": ["In Progress", "Completed", "Pending"],
        "Progress": [60, 100, 30],  # 进度百分比
        "Sales": [
            [1000, 1500, 500],
            [200, 500, 1500],
            [1800, 500, 1000],
        ],  # 销售额
    }
)

# 定义状态选项列表
statuses = ["In Progress", "Completed", "Pending", "On Hold"]

# 定义列配置
column_config = {
    "Project Name": {"label": "项目名称"},
    "Status": st.column_config.SelectboxColumn(
        "状态",
        options=statuses,
    ),
    "Progress": st.column_config.ProgressColumn(
        "进度",
        min_value=0,
        max_value=100,
        format="%d%%",  # 显示百分比
    ),
    "Sales": st.column_config.BarChartColumn(
        "销售额变化",
        y_min=100,
        y_max=2000,
    ),
}

# 使用st.data_editor展示和编辑项目数据（不包含图表列）
st.title("项目管理系统")
edited_projects = st.data_editor(
    project_data,
    width=500,
    height=300,
    column_config=column_config,
    num_rows="dynamic",
)
