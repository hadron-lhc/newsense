from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.fetcher import fetch_news
from core.database import init_db, get_articles_by_topic, save_articles
from core.analyzer import analyze_sentiment

app = FastAPI()


class AnalyzeRequest(BaseModel):
    topic: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/news")
def get_news(topic: str):
    conn = init_db()
    articles = fetch_news(topic)
    save_articles(conn, articles, topic)
    conn.close()
    return {"topic": topic, "count": len(articles), "articles": articles}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    conn = init_db()
    articles = get_articles_by_topic(conn, request.topic)
    conn.close()
    results = []
    for article in articles:
        sentiment = analyze_sentiment(article[0])
        results.append(
            {
                "title": article[0],
                "sentiment": sentiment["sentiment"],
                "score": sentiment["score"],
            }
        )
    return {"topic": request.topic, "results": results}
