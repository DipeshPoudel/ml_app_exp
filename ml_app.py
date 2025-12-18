import streamlit as st

st.title("My New Application")

age = st.sidebar.slider('Age',min_value=1,max_value=100,step=1)
gender = st.sidebar.selectbox('Gender',['Male','Female','Others'])
smoking = st.sidebar.selectbox('Smoking',['Yes','No'])