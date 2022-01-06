import requests
from bs4 import BeautifulSoup
newslist = []
useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
headers_ = {'User-Agent':useragent}
page = requests.get('https://yandex.ru', headers=headers_)
print(page.status_code)
print(page.text)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")
    allnews = soup.findAll('span',class_ = 'news__item-content')
    for d in allnews:
        newslist.append(d.text)
    print(newslist)
