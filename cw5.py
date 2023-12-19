import streamlit as st

st.title("Business Card Generator")

name = st.text_input('Enter your first name')
surname = st.text_input('Enter your last name')
profession = st.selectbox("Select profession", ("Developer", "Tester", "Administrator", "Other"))
radio = st.radio("Select gender", ("Male", "Female"))

if st.button("Generate business card"):
    if name and surname and profession:
        st.write(f"First Name: {name}")
        st.write(f"Last Name: {surname}")
        st.write(f"Profession: {profession}")
        st.write(f"Gender: {radio}")
    else:
        st.error("Fill in all fields!")