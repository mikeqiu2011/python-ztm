import requests
from bs4 import BeautifulSoup
import pprint


def get_links_subtexts(home_url, pages):
    links = []
    subtexts = []
    for i in range(pages):
        res = requests.get(f'{home_url}{i}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links.append(soup.select('.titlelink'))
        subtexts.append(soup.select('.subtext'))

    flat_links = sum(links, [])
    flat_subtexts = sum(subtexts, [])

    return flat_links, flat_subtexts


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda x: x['points'], reverse=True)


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

    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    url = 'https://news.ycombinator.com/news?p='
    links, subtexts = get_links_subtexts(url, 3)

    hacker_news = create_custom_hackernews(links, subtexts)

    pprint.pprint(hacker_news)
