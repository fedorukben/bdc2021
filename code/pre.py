import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import axes
from matplotlib import gridspec as gridspec
from sklearn.cluster import KMeans
import seaborn as sns
import glbl as g
import cln

# df = pd.io.stata.read_stata('file.dta')
g.d['misinfo-type'] = pd.read_pickle("../data/pickle/misinfo-type.pkl")
g.d['twitter'] = pd.read_pickle('../data/pickle/twitter.pkl')
g.d['twitter-keyterm'] = pd.read_pickle('../data/pickle/twitter_keyterm.pkl')
g.d['reddit'] = pd.read_pickle('../data/pickle/reddit.pkl')
g.d['4chan'] = pd.read_pickle('../data/pickle/4chan.pkl')
g.d['twarc'] = pd.read_pickle('../data/pickle/twarc.pkl')
g.d['parler'] = pd.read_pickle('../data/pickle/parley.pkl')
g.d['twarc-keyterm'] = pd.read_pickle('../data/pickle/twarc-keyterms.pkl')
for sub in g.reddit_subs:
    g.d[f'reddit-{sub}'] = pd.read_pickle(f"../data/pickle/reddit-{sub}.pkl")
for board in g.fchan_boards:
    g.d[f'4chan-{board}'] = pd.read_pickle(f'../data/pickle/4chan-{board}.pkl')
print("Data successfully loaded.")

cln.remove_zero_compound('reddit')
for sub in g.reddit_subs:
    cln.remove_zero_compound(f'reddit-{sub}')
print("Data successfully cleaned.")

#fig = sns.histplot(data=g.d['twitter'], x='compound', bins=50, kde=True, hue='neg')
#fig = sns.scatterplot(data=g.d['twitter'], x='compound', y='words')
fig = sns.histplot(data=g.d['twitter-keyterm'], x='compound',
                   bins=25, kde=True, color=g.colors['twitter'])
#fig = sns.boxplot(g.d['reddit']['compound'])
fig.set(xlabel='compounded positivity score on [-1, 1]', 
        ylabel='frequency', 
        #title='Reddit r/movies Positivity vs. No. of Words',)
        title='Filtered COVID-19 Tweets\' Frequency of Positivity by Dataset')
print("Saving figure...")
plt.show()
#plt.savefig('../figs/parler/parler-hist.png')