from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from core.database import init_db, get_articles_by_topic
import os

API_URL = "https://router.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"


load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(provider="hf-inference", api_key=HF_TOKEN)


def analyze_sentiment(text):
    result = client.text_classification(
        text, model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
    best = max(result, key=lambda x: x.score)
    return {"sentiment": best.label, "score": best.score}


def main():
    conn = init_db()
    topic = "Apple"
    report = []
    articles = get_articles_by_topic(conn, topic)
    for article in articles:
        sentiment = analyze_sentiment(article[0])
        report.append({"title": article[0], **sentiment})

    for item in report:
        print(f"{item['sentiment']:10} {item['score']:.2f} — {item['title'][:60]}")


if __name__ == "__main__":
    from core.database import init_db, get_articles_by_topic

    main()
