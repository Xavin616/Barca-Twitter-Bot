from main import bajeh_api, get_img
from scraper import get_article
import json, time

xorin = bajeh_api.get_user(screen_name="Lostbj")
print(xorin.name, '\n')

with open('art.json', 'r+') as prev:
    prv_art = dict(json.load(prev))

new = get_article()

while True:
    if prv_art != new:
        print('Posting New Article:', new['title'])
        tweet = f"{new[0]['title']}\nRead more:  {str(new[0]['link'])}\n #barcanews #barcabajeh"
        img = new[0]['image_url']
        bajeh_api.update_status_with_media(tweet, get_img(img))
        time.sleep(15)
    else: 
        print("News not updated yet!\nWaiting....")
        time.sleep(15)
        continue