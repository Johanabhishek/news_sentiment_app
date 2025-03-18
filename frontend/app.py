from backend.scraper import fetch_news
from backend.sentiment import analyze_sentiment
from backend.tts import text_to_speech

def main():
    # Fetch news articles
    articles = fetch_news()
    
    # Perform sentiment analysis
    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        article["sentiment"] = sentiment

    # Convert first summary to Hindi speech
    if articles:
        text_to_speech(articles[0]["summary"])

    # Print results
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Sentiment: {article['sentiment']}")
        print("-" * 50)

if __name__ == "__main__":
    main()
