import streamlit as st

st.title("This is my second web application: ")

name = st.text_input("Enter your name here")
age = st.slider("scroll till your age",0,75,12)
gender = st.selectbox("select your gender",["Male","Female"])

marks = st.number_input("Enter your percentage")


st.write(f"your name is {name}")
st.write(f"Your age is {age}")
st.write(f"you are a {gender}")
if marks >= 50:
    st.write("You have to passed")
else:
    st.write("you have to failed")