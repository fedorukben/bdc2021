# credits to Anarov for improved example
from __future__ import print_function
import basc_py4chan
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import re
from progressbar import ProgressBar
import warnings

def clean_comment(comment):
    c1 = re.sub('http://\S+|https://\S+', '', comment)
    c2 = BeautifulSoup(c1, 'lxml').text
    return c2

warnings.filterwarnings('ignore')
pbar = ProgressBar()

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

tuples = list(zip(titles, comments, datetimes, names, ids, is_ops))

df = pd.DataFrame(tuples, columns=['title', 'comment', 'datetime', 
                                   'name', 'id', 'is_op'])
df.to_pickle('4chan-b.pkl')