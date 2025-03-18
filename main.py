import sys
import os

# Add backend to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.scraper import fetch_news
from backend.sentiment import analyze_sentiment
from backend.tts import text_to_speech


def main():
    print("Fetching news...")  # Debugging print
    articles = fetch_news()
    
    if not articles:
        print("No articles found!")
        return

    print("Performing sentiment analysis...")  # Debugging print
    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        article["sentiment"] = sentiment
        print(f"Title: {article['title']}")
        print(f"Sentiment: {article['sentiment']}")
        print("-" * 50)

    print("Converting text to speech...")  # Debugging print
    text_to_speech(articles[0]["summary"])
    print("Done!")

if __name__ == "__main__":
    main()
 
