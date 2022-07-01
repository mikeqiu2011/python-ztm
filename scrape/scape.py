import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)

links = soup.select('.titlelink')
votes = soup.select('.score')


def create_custom_hackernews(links, votes):
    hn = []
    for idx, item in enumerate(links):
        # title = links[idx].getText()
        title = item.getText()
        href = item.get('href', None)
        points = int(votes[idx].getText().split(' ')[0])
        if points >= 100:
            hn.append({
                'title': title,
                'link': href,
                'points': points
            })

    return hn


hacker_news = create_custom_hackernews(links, votes)

print(hacker_news)
