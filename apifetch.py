import requests
from pprint import pprint

# WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
# API_KEY = "5321674b7863f1cae6a2dcda7ab0322d"
# CITY = "Minnesota"


# url = WEATHER_URL + "appid=" + API_KEY + "&q=" + CITY


# response = requests.get(url).json()
# print(
#     "_________________________________________________________________________________"
# )
# print("WEATHER API")
# print()
# pprint(response)
# print(
#     "_________________________________________________________________________________"
# )
def getItems_fromlist(param, response):
    if isinstance(response, list):
        for item in response:
            get_obj = item.get(param)
            pprint(get_obj)
    else:
        get_obj = response.get(param)
        pprint(get_obj)


DJANGO_URL = "http://127.0.0.1:8000/api/"
# Available paths:
# tasks/:userid
# location/:userid

path = input("Enter Path: ")

url = DJANGO_URL + path

response = requests.get(url).json()
location = response.get("weather")["location"]
print(
    "_________________________________________________________________________________"
)
print("WEATHER API")

# getItems_fromlist("weather", response)
pprint(location)

print(
    "_________________________________________________________________________________"
)


# # NEWS API
# NEWS_URL = "https://newsapi.org/v2/top-headlines/?sources=bbc-news&apiKey=0dcc3ef4f630463699f2f87b79983d75"
# # NEWS_URL = "https://newsapi.org/v2/everything?q=Apple?from=2024-01-01?sortBy=popularity?apiKey=0dcc3ef4f630463699f2f87b79983d75"

# response = requests.get(NEWS_URL).json().get("article", [])


# print(
#     "_________________________________________________________________________________"
# )
# print("NEWS API")
# print()
# pprint(response)
# print(
#     "_________________________________________________________________________________"
# )


# # Replace 'YOUR_API_KEY' with your actual News API key
# api_key = "0dcc3ef4f630463699f2f87b79983d75"

# # News API endpoint for top headlines
# url = f"https://newsapi.org/v2/top-headlines"

# # Parameters for the request, such as the news source and API key
# params = {
#     "sources": "bbc-news",  # Replace with your desired news source
#     "apiKey": api_key,
# }

# # Making the request to the News API
# response = requests.get(url, params=params)

# # Getting the response object
# if response.status_code == 200:
#     # The 'response' object now contains information about the top headlines
#     news_data = response.json()

#     # Extracting descriptions and source names
#     articles = news_data.get("articles", [])
#     for article in articles:
#         description = article.get("description")
#         source_name = article.get("source", {}).get("name")
#         published_at = article.get("publishedAt")

#         print(f"Description: {description}")
#         print(f"Source Name: {source_name}")
#         print(f"Published At: {published_at}")
#         print("------")
# else:
#     print(f"Error: {response.status_code} - {response.text}")
