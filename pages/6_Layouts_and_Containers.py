import streamlit as st
import time

st.header('*Layouts and Containers*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
