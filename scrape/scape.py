import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)

links = soup.select('.titlelink')
votes = soup.select('.score')

print(votes)
