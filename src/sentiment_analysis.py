from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_vader(text):
    sia = SentimentIntensityAnalyzer()
    result = sia.polarity_scores(text)['compound']
    
    return result