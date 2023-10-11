import streamlit as st
import time

st.header('*Chat elements*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
st.divider()
with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)
st.button('Rerun')
