import streamlit as st

st.title("Student Details Form")
st.subheader("AIML DEPARTMENT")

name = st.text_input("Enter Your Name: ")
PRN = st.text_input("Enter Your PRN: ")
age = st.number_input("Enter Your Age: ")
gender = st.radio('Select Gender:', ['Male','Female','Other'])
phone = st.number_input("Enter Your Contact Number: ")

button = st.button("Submit.")

if button:
    st.text(f"Name : {name}")
    st.text(f"PRN : {PRN}")
    st.text(f"age : {age}")
    st.text(f"Gender : {gender}")
    st.text(f"phone : {phone}")
