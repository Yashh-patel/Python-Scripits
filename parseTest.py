import requests
from bs4 import BeautifulSoup

URL = "https://shop.havenshop.com/collections/cav-empt"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
