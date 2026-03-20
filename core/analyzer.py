from transformers import pipeline

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


if __name__ == "__main__":
    result = analyze_sentiment(
        "Apple will hold its annual meeting next week"
    )  # ejemplo
    print(result)
