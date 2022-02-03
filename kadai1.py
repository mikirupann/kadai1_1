import time

import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
response = requests.get(url)
results = response.json()

for i in results:
    url2 = f"https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty"
    reponse2 = requests.get(url2)
    results2 = reponse2.json()
    print(f"'title': {results2['title']}, 'link': {results2['url']}")
    time.sleep(1)  # ここで1秒止まる
