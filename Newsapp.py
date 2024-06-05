import requests
import json

from bs4 import BeautifulSoup
def creatingnews():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=eacbc0d03f5248aba38736ae85c08998"
    response = requests.get(url)


    data = json.loads(response.text)  # Parse the JSON response

    articles = data.get("articles", [])  # Extract the "articles" array from the response

    for article in articles:
        title = article.get("title", "")  # Get the title attribute of each article
        print(title)


creatingnews()
