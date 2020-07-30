
import json
import requests
import emailSender

# keywords to look for on the page
keywords = ["FREE", "100%", "99%", "98%", "97%", "96%", "95%", "94%", "93%", "92%", "91%", "90%", "$0.00", "$0.99", "$1.00"]

# the page that is to be searched
api_url = 'https://www.reddit.com/r/GameDeals.json'

# getting the page using a get request. A unique user-agent is required to acess the information consistently.
data = requests.get(api_url, headers = {'User-agent': 'UNIQUE NAME'})

# parsing the data as a json
pp = data.json()

dataToSend = {}
c = 0

# Each page on reddit has 25 posts hence the range is from 0 to 25
for i in range(0, 25):
    tmos = pp["data"]["children"][i]["data"]["title"]
    for j in range(0, len(keywords)):
        if keywords[j] in tmos:
            title = pp["data"]["children"][i]["data"]["title"]
            url = pp["data"]["children"][i]["data"]["url"]
            dataToSend[c] = title, url
            c += 1

emailSender.send(dataToSend)
