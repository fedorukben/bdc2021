import pandas as pd
import enchant
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

keywords = ['bioweapon', 'china virus', 'wuhan virus', 'fake news', 'microchip']
nltk.download('vader_lexicon')
df = pd.read_json('../data/twarc/covid.jsonl', lines=True)
all_texts = df['full_text'].tolist()
print(len(all_texts))

eng_texts = []
total_texts = len(all_texts)
curr_iter = 0
for text in all_texts:
    curr_iter += 1
    number_english_words = 0
    number_words = 0
    print(f"Cleaning {curr_iter} of {total_texts}...")
    for kw in keywords:
        if not kw in text:
            continue
    for word in text.split()[2:]:
        number_words += 1
        if enchant.Dict('en_US').check(word):
            number_english_words += 1
    if number_words == 0:
        continue
    pct_english = float(number_english_words) / number_words
    if pct_english >= 0.5:
        eng_texts.append(text)

texts = set(eng_texts)
sia = SentimentIntensityAnalyzer()
results = []

print("Performing sentiment analysis...")
for line in texts:
  pol_score = sia.polarity_scores(line)
  if pol_score['compound'] == 0.0:
      continue
  pol_score['text'] = line
  results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

df.to_pickle('../data/pickle/twarc-keyterms.pkl')

print("Done!")