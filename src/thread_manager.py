import threading
from src.sentiment_analysis import analyze_vader
from src.financial_sentiment import analyze_finbert

class SentimentAnalyzer:
    def __init__(self, text):
        self.text = text
        self.vader_result = None
        self.finbert_result = None

    def vader_thread(self):
        self.vader_result = analyze_vader(self.text)

    def finbert_thread(self):
        self.finbert_result = analyze_finbert(self.text)

    def run_analysis(self):
        t1 = threading.Thread(target=self.vader_thread)
        t2 = threading.Thread(target=self.finbert_thread)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()

        return self.combine_results()

    def combine_results(self, vader_weight=0.5, finbert_weight=0.5):
        combined = {
            'pos': (self.vader_result['pos'] * vader_weight) + (self.finbert_result['pos'] * finbert_weight),
            'neg': (self.vader_result['neg'] * vader_weight) + (self.finbert_result['neg'] * finbert_weight),
            'neu': (self.vader_result['neu'] * vader_weight) + (self.finbert_result['neu'] * finbert_weight),
            'compound': (self.vader_result['compound'] * vader_weight) + (self.finbert_result['compound'] * finbert_weight)
        }
        return combined
