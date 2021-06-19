import pandas as pd
import re
import os
from progressbar import ProgressBar
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
sia = SentimentIntensityAnalyzer()

pbar = ProgressBar()

df = pd.read_pickle(r"C:\Users\Kai Fucile Ladouceur\.vscode\Code\bdc2021\data\pickle\parley.pkl")
# print(df['headline'][278].tolist()[-1])
# number_of_entries = df.shape[0] - 5 # subtracted 5 to deal with index errors
key_terms = ["china flu","wuflu","china virus","wuhan virus", "kungflu","wuhan","lab leak"]

df["text"] = df['text'].str.lower()
df.reset_index()
#test out seeing if using sars-cov-2 and scientific names have reduced negative sentiment when compared to just using covid or covid 19

df3 = pd.DataFrame()

for index, harrisonisthebest in df.iterrows():
   for keyterm in key_terms:
    if keyterm in harrisonisthebest['text'].lower():
      df3 = pd.concat([df3, harrisonisthebest.to_frame().T])

print(df3)
df3['compound'] = pd.to_numeric(df3['compound'])
df3['pos'] = pd.to_numeric(df3['pos'])
df3['neg'] = pd.to_numeric(df3['neg'])
df3['neu'] = pd.to_numeric(df3['neu'])
df3['label'] = pd.to_numeric(df3['label'])
print(df3.info())
df3.to_pickle(r"C:\Users\Kai Fucile Ladouceur\.vscode\Code\bdc2021\data\pickle\Parler-name-filter.pkl")