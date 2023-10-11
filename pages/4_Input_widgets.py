import streamlit as st

st.header('*Input widgets*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
st.button("Reset", type="primary")
if st.button('跟我說早安'):
    st.write('現在不是早上幹嘛說早安')
else:
    st.write('想你了')
st.divider()
st.link_button("按這裡去色色網站", "https://researchoutput.ncku.edu.tw/zh/persons/jiunn-der-liao")
st.caption("_好玩_")
st.divider()
agree = st.checkbox('嫁給我吧')
if agree:
    st.write('❣️')
st.divider()
on = st.toggle('原神啟動')
if on:
    st.write('啟動!')
st.divider()
genre = st.radio(
    "我跟阿德你要選誰?",
    [":violet[我]", "阿德"],
    captions = ["怎麼看都要選我", "選他口味很重"],
    index=None)
if genre == ':rainbow[我]':
    st.write('你真聰明')
else:
    st.write("請小心選擇")
