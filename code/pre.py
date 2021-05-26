import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import cln
import glbl as g

# df = pd.io.stata.read_stata('file.dta')
g.d['misinfo-type'] = pd.read_csv('../data/original/misinfo-type.csv')
g.d['social-algos'] = pd.read_csv('../data/original/social-algos.csv')


# plt.show()