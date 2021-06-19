import pandas as pd
import re
import os
from progressbar import ProgressBar
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
sia = SentimentIntensityAnalyzer()

pbar = ProgressBar()

df = pd.read_pickle(r"C:\Users\Kai Fucile Ladouceur\.vscode\Code\bdc2021\data\pickle\reddit-all.pkl")
# print(df['headline'][278].tolist()[-1])
# number_of_entries = df.shape[0] - 5 # subtracted 5 to deal with index errors
df2 = pd.DataFrame()
key_terms = ["china flu","wuflu","china virus","wuhan virus", "kungflu","wuhan","lab leak"]
for index, harrisonisthebest in df.iterrows():
  if "variant" in harrisonisthebest['headline'].lower():
    for keyterm in ["british", "indian","uk","brazil","britain","u.k.","india","south africa","brazilian","african"]:
      if keyterm in harrisonisthebest['headline'].lower():
        df2 = pd.concat([df2, harrisonisthebest.to_frame().T])
        # print(type(harrisonisthebest))


print(df2)