import requests
from bs4 import BeautifulSoup
newslist = []
page = requests.get('https://rambler.ru')
print(page.status_code)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")
    allnews = soup.findAll('a',class_ = '_2j90')
    for d in allnews:
        newslist.append(d.text)
    print(newslist)
