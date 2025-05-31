#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def crawl_page(url):
    """Fetches and parses a webpage, extracting links."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        return links
    except requests.exceptions.RequestException as e:
        print(f"\033[31mError fetching {url}: {e}")
        return []

def main():
    """Prompts the user for a URL and crawls the page."""
    while True:
        print("")
        url = input("\033[37mEnter the URL to crawl or type 'a' to abort > " )
        if url.lower() == 'a':
            break
        if not url.startswith("http://") and not url.startswith("https://"):
            print("")
            print("\033[37mPlease enter a valid URL (e.g., http://example.com)")
            continue
        print("")
        print(f"\033[93mCrawling: \033[36m{url}\033[32m\n")
        links = crawl_page(url)

        if links:
            for link in links:
                print(link['href'])
        else:
            print("")
            print("\033[31mNo links found or error occurred.")

if __name__ == "__main__":
    main()

print("\033[37m")
print("     Run Script     python3 cr4wler1.py")
print("")
print("     Menu           ./cr4wler.sh")
print("")
