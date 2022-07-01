import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'
res = requests.get(url)
print(res)
print(res.text)
