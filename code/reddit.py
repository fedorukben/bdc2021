import urllib.request
import json 
import datetime
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pprint import pprint
from IPython import display

nltk.download('vader_lexicon')
sb.set(style='darkgrid', context='talk', palette='Dark2')

def load_results(lower_bound_timestamp, upper_bound_timestamp, target_result_size, target_subreddit, score_threshold):
  headline_collection = set()
  reddit_data_url = f'https://api.pushshift.io/reddit/submission/search/?after={lower_bound_timestamp}&before={upper_bound_timestamp}&sort_type=score&sort=desc&subreddit={target_subreddit}&size={target_result_size}&score={score_threshold}'

  try:
    with urllib.request.urlopen(reddit_data_url) as url:
      data = json.loads(url.read().decode())
      for submission in data['data']:
        headline_collection.add(submission['title'])
    return headline_collection
  except urllib.error.HTTPError as e:
    print(e.__dict__)
    return set()
  except urllib.error.URLError as e:
    print(e.__dict__)
    return set()

headlines = set()
time_now = datetime.datetime.now()
limit_delta = 365
limit_lower_delta = 360
subreddit = "COVID"
result_size = 1000
score_limit = ">1"

for i in range(0, 100):
  previous_timestamp = int((time_now - datetime.timedelta(days=limit_delta)).timestamp())
  current_timestamp = int((time_now - datetime.timedelta(days=limit_lower_delta)).timestamp())
  full_collection = load_results(previous_timestamp, current_timestamp, result_size, subreddit, score_limit)
  headlines = headlines.union(full_collection)
  limit_delta = limit_delta - 5
  limit_lower_delta = limit_lower_delta - 5
  display.clear_output()
  print(f"Cycle {i}")
  print(len(headlines))

sia = SentimentIntensityAnalyzer()
results = []
for line in headlines:
  pol_score = sia.polarity_scores(line)
  pol_score['headline'] = line
  results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1
print(df.head(10))

df.to_pickle("../data/pickle/reddit-covid.pkl")
