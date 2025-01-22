import streamlit as st

st.title("this is my first streamlit file ")
st.write("hello")

name = st.text_input("Enter your name")
st.write(f"My name is {name}")
