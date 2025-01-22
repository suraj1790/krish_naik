import streamlit as st

hindi = st.number_input("Hindi",0)

math = st.number_input("math",0)

physics = st.number_input("physics",0)

chemistry = st.number_input("chemistry",0)

english = st.number_input("english",0)


total_per = hindi+math+physics+chemistry+english

if total_per >= 30 and physics>30 and hindi >= 30 and english >= 30 and math >= 30 and chemistry >=30:
    st.write("You have to passed")
else:
    st.write("You have to failed")