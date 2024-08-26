from transformers import pipeline

def analyze_finbert(text):
    sentiment_pipeline = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone")
    result = sentiment_pipeline(text)
    # Convert the FinBERT output to a similar format as VADER
    score = {
        'pos': 0.0,
        'neg': 0.0,
        'neu': 0.0,
        'compound': 0.0
    }
    
    if result[0]['label'] == 'positive':
        score['pos'] = result[0]['score']
        score['compound'] = result[0]['score']
    elif result[0]['label'] == 'negative':
        score['neg'] = result[0]['score']
        score['compound'] = -result[0]['score']
    else:
        score['neu'] = result[0]['score']
    
    return score
