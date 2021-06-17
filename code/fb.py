import pandas as pd
import facebook_scraper

search_term = 'c'
texts = []
for post in facebook_scraper.get_posts(search_term, cookies='../../fbcookies.json'):
    texts.append(post['text'])

print(texts)