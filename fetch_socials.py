import json
import os
import cloudscraper
import time
from bs4 import BeautifulSoup
from opensea_rankings_crawler import opensea_rankings_crawler




fast = opensea_rankings_crawler(my_proxy="s",url='cat',use_proxy=True)
fast.do_json()

with open("udata.json", "r") as f:
    dict = json.load(f)


stats = []
hcount = 0
ncount = 0
for key in dict:
    if dict[key]['hit']:
        hcount+=1
    else:
        ncount+=1
print (hcount,ncount)

scraper = cloudscraper.create_scraper()
county = 0
for key in dict:
    if dict[key]['hit']:
        continue
    url = "https://api.opensea.io/api/v1/collection/" + key + "?force_update=true&format=json"
    print (url)


    html = scraper.get(url, timeout=25).json()#.text.encode("utf-8") # #.text.encode("utf-8")
    #html = BeautifulSoup(html,'lxml')
    #print (html)
    with open("testing/" + key,"w") as f:
        json.dump(html,f)
    dict[key]['hit'] = 1
    dict[key]['data']['url'] = url
    with open("udata.json", "w") as f:
        json.dump(dict, f, indent=4)
    county+=1
    print (county, ' out of ', ncount)
    time.sleep(.7)