from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox options
options = Options()
options.headless = True  # Run in background

# Initialize Firefox driver
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)
from bs4 import BeautifulSoup
import time

def get_twitter_trends(country="United States"):
    # Set up Selenium with Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Open Twitter's explore page for trends
        driver.get(f"https://twitter.com/explore/tabs/trending")
        
        # Wait for trends to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Timeline: Trending now"]'))
        )
        
        # Give it some extra time to load
        time.sleep(3)
        
        # Change location if needed
        if country != "Worldwide":
            try:
                # Click the settings icon
                settings_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Settings"]')
                settings_button.click()
                
                # Click "Change location"
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Change location")]'))
                ).click()
                
                # Search for the country
                search_box = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]'))
                )
                search_box.send_keys(country)
                
                # Select the country from results
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f'//span[contains(text(), "{country}")]'))
                ).click()
                
                # Wait for trends to reload
                time.sleep(5)
            except Exception as e:
                print(f"Couldn't change location: {e}")
        
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Extract trends - this selector might need updating if Twitter changes its layout
        trends = []
        trend_elements = soup.select('[data-testid="trend"]')
        
        for trend in trend_elements:
            try:
                topic = trend.select_one('[data-testid="trend"] div:nth-child(1) div:nth-child(1)').text
                tweet_count = trend.select_one('[data-testid="trend"] div:nth-child(1) div:nth-child(2)').text
                trends.append({
                    'topic': topic,
                    'tweet_count': tweet_count
                })
            except AttributeError:
                continue
        
        return trends
    
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    country = "India"  # Change to your desired country
    trends = get_twitter_trends(country)
    
    print(f"\nTop 10 Trending Topics in {country}:")
    for i, trend in enumerate(trends[:10], 1):
        print(f"{i}. {trend['topic']} - {trend.get('tweet_count', 'N/A')}")