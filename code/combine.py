import pandas as pd
import os


df1 = pd.read_csv('../data/original/yt/GBcomments.csv', error_bad_lines=False, engine='python')
df2 = pd.read_csv('../data/original/yt/UScomments.csv', error_bad_lines=False, engine='python')

pd.concat([df1, df2]).to_pickle('../data/pickle/youtube-all.pkl')
print("Saved combined file.")