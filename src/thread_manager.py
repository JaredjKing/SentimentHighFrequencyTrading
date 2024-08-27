import threading
from src.sentiment_analysis import analyze_vader
from src.financial_sentiment import analyze_finbert

class SentimentAnalyzer:
    def __init__(self, text):
        self.text = text
        self.vader_result = None
        self.finbert_result = None

    # thread function to compute sentiment analysis
    def vader_thread(self):
        self.vader_result = analyze_vader(self.text)

    # thread functon to compute financial sentiment analysis
    def finbert_thread(self):
        self.finbert_result = analyze_finbert(self.text)

    # creates a thread for each sentiment analyses and averages values 
    def run_analysis(self):
        t1 = threading.Thread(target=self.vader_thread)
        t2 = threading.Thread(target=self.finbert_thread)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()

        print("Sentiment Result: ", self.vader_result)
        print("Financial Result: ", self.finbert_result)
        print("Combined: ", self.combine_results())

        return self.combine_results()

    # computes weighted average of models given parameters 
    def combine_results(self, vader_weight=0.25, finbert_weight=0.75):
        combined = (self.vader_result * vader_weight) + (self.finbert_result * finbert_weight)
        return combined
