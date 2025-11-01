import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_to_csv(base_url, start_page, filename):
    all_quotes = []
    current_page = start_page

    while current_page:
        response = requests.get(f"{base_url}{current_page}")
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            all_quotes.append({"text": text, "author": author, "tags": tags})

        next_link = soup.find('li', class_='next')
        current_page = next_link.find('a')['href'] if next_link else None

    df = pd.DataFrame(all_quotes)
    df.to_csv(filename, index=False)
    # df.to_json(filename, index=4)
    print(f"Data saved to {filename}")

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
filename = 'quotes.csv'
# filename = 'quotes.json'
extract_to_csv(base_url, start_page, filename)