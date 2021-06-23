import pandas as pd
import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import enchant
import demoji
from progressbar import ProgressBar
import re

df1 = pd.read_csv('../data/original/yt/GBcomments.csv', error_bad_lines=False, engine='python')
df2 = pd.read_csv('../data/original/yt/UScomments.csv', error_bad_lines=False, engine='python')

all_texts = set(pd.concat([df1, df2])['comment_text'].tolist())
print(f'{len(all_texts)=}')

pbar = ProgressBar()
sia = SentimentIntensityAnalyzer()
results = []
nltk.download('vader_lexicon')

print("Performing sentiment analysis...")
for line in pbar(all_texts):
    if not type(line) == type('hello'):
        continue
    if line == '' or line == np.nan or 'nan' in line:
        continue
    line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', demoji.replace_with_desc(line, ' ').lower())
    pol_score = sia.polarity_scores(line)
    if pol_score['compound'] == 0.0:
        continue
    pol_score['text'] = line
    print('h')
    results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

df.to_pickle('../data/pickle/youtube-all.pkl')
print("Saved combined file.")