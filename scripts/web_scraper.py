import requests
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    try:
        # Add headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text from paragraphs and other text elements
        text_elements = soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        text = ' '.join(element.get_text().strip() for element in text_elements if element.get_text().strip())
        
        return text
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return ""
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return ""