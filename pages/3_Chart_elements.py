import streamlit as st
import pandas as pd
import numpy as np

st.header('*Chart elements*', divider= 'rainbow')
st.subheader('可能以後放準確率? 不曉得')
st.caption('_好累喔_')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
