import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import cln
import glbl as g

# df = pd.io.stata.read_stata('file.dta')
g.d['misinfo-type'] = pd.read_csv('../data/misinfo-type.csv')

# plt.show()