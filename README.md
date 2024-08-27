# Sentiment High-Frequency Trading (HFT) Project

## Overview
This project is a High-Frequency Trading (HFT) system that leverages sentiment analysis from financial news sources to make trading decisions. The project integrates multiple sentiment analysis models, including VADER and FinBERT, to assess the sentiment of financial news articles in real time. The combined sentiment scores are used to influence trading strategies, with the goal of gaining an edge in the market.

## Project Structure
HFTAlgoProject/<br>
├── src/<br>
│&nbsp;&nbsp;&nbsp;├── data_collection.py&nbsp;&nbsp;&nbsp;// Handles data collection from financial news APIs<br>
│&nbsp;&nbsp;&nbsp;├── thread_manager.py&nbsp;&nbsp;&nbsp;// Manages multithreading for sentiment analysis<br>
│&nbsp;&nbsp;&nbsp;├── financial_sentiment.py&nbsp;&nbsp;&nbsp;// Financial sentiment analysis using FinBERT<br>
│&nbsp;&nbsp;&nbsp;├── vader_sentiment.py&nbsp;&nbsp;&nbsp;// General sentiment analysis using VADER<br>
├── tests/<br>
│&nbsp;&nbsp;&nbsp;├── test_data_collection.py&nbsp;&nbsp;&nbsp;// Unit tests for data collection<br>
│&nbsp;&nbsp;&nbsp;├── test_thread_manager.py&nbsp;&nbsp;&nbsp;// Unit tests for threading and combinational logic<br>
│&nbsp;&nbsp;&nbsp;├── test_finance_sentiment.py&nbsp;&nbsp;&nbsp;;// Unit tests for financial sentiment logic<br>
│&nbsp;&nbsp;&nbsp;├── test_sentiment_analysis.py&nbsp;&nbsp;&nbsp;// Unit tests for sentiment analysis logic<br>
├── config/<br>
│&nbsp;&nbsp;&nbsp;├── api_keys.json&nbsp;&nbsp;&nbsp;// API keys and configuration (gitignored)<br>
│&nbsp;&nbsp;&nbsp;├── config.py&nbsp;&nbsp;&nbsp;// Configuration management (e.g., API key loading)<br>
└── README.md&nbsp;&nbsp;&nbsp;// Project overview and instructions<br>
└── requirements.txt&nbsp;&nbsp;&nbsp;// required dependincies<br>
└── run.py&nbsp;&nbsp;&nbsp;// run project<br>

## Features
- **Data Collection**: Fetches financial news articles from APIs like NewsAPI, Alpha Vantage, or Finnhub.
- **Sentiment Analysis**:
    - **VADER**: Provides general sentiment analysis, well-suited for social media and short text.
    - **FinBERT**: Specialized for financial text, offering more precise sentiment analysis for financial news.
- **Multithreading**: Runs VADER and FinBERT sentiment analysis in parallel, improving efficiency.
- **Sentiment Averaging**: Combines sentiment scores from both models, with adjustable weighting to fine-tune the trading strategy.

