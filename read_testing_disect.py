import os
import json
import unicodecsv
from opensea_rankings_crawler import opensea_rankings_crawler

data = {}

files = os.listdir("testing/")

dict_keys = (['editors',
              'payment_tokens',
              'primary_asset_contracts',
              'traits',
              'stats',
              'banner_image_url',
              'chat_url',
              'created_date',
              'default_to_fiat',
              'description',
              'dev_buyer_fee_basis_points',
              'dev_seller_fee_basis_points',
              'discord_url',
              'display_data',
              'external_url',
              'featured',
              'featured_image_url',
              'hidden',
              'safelist_request_status',
              'image_url',
              'is_subject_to_whitelist',
              'large_image_url',
              'medium_username',
              'name',
              'only_proxied_transfers',
              'opensea_buyer_fee_basis_points',
              'opensea_seller_fee_basis_points',
              'payout_address',
              'require_email',
              'short_description',
              'slug',
              'telegram_url',
              'twitter_username',
              'instagram_username',
              'wiki_url',
              'is_nsfw'])

total_skip = 0
skip = 0
for file in files:
    with open("testing/" + file, 'r') as f:
        dict = json.load(f)
    #print (file)

    try:
        dict = dict['collection']
    except:
        print(file)

        continue
    #print ( dict['name'])
    #print(dict.keys())

    keys = ['name','instagram_username','twitter_username','telegram_url','discord_url','medium_username','external_url','editors','stats','image_url','banner_image_url','description']# ,'payout_address']

    nft = {}
    if not dict['stats']['total_sales']:
        continue
    total_skip+=1


    if not dict['external_url']:
        continue
    print ("Yay found external_url !! => ", dict['external_url'])
    skip+=1

    #if not dict['image_url']:
    #    continue
    #else:
    #    print (dict['image_url'])

    for key in keys:
        if dict[key]:
            #print (key, dict[key])
            #print (key,'._=> ',dict[key])


            nft[key] = dict[key]
            #print( 'https://medium.com/@'+dict[key].rstrip())
        else:
            nft[key] = ''

    nft['slug'] = file
    nft['opensea_url'] = "https://opensea.io/collection/" + file
    data[file] = nft

with open("ztest.json","w") as f:
    json.dump(data,f)
    f.close()


print (skip,total_skip, ' out of ',len(files))
print (len(data))

