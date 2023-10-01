import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next Days")
place = st.text_input("place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select number of forecast days")

option = st.selectbox("select Data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filterd_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filterd_data]

            temperatures = [tempreture/10 for tempreture in temperatures ]

            dates = [dict["dt_txt"] for dict in filterd_data]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date","y":"temperature (c)"})
            st.plotly_chart(figure)

        if option == "Sky":
            image = {"Clear": "images/clear.png", "Clouds": "images/cloud.png"
                     , "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filterd_data]
            image_path = [image[condition] for condition in sky_conditions]
            st.image(image_path, width=115)

    except KeyError:
        st.write("There is No city with this name!!")