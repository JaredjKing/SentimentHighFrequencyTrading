from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_vader(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)