import requests
from bs4 import BeautifulSoup


def naver_news():
    url = 'https://m.news.naver.com/rankingList.nhn'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    select = soup.select('.commonlist_tx_headline')
    str = ''

    for title in select:
        str += title.text + " / "

    return str
