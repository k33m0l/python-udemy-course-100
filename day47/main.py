import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"
THRESHOLD_PRICE = 100

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US",
    "User-Agent": "Bot"
}
response = requests.get(url=URL, headers=headers).text
soup = BeautifulSoup(response, "html.parser")

price_tag = soup.find(name="span", class_="a-offscreen")
current_price = float(price_tag.get_text().split("$")[1])

if current_price <= THRESHOLD_PRICE:
    print("You should buy it quickly!")