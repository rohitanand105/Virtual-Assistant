import requests
from bs4 import BeautifulSoup

r = requests.get("https://groww.in/stocks/indian-overseas-bank")

print(r.content)

