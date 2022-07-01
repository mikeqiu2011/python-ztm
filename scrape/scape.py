import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)

print(soup.find_all('div'))  # get all the div tags
