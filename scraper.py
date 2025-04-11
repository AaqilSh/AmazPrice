import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_product_data(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select_one("#productTitle")
    price = soup.select_one(".a-price .a-offscreen")

    if not title or not price:
        return None

    return {
        "title": title.get_text(strip=True),
        "price": price.get_text(strip=True)
    }
