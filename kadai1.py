import time

import requests


def news_add():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(url)
    results = response.json()[0:30]
    for i in results:
        url2 = f"https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty"
        reponse2 = requests.get(url2)
        results2 = reponse2.json()
        try:
            print(f"'title': {results2['title']}, 'link': {results2['url']}")
            time.sleep(1)  # ここで1秒止まる
        except KeyError:
            pass


def main():
    news_add()


if __name__ == '__main__':
    main()
