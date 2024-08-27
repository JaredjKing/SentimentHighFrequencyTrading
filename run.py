import sys
from src.thread_manager import SentimentAnalyzer
import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Example text for analysis
    text = "The financial outlook is positive and market trends are favorable."

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
