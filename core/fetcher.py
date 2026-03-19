from dotenv import load_dotenv
import os
import requests
import json


def fetch_news(topic, page_size=20):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": api_key,
        "pageSize": page_size,
        "language": "en",
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("articles", [])


if __name__ == "__main__":
    load_dotenv()  # carga el .env

    api_key = os.getenv("NEWSAPI_KEY")

    articles = fetch_news("Apple")
    print(json.dumps(articles[0], indent=2))
    """
    for a in articles[:5]:
        print(a["title"])
    """
