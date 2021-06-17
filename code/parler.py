import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import demoji
from progressbar import ProgressBar

pbar = ProgressBar()

print('Loading external dependencies...')
nltk.download('vader_lexicon')
demoji.download_codes()

print('Reading data...')
df = pd.read_json('../data/original/parler.ndjson', lines=True, nrows=500000)

print("Cleaning data...")
parleys_unclean = set(df['body'].tolist())
parleys_w_emoji = parleys_unclean - set([''])

parleys = set()
for parley in pbar(parleys_w_emoji):
    parleys.add(demoji.replace_with_desc(str(parley), ' '))

for parley in parleys:
  for kw in keywords:
    if not kw in parley:
      parleys.remove(parley)
    
sia = SentimentIntensityAnalyzer()
results = []

print("Performing sentiment analysis...")
for parley in parleys:
  pol_score = sia.polarity_scores(str(parley))
  if pol_score['compound'] == 0.0:
      continue
  pol_score['text'] = str(parley)
  results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

df.to_pickle('../data/pickle/parley.pkl')

print("Done!")