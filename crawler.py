from opensea_rankings_crawler import opensea_rankings_crawler

with open("cat_urls.txt","r") as f:
    cat_urls = [x.strip() for x in f.readlines()]
with open("proxies.txt","r") as f:
    proxy_stack = [x.strip() for x in f.readlines()]


# dirs data/listData





use_proxy = 0 #set this variable to 0 if you dont want to use proxies
scraped_urls = []

while True:
    for url in cat_urls:
        if url in scraped_urls:
           continue
        print(url)
        if not proxy_stack:
            with open("proxies.txt", "r") as f:
                proxy_stack = [x.strip() for x in f.readlines()]

        my_proxy = proxy_stack.pop(0)

        rankings_crawler = opensea_rankings_crawler(my_proxy,url,use_proxy )

        try:
            ret = rankings_crawler.doScrape()
            scraped_urls.append(url)
        except Exception as e:
            print ('Error')
            print (e)
    if len(scraped_urls) == len(cat_urls):
        break
