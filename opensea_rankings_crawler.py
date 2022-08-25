import cloudscraper
from bs4 import BeautifulSoup
import json
import datetime
import os


class opensea_rankings_crawler():
    def __init__(self, my_proxy,url,use_proxy):
        self.url = "https://opensea.io/rankings"
        self.url = url
        self.scraper = cloudscraper.create_scraper()
        self.my_proxy = my_proxy
        self.use_proxy = use_proxy

        try:
            os.mkdir("listData")
            print ("Created dir => listData/")
        except:
            pass
        try:
            os.mkdir("data")
            print ("Created dir => data/")
        except:
            pass

        try:
            os.mkdir("testing")
            print ("Created dir => testing/")
        except:
            pass

    def do_json(self):
        files = os.listdir("listData")
        stack = set()
        for file in files:
            with open("listData/" + file, 'r') as f:
                temp = [x.strip() for x in f.readlines()]
            for x in temp:
                stack.add(x)

        try:
            with open("udata.json", "r") as f:
                dict = json.load(f)
        except Exception as e:
            print(e)
            print("Making fresh udata.json")
            with open("udata.json", "w") as f:
                f.write("{}")
                f.flush()
                f.close()
            with open("udata.json", "r") as f:
                dict = json.load(f)

        onStack = dict.keys()
        newTargets = []

        for target in stack:
            if not target in onStack:
                newTargets.append(target)
                dict[target] = {
                    "hit": 0,
                    "data": {}
                }

        with open("udata.json", "w") as f:
            json.dump(dict, f, indent=4)


    def gen_proxy_stubs_noauth(self,proxy):
        'generates useable proxy stubs for requests'
        temp_proxy_data = []

        skelly = {'https': 'http://', 'http': 'http://'}
        proxy_ip = proxy.split(":")[0]
        proxy_port = proxy.split(":")[1]

        p_build = proxy_ip + ":" + proxy_port
        skelly['https'] += p_build
        skelly['http'] += p_build

        # temp_proxy_data.append(skelly)
        # return temp_proxy_data

        return skelly

    def doScrape(self):
        # fetch proxy here

        if self.use_proxy:
            proxy_stub = self.gen_proxy_stubs_noauth(self.my_proxy)
            print (proxy_stub)

            self.scraper.proxies = proxy_stub
        html = self.scraper.get(self.url, timeout=25).text.encode("utf-8") # #.text.encode("utf-8")
        with open("last_html.html","wb") as f:
            f.write(html)

        html = BeautifulSoup(html,'lxml')


        # will break if 404 page
        script = html.find("script",id="__NEXT_DATA__")
        #print (script)




        json_object = json.loads(script.contents[0])
        stubs =  json_object['props']['relayCache']
        print (len(stubs))

        stack = set()
        for stub in stubs:
            for x in range(0,1000):
                stack.add(stub[1]['json']['data']['rankings']['edges'][x]['node']['slug'])
            print (len(stack))





        # save data
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        with open("data/" + filename + ".json","w") as f:
            json.dump(stubs,f,indent=4)
        print ("wrote => ", "data/" + filename + ".json")

        # do output list data here
        with open("listData/" + filename + ".txt","w") as f:
            for name in stack:
                f.write(name+"\n")
        print("wrote =>","listData/" + filename + ".txt")
        return True








