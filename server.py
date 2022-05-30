from main import bajeh_api, get_img
from scraper import get_article
import json, time

xorin = bajeh_api.get_user(screen_name="Lostbj")
print(xorin.name, '\n')

while True:
    new = get_article()

    with open('art.json', 'r+') as prev:
        prv_art = dict(json.load(prev))

    print("New: ", new['title'])
    print("Previuos: ", prv_art['title'])
    
    if prv_art['title'] != new['title']:
        print('Posting New Article:', new['title'])
        tweet = f"{new['title']}\nRead more:  {str(new['link'])}"
        img = new['image_url']
        bajeh_api.update_status_with_media(tweet, get_img(img))
        with open('art.json', 'w') as f:
            json.dump(new, f, indent=4)
        print("Added new article to json file.\n\nWaiting....")
        time.sleep(600)
    else: 
        print("News not updated yet!\nWaiting....")
        time.sleep(600)
        continue