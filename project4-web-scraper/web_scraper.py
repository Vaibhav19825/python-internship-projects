
# Project 4 - Web Scraper for Quotes

import requests
from bs4 import BeautifulSoup
import json
import time
import os

quotes_list = []

try:
    for page_number in range(1, 3):

        url = "https://quotes.toscrape.com/page/" + str(page_number) + "/"

        print("Getting quotes from page", page_number)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for item in quotes:
            quote = item.find("span", class_="text")
            author = item.find("small", class_="author")
            tags = item.find_all("a", class_="tag")

            if quote is not None and author is not None:
                data = {
                    "quote": quote.get_text(strip=True),
                    "author": author.get_text(strip=True),
                    "tags": []
                }

                for tag in tags:
                    data["tags"].append(tag.get_text(strip=True))

                quotes_list.append(data)

        if page_number < 2:
            time.sleep(1)

    folder = os.path.dirname(__file__)
    filename = os.path.join(folder, "quotes.json")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(quotes_list, file, indent=4, ensure_ascii=False)

    print("\nScraping completed successfully!")
    print("Total quotes saved:", len(quotes_list))

except requests.exceptions.RequestException as error:
    print("Website connection error:", error)
