import streamlit as st

st.title('Dropdown List Selection')

option = st.selectbox(
    'What is your favorite animal?',
    ('Dog', 'Cat', 'Rabbit', 'Parrot')
)

st.write('Your favorite animal is:', option)