import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next Days")
place = st.text_input("place: ")

days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="select number of forecast days")

option = st.selectbox("select Data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2023-25-10", "2023-26-10", "2023-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d,t = get_data(days)

figure = px.line(x=d,y=t,labels={"x":"Date","y":"temperature (c)"})
st.plotly_chart(figure)