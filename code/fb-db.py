import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import enchant
import demoji
from progressbar import ProgressBar
import re

pbar = ProgressBar()

df_in = pd.read_pickle('../data/pickle/fb-db.pkl')

all_texts = df_in['status_message'].tolist()
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
    results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

print(df)

df.to_pickle('../data/pickle/fb-db.pkl')

print("Done!")