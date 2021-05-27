import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import axes
from sklearn.cluster import KMeans
import seaborn as sns
import glbl as g
import cln

# df = pd.io.stata.read_stata('file.dta')
g.d['misinfo-type'] = pd.read_pickle("../data/pickle/misinfo-type.pkl")
g.d['reddit-covid'] = pd.read_pickle("../data/pickle/reddit-covid.pkl")
g.d['reddit-prog'] = pd.read_pickle("../data/pickle/reddit-prog.pkl")
g.d['reddit-ask'] = pd.read_pickle("../data/pickle/reddit-ask.pkl")
g.d['reddit-politics'] = pd.read_pickle('../data/pickle/reddit-politics.pkl')
g.d['reddit-movies'] = pd.read_pickle('../data/pickle/reddit-movies.pkl')
g.d['reddit-kindness'] = pd.read_pickle('../data/pickle/reddit-kindness.pkl')
g.d['reddit-askdon'] = pd.read_pickle('../data/pickle/reddit-askdon.pkl')
g.d['reddit-atheist'] = pd.read_pickle('../data/pickle/reddit-atheist.pkl')
g.d['reddit-consp'] = pd.read_pickle('../data/pickle/reddit-consp.pkl')
g.d['reddit-trumpspam'] = pd.read_pickle('../data/pickle/reddit-trumpspam.pkl')
print("Data successfully loaded.")

to_remove_zero_compounds = ['reddit-prog', 'reddit-covid', 
                            'reddit-ask', 'reddit-politics', 'reddit-movies',
                            'reddit-kindness', 'reddit-askdon', 'reddit-atheist',
                            'reddit-consp', 'reddit-trumpspam']
for label in to_remove_zero_compounds:
    cln.remove_zero_compound(label)
print("Data successfully cleaned.")

#fig = sns.histplot(data=g.d['reddit-movies'], x='compound', bins=50, kde=True, hue='words', alpha=.7)
#fig = sns.scatterplot(data=g.d['reddit-ask'], x='compound', y='words')
fig = sns.histplot(data=g.d['reddit-prog'], x='compound', bins=50, kde=True)
fig.set(xlabel='compounded positivity score on [-1, 1]', 
        ylabel='frequency', 
        #title='Reddit r/movies Positivity vs. No. of Words',)
        title='Reddit r/programming Frequency of Positivity')
print("Plotting figure...")
plt.show()