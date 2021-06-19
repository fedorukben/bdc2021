import pandas as pd

lst = []

lst.append(pd.read_pickle('../data/pickle/twitter.pkl'))
lst.append(pd.read_pickle('../data/pickle/twarc.pkl'))
print("Gathered data.")

pd.concat(lst).to_pickle('../data/pickle/twitter-all.pkl')
print("Saved combined file.")