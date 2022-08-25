# opensea.io scraper/crawler

collects data from opensea.io/rankings
requirements cloudscraper/bs4
python version 3.8

Very barebones scraper i threw together, suggest using proxies.


# Step 1)
run crawler.py

This will download/save realtime data collected from all urls found in the cat_urls.txt file
 
 



# Step 2)
run fetch_socials.py

note not sure if i'm just lucky or if opensea doesn't care if u hit this endpoint much, 
but i didn't have to use proxies ;v
Script will cycle through all names found from step 1
hitting this api endpoint
https://api.opensea.io/api/v1/collection/<<NAMEHERE>>?force_update=true&format=json


 

 

Saves all data into testing/ folder 
one file per user (they are really big)



# Step 3)
run read_testing_disect.py
 
read data play around ^
 

Random keys of interest found
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



