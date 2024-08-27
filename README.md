Sentiment High-Frequency Trading (HFT) Project
Overview
This project is a High-Frequency Trading (HFT) system that leverages sentiment analysis from financial news sources to make trading decisions. The project integrates multiple sentiment analysis models, including VADER and FinBERT, to assess the sentiment of financial news articles in real time. The combined sentiment scores are used to influence trading strategies, with the goal of gaining an edge in the market.

Project Structure
HFTAlgoProject/
├── src/
│   ├── data_collection.py       # Handles data collection from financial news APIs
│   ├── thread_manager.py        # Manages multithreading for sentiment analysis
│   ├── financial_sentiment.py   # Financial sentiment analysis using FinBERT
│   ├── vader_sentiment.py       # General sentiment analysis using VADER
├── tests/
│   ├── test_data_collection.py  # Unit tests for data collection
│   ├── test_thread_manager.py   # Unit tests for threading and sentiment analysis logic
├── config/
│   ├── api_keys.json            # API keys and configuration (gitignored)
│   ├── config.py                # Configuration management (e.g., API key loading)
└── README.md                    # Project overview and instructions

Features
    - Data Collection: Fetches financial news articles from APIs like NewsAPI, Alpha Vantage, or Finnhub.
    - Sentiment Analysis:
        - VADER: Provides general sentiment analysis, well-suited for social media and short text.
        - FinBERT: Specialized for financial text, offering more precise sentiment analysis for financial news.
    - Multithreading: Runs VADER and FinBERT sentiment analysis in parallel, improving efficiency.
    - Sentiment Averaging: Combines sentiment scores from both models, with adjustable weighting to fine-tune the trading strategy.
