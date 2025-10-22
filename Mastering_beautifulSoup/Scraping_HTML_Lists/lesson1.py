from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books_ordered_list = soup.select(".page_inner section ol li")

for book in books_ordered_list:
    title = book.select("article h3 a")[0]["title"]
    print(title)