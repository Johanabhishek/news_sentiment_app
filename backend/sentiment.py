from transformers import pipeline

# Load sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    return result["label"]  # Returns "POSITIVE", "NEGATIVE", or "NEUTRAL"
