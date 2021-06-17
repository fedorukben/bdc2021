# credits to Anarov for improved example
from __future__ import print_function
import basc_py4chan
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import re
import os
from progressbar import ProgressBar
import warnings
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def clean_comment(comment):
    c1 = re.sub('http://\S+|https://\S+', '', comment)
    c2 = BeautifulSoup(c1, 'lxml').text
    if c2[:2] == ">>":
        c3 = c2[11:]
    else:
        c3 = c2
    c4 = re.sub('>', '', c3)
    return c4.lower()

warnings.filterwarnings('ignore')
pbar = ProgressBar()
nltk.download('vader_lexicon')

# get the board we want
board = basc_py4chan.Board('b')

# select the first thread on the board
all_thread_ids = board.get_all_thread_ids()
# first_thread_id = all_thread_ids[0]
# thread = board.get_thread(first_thread_id)

titles = []
comments = []
datetimes = []
names = []
ids = []
is_ops = []
print(f"Scraping data from \\{board.name}\\...")
for thread_id in pbar(all_thread_ids):
    thread = board.get_thread(thread_id)
    try:
        title = thread.topic.comment


        # file information
        for post in thread.posts:
            comments.append(clean_comment(post.comment))
            #comments.append(post.comment)
            datetimes.append(post.datetime)
            names.append(post.name)
            is_ops.append(post.is_op)
            ids.append(post.post_id)
            titles.append(title)
    except:
        continue

# tuples = list(zip(titles, comments, datetimes, names, ids, is_ops))

# df = pd.DataFrame(tuples, columns=['title', 'comment', 'datetime', 
#                                    'name', 'id', 'is_op'])

results = []
texts = set(comments).union(set(titles))

keywords = ['wuhanvirus','chinavirus','chinese lab virus', 'wuflu', 'kung flu']
clean_text1 = set()

for text in texts: 
  for keyword in keywords:
    if keyword in text: 
      clean_text1.add(text)
print(len(clean_text1))

good_keywords = ['covid-19','covid','sars-cov-2']
clean_text2 = set() 

for text in texts: 
  for keyword in good_keywords:
    if keyword in text:  
      clean_text2.add(text)
print(len(clean_text2))

# print("Performing sentiment analysis...")
# for line in texts:
#   pol_score = sia.polarity_scores(line)
#   if pol_score['compound'] == 0.0:
#       continue
#   pol_score['text'] = line
#   results.append(pol_score)

# df = pd.DataFrame.from_records(results)
# df['label'] = 0
# df.loc[df['compound'] > 0.1, 'label'] = 1
# df.loc[df['compound'] < -0.1, 'label'] = -1

# if os.path.isfile(f'../data/pickle/4chan-{board.name}.pkl'):
#     last_df = pd.read_pickle(f'../data/pickle/4chan-{board.name}.pkl')
#     concat_df = pd.concat([df, last_df])
#     df_no_dupl = df.drop_duplicates()

#     df_no_dupl.to_pickle(f'../data/pickle/4chan-{board.name}.pkl')
# else:
#     df.to_pickle(f'../data/pickle/4chan-{board.name}.pkl')

# print("Done!")
