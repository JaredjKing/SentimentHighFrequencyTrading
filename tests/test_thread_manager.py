import unittest
from src.thread_manager import SentimentAnalyzer

class TestThreadManager(unittest.TestCase):
    def test_run_analysis(self):
        # Sample text
        text = "The financial outlook is positive and market trends are favorable."
        
        # Create an instance of SentimentAnalyzer
        analyzer = SentimentAnalyzer(text)
        
        # Run analysis
        result = analyzer.run_analysis()
        
        # Check that results are not None and are dictionaries
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('pos', result)
        self.assertIn('neg', result)
        self.assertIn('neu', result)
        self.assertIn('compound', result)
        
        # Check that the compound score is within the expected range
        self.assertGreaterEqual(result['compound'], 0)
        self.assertLessEqual(result['compound'], 1)

if __name__ == "__main__":
    unittest.main()
