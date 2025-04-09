import requests
from bs4 import BeautifulSoup
import json
import time

base_url = "https://www.goodreads.com/author/quotes/6862186.Naval_Ravikant"
headers = {"User-Agent": "Mozilla/5.0"}

all_quotes = []

# Try pages 1 to 5 (can go higher if needed)
for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = f"{base_url}?page={page}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    quote_divs = soup.find_all("div", class_="quoteText")

    for div in quote_divs:
        text = div.get_text(strip=True).split("―")[0].strip()
        if text:
            all_quotes.append(text)

    time.sleep(1)  # Be nice to Goodreads, add delay

# Save merged quotes
with open("naval_quotes_goodreads.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, ensure_ascii=False, indent=2)

print(f"✅ Scraped {len(all_quotes)} quotes from Goodreads.")
