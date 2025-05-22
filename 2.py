import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from datetime import time, datetime
st.title(':red[Hello], :blue[World]!')
st.header('st.slider')
st.subheader('slider')
age = st.slider('How old are you?', 0, 130, 25)


