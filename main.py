import streamlit as st

st.title("Weather forecast for the next Days")
place = st.text_input("place: ")

days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="select number of forecast days")

option = st.selectbox("select Data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")