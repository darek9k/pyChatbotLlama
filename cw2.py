import streamlit as st

st.title('User interaction')

name = st.text_input('Give me your name')
if name:
    st.write(f'Hi, {name}!')