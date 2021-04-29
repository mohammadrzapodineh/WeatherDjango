import requests


def get_weather_data(url):
    data = requests.get(url)
    return data.json()