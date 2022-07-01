import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://news.ycombinator.com/news'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)

links = soup.select('.titlelink')
# votes = soup.select('.score') # some links have no score, but all have subtext
subtexts = soup.select('.subtext')


def create_custom_hackernews(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        # title = links[idx].getText()
        title = item.getText()
        href = item.get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().split(' ')[0])
            if points >= 100:
                hn.append({
                    'title': title,
                    'link': href,
                    'points': points
                })

    return hn


hacker_news = create_custom_hackernews(links, subtexts)

pprint.pprint(hacker_news)
