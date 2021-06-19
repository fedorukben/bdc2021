import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import axes
from matplotlib import gridspec as gridspec
from sklearn.cluster import KMeans
import seaborn as sns
import glbl as g
import cln

"""

g.d = {
    '4chan': pd.read_pickle("../data/pickle/4chan.pkl"),
    'twitter': pd.read_pickle("../data/pickle/twitter.pkl"),
}

"""

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
g.d['reddit-all'] = pd.read_pickle('../data/pickle/reddit-all.pkl')
g.d['4chan-all'] = pd.read_pickle('../data/pickle/4chan-all.pkl')
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
fig = sns.histplot(data=g.d['reddit-all'], 
                   x='compound', 
                   bins=25, 
                   kde=True, 
                   color=g.colors['reddit'])

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
#                      data=pd.melt(cln.compounds_df(['parler', 'parler-kw', 'parler-sars'], ['None', 'Locational Taxonomy', 'Biological Taxonomy'])),
#                      showmeans=True,
#                      inner="box",
#                      color=g.colors['parler'])
fig.set(
        xlabel='compounded positivity score on [-1, 1]', 
        ylabel='frequency', 
        # xlabel='Filter',
        # ylabel='Compounded positivity score on [-1, 1]',
        #title='Reddit r/movies Positivity vs. No. of Words',)
        title='Parler Frequency of Positivity Filtered by Locational Taxonomy')
        #title='Parler Box and Whisker')
        # title = 'Parler Violin Plot')
print("Plotting figure...")
plt.show()