import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_to_csv(base_url, start_page, filename):
    all_quotes = []
    current_page = start_page

    while current_page:
        response = requests.get(f"{base_url}{current_page}")
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')[:2]

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]

            # Get author's detail page URL and fetch the birthdate
            author_url_tag = quote.select_one('span a')
            author_url = author_url_tag['href']

            author_response = requests.get(f"{base_url}{author_url}")
            author_soup = BeautifulSoup(author_response.text, 'html.parser')

            # TODO: Update the lines below to fetch the author description instead of the birth date
            # Hint: It can be found in the element with class 'author-description'
            description_tag = author_soup.find('div', class_='author-description')
            description = description_tag.text

            # TODO: Update the append statement to include the description
            all_quotes.append({"text": text, "author": author, "tags": tags, "description": description})

        next_link = soup.find('li', class_='next')
        current_page = next_link.find('a')['href'] if next_link else None

    df = pd.DataFrame(all_quotes)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
filename = 'quotes.csv'
extract_to_csv(base_url, start_page, filename)