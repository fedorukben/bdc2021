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
g.d['parler-kw'] = pd.read_pickle('../data/pickle/Parler-name-bad-filter.pkl')
g.d['parler-sars'] = pd.read_pickle('../data/pickle/Parler-name-filter.pkl')
g.d['reddit-loc'] = pd.read_pickle('../data/pickle/Reddit-name-filter.pkl')
g.d['twitter-loc'] = pd.read_pickle('../data/pickle/Twitter-name-bad-filter.pkl')
g.d['twitter-bio'] = pd.read_pickle('../data/pickle/Twitter-name-good-filter.pkl')
g.d['reddit-all'] = pd.read_pickle('../data/pickle/reddit-all.pkl')
g.d['4chan-all'] = pd.read_pickle('../data/pickle/4chan-all.pkl')
g.d['twitter-all'] = pd.read_pickle('../data/pickle/twitter-all.pkl')
for sub in g.reddit_subs:
    g.d[f'reddit-{sub}'] = pd.read_pickle(f"../data/pickle/reddit-{sub}.pkl")
for board in g.fchan_boards:
    g.d[f'4chan-{board}'] = pd.read_pickle(f'../data/pickle/4chan-{board}.pkl')
print("Data successfully loaded.")

cln.remove_zero_compound('reddit')
for sub in g.reddit_subs:
    cln.remove_zero_compound(f'reddit-{sub}')
print("Data successfully cleaned.")


# SENTIMENT HISTOGRAM
fig = sns.histplot(data=g.d['4chan-all'], 
                   x='compound', 
                   bins=25, 
                   kde=True, 
                   color=g.colors['4chan'])

# WORDS SCATTER PLOT
#fig = sns.scatterplot(data=g.d['twitter'], x='compound', y='words')

# SENTIMENT BOX AND WHISKER PLOT
# fig = sns.boxplot(x="value", 
#                   y="variable", 
#                   data=pd.melt(cln.compounds_df(['parler', 'parler-kw'])),
#                   showmeans=True)

# SENTIMENT VIOLIN PLOT
# fig = sns.violinplot(y='value',
#                      x='variable',
#                      data=pd.melt(cln.compounds_df(['reddit-all', 'reddit-loc'], ['None', 'Locational Taxonomy'])),
#                      showmeans=True,
#                      inner="box",
#                      color=g.colors['reddit'])
fig.set(
        xlabel='compounded positivity score on [-1, 1]', 
        ylabel='frequency', 
        # xlabel='Filter',
        # ylabel='Compounded positivity score on [-1, 1]',
        #title='Reddit r/movies Positivity vs. No. of Words',)
        title='4chan Frequency of Positivity Combined')
        #title='Parler Box and Whisker')
        # title = 'Reddit Violin Plot')
print("Plotting figure...")
plt.show()