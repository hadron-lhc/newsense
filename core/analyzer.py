from transformers import pipeline
from database import init_db, get_articles_by_topic

_classifier = None


def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        )
    return _classifier


def analyze_sentiment(text):
    classifier = get_classifier()
    result = classifier(text)
    return {"sentiment": result[0]["label"], "score": result[0]["score"]}


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
    main()
