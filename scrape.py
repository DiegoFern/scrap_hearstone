import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://playhearthstone.com/es-es/cards/')
soup = BeautifulSoup(page.read())
print(soup)
