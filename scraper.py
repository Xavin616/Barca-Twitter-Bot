import json
from bs4 import BeautifulSoup as bs
import requests as rq
import webbrowser

url = "https://barcablaugranes.com/"

def get_article() -> dict:
    res = rq.get(url)
    if res.status_code != 200: print("Not found")
    soup = bs(res.content, 'html.parser')
    articles = soup.select("[class~=c-entry-box--compact--article]")
    a = articles[0]
    title = a.select_one(".c-entry-box--compact__title")
    link = a.select_one(".c-entry-box--compact__image-wrapper")
    image = link.find("img")
    art = {
        'title': title.text,
        'link': link['href'],
        'image_url': image['src']
    }
    return art
        

if __name__ == "__main__":
    arts = [ i for i in get_article()]
    with open('art.json', 'w') as f:
        json.dump(arts[0], f, indent=4)
    print("Saved:", arts[0]['title'])