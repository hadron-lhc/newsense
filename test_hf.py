from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

frases = [
    "Apple reports record earnings this quarter",
    "Apple stock crashes amid fraud allegations",
    "Apple will hold its annual meeting next week",
]

for frase in frases:
    result = classifier(frase)
    print(f"{result[0]['label']:10} {result[0]['score']:.3f} — {frase}")
