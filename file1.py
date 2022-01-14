import requests
from bs4 import BeautifulSoup
def findnews(inwebaddress,newstag, newsclass):
    newslist = []
    useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    headers_ = {'User-Agent':useragent}
    page = requests.get(inwebaddress, headers=headers_)
    print(f'-----> connect to resource {inwebaddress} status {page.status_code}')
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        allnews = soup.findAll(newstag,class_ = newsclass)
        for d in allnews:
            newslist.append(d.text)
        return newslist
    else:
        return [-1]

print(findnews('https://msn.com','span','title'))
print(findnews('https://yandex.ru','span','news__item-content'))
