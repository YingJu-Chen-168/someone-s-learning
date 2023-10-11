import streamlit as st

st.header('*Text elements*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
code= '''def hello():
    print("Hello!")
#大家要記得縮排不然會報錯喔'''
st.code(code)
st.divider()
st.text("寫字寫字")
st.divider()
st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)''')
