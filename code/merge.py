import pandas as pd
import glbl as g

# Importing
for sub in g.reddit_subs:
    g.d[f'reddit-{sub}'] = pd.read_pickle(f"../data/pickle/reddit-{sub}.pkl")
for board in g.fchan_boards:
    g.d[f'4chan-{board}'] = pd.read_pickle(f'../data/pickle/4chan-{board}.pkl')

# Concating
reddits = [g.d[f'reddit-{sub}'] for sub in g.reddit_subs]
reddit_df = pd.concat(reddits)

fchans = [g.d[f'4chan-{board}'] for board in g.fchan_boards]
fchan_df = pd.concat(fchans)

# Pickling
reddit_df.to_pickle('../data/pickle/reddit.pkl')
fchan_df.to_pickle('../data/pickle/4chan.pkl')