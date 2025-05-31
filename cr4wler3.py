#!/usr/bin/env python3

import requests                                                                 
from bs4 import BeautifulSoup
from urllib.parse import urljoin
print("")

def crawl(url, visited_urls, depth=2):
    if depth == 0 or url in visited_urls:
        return
    print(f"\033[33mCrawling: \033[36m{url}")
    visited_urls.add(url)
    print("")
    try:
      response = requests.get(url)
      response.raise_for_status()
      soup = BeautifulSoup(response.text, 'html.parser')
      links = soup.find_all('a', href=True)
      for link in links:
        next_url = urljoin(url, link.get('href'))
        crawl(next_url, visited_urls, depth - 1)
    except requests.exceptions.RequestException as e:
      print("")
      print(f"\033[31mError crawling {url}: {e}")

start_url = 'https://example.com'
visited_urls = set()
crawl(start_url, visited_urls)

print("")
print(" \033[37mUsage:   \033[36mnano cr4wler3.py")
print("")
print(" \033[37mReplace  \033[32mhttps://example.com  \033[37mwith your url")
print("")
print("")
print("     Run Script     python3 cr4wler3.py")
print("")
print("     Menu           ./cr4wler.sh")
print("")
