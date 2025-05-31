#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

def crawl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print("")
        print(f"  \033[91mError Fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith('http'):
            links.append(link)
        else:
            links.append(url + link)


    if links:
        print("")
        print("  \033[1;96mLinks Found \033[0m")
        print("")
        for link in links:
            print(link)
    else:
        print("")
        print("\033[91mNo links found on this page.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("")
        print("     \033[37mUsage: python3 cr4wler2.py <url>")
        print("")  
        sys.exit(1)

    url = sys.argv[1]
    crawl(url)
print("\033[37m")
print("  Run Script     python3 cr4wler2.py <url>")
print("")
print("  Menu           ./cr4wler.sh")
print("")
