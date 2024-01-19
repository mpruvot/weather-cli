import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


class WeatherData:
    """
    A class representing weather data for a specific city.

    Attributes:
        city_name (str): The name of the city.
        url (str): The URL of the weather API.
        params (dict): The parameters for the API request.
        response (Response): The response object from the API request.
        data (dict): The JSON data returned by the API.

    Methods:
        __init__(self, city_name): Initializes a new instance of the WeatherData class.
        __str__(self): Returns a string representation of the WeatherData object.
        get_data(self): Returns the weather data.
        get_temperature(self): Returns the current temperature.
        get_humidity(self): Returns the current humidity.
        get_weather_code(self): Returns the weather code.
        get_weather_icon(self): Returns the URL of the weather icon.
        get_wind_speed(self): Returns the wind speed.
        get_wind_direction(self): Returns the wind direction.
        get_city_name(self): Returns the name of the city.
        get_country_name(self): Returns the name of the country.
        get_local_time(self): Returns the local time of the city.
    """

    def __init__(self, city_name):
        self.city_name = city_name
        self.url = "http://api.weatherstack.com/current"
        self.params = {
            "access_key": API_KEY,
            "query": city_name,
        }
        self.response = requests.get(self.url, params=self.params)
        self.response.raise_for_status()
        self.data = self.response.json()

    def __str__(self) -> str:
        return f"{self.city_name} Weather Data"

    @property
    def get_data(self):
        return self.data

    def get_temperature(self):
        return self.data["current"]["temperature"]

    def get_humidity(self):
        return self.data["current"]["humidity"]

    def get_weather_code(self):
        return self.data["current"]["weather_code"]

    def get_weather_icon(self):
        return self.data["current"]["weather_icons"][0]

    def get_wind_speed(self):
        return self.data["current"]["wind_speed"]

    def get_wind_direction(self):
        return self.data["current"]["wind_dir"]

    def get_city_name(self):
        return self.data["location"]["name"]

    def get_country_name(self):
        return self.data["location"]["country"]

    def get_local_time(self):
        return self.data["location"]["localtime"]
