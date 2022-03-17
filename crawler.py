import requests
from bs4 import BeautifulSoup


def get_artists(url):
    ret = []
    r= requests.get(url)
    body= r.content
    soup= BeautifulSoup(body, features="html.parser")
    tracklist=soup.find("table",{"class":"tracklist"})

    links=tracklist.find_all("a")
    for i in links:
        ret.append((i.text, i['href']))
    return ret
    
def crawl():
    # r=requests.get("https://www.songlyrics.com/a")
    # body=r.content
    # print(body)
    artists= get_artists("https://www.songlyrics.com/a/")
    for name,link in artists:
        print(name, "  : ",link)
 

if __name__ =="__main__":
    crawl()
