import requests

url = "https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty"
response = requests.get(url)
results = response.json()
list = []
for i in results:
    print(i['kids'])
