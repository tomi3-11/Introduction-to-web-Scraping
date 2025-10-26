import os
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

os.makedirs('images', exist_ok=True)

for image in images:
    src = image['src'] # image 1
    # src = images[1]['src'] # image 2

    full_src = f"https://books.toscrape.com/{src}" if not src.startswith('http') else src

    img_response = requests.get(full_src, stream=True)

    if img_response.status_code == 200:
        img_name = os.path.basename(src)
        with open(f"images/{img_name}", 'wb') as f:
            for chunk in img_response.iter_content(1024):
                f.write(chunk)
        print(f"Saved {img_name}")