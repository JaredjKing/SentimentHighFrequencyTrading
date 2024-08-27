from transformers import pipeline

def analyze_finbert(text):
    sentiment_pipeline = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone", device=0)
    result = sentiment_pipeline(text)[0]

    if result['label'] == "Negative":
        sentiment = -result['score']
    elif result['label'] == "Neutral":
        sentiment = float(0)
    else:
        sentiment = result['score']

    print("With the text: \" ", text, "\"")
    print("the sentiment is: ", sentiment, " ", result['label'])
    return sentiment