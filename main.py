import tweepy
import requests as rq
import shutil

consumer_key = "AKyXbv6IAPfUn9WEwPbe6oRZq" 
consumer_secret = "fi5LeH0vxhWsFMSx3ODfTPLe1BrvdzimONftXqQmFXp0Xg90jd"

b_access_token = "1417598308630007810-cqss2rp5y34TXEYJ3DmthWpAfzxdCu"
b_access_secret = "pPARpIWF1OnXNPg8BmqA3Wnf6zAYmYZP9AnGdOt59KSiS"

bauth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, b_access_token, b_access_secret)
bajeh_api = tweepy.API(bauth)

def get_img(url) -> str:
    res = rq.get(url, stream=True)
    if res.status_code == 200:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print("Downloaded", filename)
        return filename
    else: 
        print("An error occurred")
