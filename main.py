
import json
import requests
import emailSender

keywords = ["FREE", "100%", "99%", "98%", "97%", "96%", "95%", "94%", "93%", "92%", "91%", "90%", "$0.00", "$0.99", "$1.00"]

api_url = 'https://www.reddit.com/r/GameDeals.json'

data = requests.get(api_url, headers = {'User-agent': 'your bot v0.1'})
pp = data.json()

dataToSend = {}
c = 0

for i in range(0, 25):
    tmos = pp["data"]["children"][i]["data"]["title"]
    for j in range(0, len(keywords)):
        if keywords[j] in tmos:
            title = pp["data"]["children"][i]["data"]["title"]
            url = pp["data"]["children"][i]["data"]["url"]
            dataToSend[c] = title, url
            c += 1

emailSender.send(dataToSend)