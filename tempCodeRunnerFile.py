
# NEWS API
# NEWS_URL = "https://newsapi.org/v2/top-headlines/sources?country=us&apiKey=0dcc3ef4f630463699f2f87b79983d75"
NEWS_URL = "https://newsapi.org/v2/everything?q=Apple&from=2024-01-01&sortBy=popularity&apiKey=0dcc3ef4f630463699f2f87b79983d75"
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