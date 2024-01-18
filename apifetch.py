import datetime
import requests
from pprint import pprint

# openweathermap
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5321674b7863f1cae6a2dcda7ab0322d"
CITY = "Minnesota"


url = WEATHER_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
print(
    "_________________________________________________________________________________"
)
print("WEATHER API")
print()
pprint(response)
print(
    "_________________________________________________________________________________"
)


# NEWS API
NEWS_URL = "https://newsapi.org/v2/top-headlines/sources?country=us&apiKey=0dcc3ef4f630463699f2f87b79983d75"
response = requests.get(NEWS_URL).json()

print(
    "_________________________________________________________________________________"
)
print("NEWS API")
print()
pprint(response)
print(
    "_________________________________________________________________________________"
)
