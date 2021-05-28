import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import axes
from sklearn.cluster import KMeans
import seaborn as sns
import glbl as g
import cln

reddit_subs = [
    'covid',
    'prog',
    'ask',
    'politics',
    'movies',
    'kindness',
    'askdon',
    'atheist',
    'consp',
    'trumpspam',
]
fchan_boards = [
    'b',
    'pol',
    'r9k',
]

# df = pd.io.stata.read_stata('file.dta')
g.d['misinfo-type'] = pd.read_pickle("../data/pickle/misinfo-type.pkl")
g.d['twitter'] = pd.read_pickle('../data/pickle/twitter.pkl')
for sub in reddit_subs:
    g.d[f'reddit-{sub}'] = pd.read_pickle(f"../data/pickle/reddit-{sub}.pkl")
for board in fchan_boards:
    g.d[f'4chan-{board}'] = pd.read_pickle(f'../data/pickle/4chan-{board}.pkl')
print("Data successfully loaded.")

for sub in reddit_subs:
    cln.remove_zero_compound(f'reddit-{sub}')
print("Data successfully cleaned.")

#fig = sns.histplot(data=g.d['reddit-movies'], x='compound', bins=50, kde=True, hue='words', alpha=.7)
#fig = sns.scatterplot(data=g.d['reddit-ask'], x='compound', y='words')
fig = sns.histplot(data=g.d['twitter'], x='compound', bins=50, kde=True)
fig.set(xlabel='compounded positivity score on [-1, 1]', 
        ylabel='frequency', 
        #title='Reddit r/movies Positivity vs. No. of Words',)
        title='COVID-19-Related Tweets\' Frequency of Positivity')
print("Plotting figure...")
plt.show()