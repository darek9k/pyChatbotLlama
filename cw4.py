import streamlit as st
import time

st.title('Streamlit Example with Spinner')

with st.spinner('Please wait... Loading data'):
    # Simulating a long-running operation
    time.sleep(5)

st.success('Data has been loaded!')