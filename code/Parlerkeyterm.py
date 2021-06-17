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

for index, harrisonisthebest in df.iterrows():
  # if "variant" in harrisonisthebest['text'].lower():
  #   for keyterm in ["british", "indian","uk","brazil","britain","u.k.","india","south africa","brazilian","african"]:
  for keyterm in key_terms:
    if keyterm not in harrisonisthebest["text"]: 
      df.drop(index)

df.to_pickle("Parler-name-filter.pkl")