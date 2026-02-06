import requests

def get_weather(city="Bhubaneswar"):
    url = f"https://wttr.in/{city}?format=3"
    return requests.get(url).text