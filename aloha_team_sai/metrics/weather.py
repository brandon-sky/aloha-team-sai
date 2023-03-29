import requests
import streamlit as st
from datetime import date
from typing import List
from pydantic import BaseModel

API_URL = "https://api.weatherapi.com/v1/forecast.json"
API_KEY = "e8dfe77ac8d2432292a213014232903"
LOCATION = "Honolulu"
NUM_DAYS = 3
ICON_WIDTH = 75

class WeatherCondition(BaseModel):
    text: str
    icon: str

class WeatherDay(BaseModel):
    date: date
    avgtemp_c: float
    daily_chance_of_rain: int
    condition: WeatherCondition

class WeatherForecast(BaseModel):
    forecastday: List[WeatherDay]


   
def __get_weather_data():

    # Setze die URL der API und den API-Schlüssel
    url = API_URL
    api_key = API_KEY

    # Setze die Parameter für die Anfrage
    params = {
        "key": api_key,
        "q": LOCATION,
        "days": NUM_DAYS
    }

    # Sende die GET-Anfrage an die API und speichere die Antwort
    response = requests.get(url, params=params)
    weather_data = response.json()
    return weather_data


def __transform_data(data):
    forecast_data = data['forecast']['forecastday']
    weather_forecast = WeatherForecast(forecastday=[])

    for day_data in forecast_data:
        day = WeatherDay(
            date=date.fromisoformat(day_data['date']),
            avgtemp_c=day_data['day']['avgtemp_c'],
            daily_chance_of_rain=day_data['day']['daily_chance_of_rain'],
            condition=WeatherCondition(
                text=day_data['day']['condition']['text'],
                icon=day_data['day']['condition']['icon']
            )
        )
        weather_forecast.forecastday.append(day)
    return weather_forecast


def WeatherInfo():
    data = __get_weather_data()
    data = __transform_data(data)
    
    for index, column in enumerate(st.columns(3)):
        with column:
            day = data.forecastday[index]
            st.metric(label=day.date.strftime('%d.%m.'), value=day.date.strftime('%A'))
            st.image(f"http:{day.condition.icon}", width=ICON_WIDTH)
            st.metric(label="Regen", value=f"{day.daily_chance_of_rain} %")
            st.metric(label="Temperatur", value=f"{day.avgtemp_c} °C")

