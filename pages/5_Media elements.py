import streamlit as st
from PIL import Image

st.header('*Media elements*', divider= 'rainbow')
st.subheader('不知道要放啥')
st.caption('_說明說明說明_')
image = Image.open('https://github.com/YingJu-Chen-168/someone-s-learning/blob/main/pages/tutorial.jpg')
st.image(image, caption='可愛貓頭鷹')
