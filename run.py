import sys
from src.thread_manager import SentimentAnalyzer
import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Example text for analysis
    text = """Unwinds of stretched positions, U.S. recession fears and policy uncertainty have sparked big market swings - exacerbated by
        thin trading activity. The BOJ's sudden willingness to incorporate the yen as a factor in setting policy accelerated an unwind of carry 
        trades that use the low-yielding yen to buy other assets. Speculators scrambling to close their short-yen positions drove one of the largest 
        unwinds in yen futures on record in the past few weeks, according to CFTC data. 

        Up until recently the BOJ had been deliberate in trying to normalize policy without jeopardizing Japan's return of inflation. Then came its sudden rate 
        hike in July and blurring of its policy framework, including the yen as a factor. The rise of a BOJ policy misstep prompted us to reconsider our positive 
        view on Japan. Yet we felt the BOJ would be forced to walk back - and did. We think the BOJ will now proceed cautiously on policy, so we stay overweight 
        Japanese stocks on a currency-unhedged basis. 

        While Japan bore the brunt of last week's turbulence, U.S. recession fears sparked the latest slide after U.S. payrolls data for July showed an uptick in 
        the unemployment rate. Yet the unemployment rate is still remarkably low by historical standards - and it's rising because of a growing labor force tied to 
        immigration, not because of job losses. Total U.S. payrolls have grown more than 1 million over the past six months, well above usual pre-recession levels. 
        The latest jobless claims, ISM services data and Fed bank lending survey all paint the picture of an economy that is slowing, not approaching recession, in 
        our view.

        Stronger-than-expected U.S. corporate earnings, especially in tech, reaffirm our positive U.S. view. To date, Q2 earnings growth for tech versus non-tech 
        sectors sits at 20 percent and 5percent, respectively - up from expectations of 18 percent and 2 precent at the start of earnings season, according to LSEG
        Datastream data. While tech is leading the charge, non-tech sectors are poised to log their first earnings growth since late 2022, a sign strong earnings 
        may be broadening out. Easing cost pressures and moderating inflation have benefited U.S. corporates. We stay overweight U.S. stocks and the artificial 
        intelligence (AI) theme."""

    # Initialize the SentimentAnalyzer with the example text
    analyzer = SentimentAnalyzer(text)

    # Run the sentiment analysis
    try:
        result = analyzer.run_analysis()
        logger.info("Sentiment analysis result: %s", result)
    except Exception as e:
        logger.error("Error occurred during sentiment analysis: %s", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
