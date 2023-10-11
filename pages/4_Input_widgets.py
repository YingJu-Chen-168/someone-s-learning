import streamlit as st

st.header('*Input widgets*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
st.divider()
st.link_button("Go to gallery", "https://streamlit.io/gallery")
st.divider()
agree = st.checkbox('嫁給我吧')
if agree:
    st.write('❣️')
st.divider()
on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')
st.divider()
genre = st.radio(
    "我跟?你要選誰?",
    [":rainbow[我]", "?"],
    captions = ["怎麼看都要選我", "選他不好吧"],
    index=None)
if genre == ':rainbow[我]':
    st.write('你真聰明')
else:
    st.write("你笨")
