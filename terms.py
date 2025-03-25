import requests
from bs4 import BeautifulSoup
import json

def get_twitter_trends(country='worldwide'):
    """
    Scrape trending topics from Twitter/X
    Note: This method is fragile and may break due to site changes
    """
    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        # X/Twitter trends page
        url = 'https://twitter.com/i/trends'
        
        # Send GET request
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is a placeholder - actual selector will depend on X's current HTML structure
        trend_elements = soup.select('div[data-testid="trend"]')
        
        # Extract trend texts
        trends = [trend.text for trend in trend_elements if trend.text]
        
        return trends
    
    except requests.RequestException as e:
        print(f"Error fetching trends: {e}")
        return []

def main():
    # Fetch and print trending topics
    trending_topics = get_twitter_trends()
    
    print("Current Trending Topics:")
    for index, topic in enumerate(trending_topics, 1):
        print(f"{index}. {topic}")

if __name__ == "__main__":
    main()