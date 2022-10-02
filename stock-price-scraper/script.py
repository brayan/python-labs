import requests
from googlesearch import search
import urllib
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

URL = "https://www.google.com/search?q=vale3"
page = google_scrape('vale3')
print(page)
# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="vWLAgc")

# print(results.prettify())