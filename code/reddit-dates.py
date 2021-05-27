import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()
before = int(dt.datetime(2020,1,1,0,0).timestamp())
after = int(dt.datetime(2021,5,25,0,0).timestamp())

sub = 'wallstreetbets'
limit = 500

comments = api.search_comments(subreddit=sub, limit=limit)

df = pd.DataFrame(comments)
df.head()

df.to_pickle('../data/pickle/wallstreetbets.pkl')
