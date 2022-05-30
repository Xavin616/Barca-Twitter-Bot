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
        tweet = f"{new['title']}\nRead more:  {str(new['link'])}"
        img = new['image_url']
        bajeh_api.update_status_with_media(tweet, get_img(img))
        with open('art.json', 'w') as f:
            json.dump(new, f, indent=4)
        print("Added new article to json file.\n\nWaiting....")
        time.sleep(900)
    else: 
        print("News not updated yet!\nWaiting....")
        time.sleep(900)
        continue