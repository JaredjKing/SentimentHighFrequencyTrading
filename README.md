# Sentiment High-Frequency Trading (HFT) Project

## Overview
This project is a High-Frequency Trading (HFT) system that leverages sentiment analysis from financial news sources to make trading decisions. The project integrates multiple sentiment analysis models, including VADER and FinBERT, to assess the sentiment of financial news articles in real time. The combined sentiment scores are used to influence trading strategies, with the goal of gaining an edge in the market.

## Project Structure
HFTAlgoProject/<br>
├── src/<br>
│   ├── data_collection.py          // Handles data collection from financial news APIs<br>
│   ├── thread_manager.py           // Manages multithreading for sentiment analysis<br>
│   ├── financial_sentiment.py      // Financial sentiment analysis using FinBERT<br>
│   ├── vader_sentiment.py          // General sentiment analysis using VADER<br>
├── tests/<br>
│   ├── test_data_collection.py     // Unit tests for data collection<br>
│   ├── test_thread_manager.py      // Unit tests for threading and combinational logic<br>
│   ├── test_finance_sentiment.py   // Unit tests for financial sentiment logic<br>
│   ├── test_sentiment_analysis.py  // Unit tests for sentiment analysis logic<br>
├── config/<br>
│   ├── api_keys.json                // API keys and configuration (gitignored)<br>
│   ├── config.py                    // Configuration management (e.g., API key loading)<br>
└── README.md                        // Project overview and instructions<br>
└── requirements.txt                 // required dependincies<br>
└── run.py                           // run project<br>

## Features
- **Data Collection**: Fetches financial news articles from APIs like NewsAPI, Alpha Vantage, or Finnhub.
- **Sentiment Analysis**:
    - **VADER**: Provides general sentiment analysis, well-suited for social media and short text.
    - **FinBERT**: Specialized for financial text, offering more precise sentiment analysis for financial news.
- **Multithreading**: Runs VADER and FinBERT sentiment analysis in parallel, improving efficiency.
- **Sentiment Averaging**: Combines sentiment scores from both models, with adjustable weighting to fine-tune the trading strategy.

