import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://news.ycombinator.com/"  # Example news site
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching news")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for item in soup.select(".titleline a")[:10]:  # Get top 10 headlines
        title = item.text
        link = item["href"]
        articles.append({"title": title, "summary": "Summary not available", "link": link})
    
    return articles
