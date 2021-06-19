import pandas as pd
import seaborn as sb
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import glbl as g

def clean_months():
    months = []
    for dt in g.d['status_created_at']:
        if 'Jan' in dt:
            months.append(1)
        elif 'Feb' in dt:
            months.append(2)
        elif 'Mar' in dt:
            months.append(3)
        elif 'Apr' in dt:
            months.append(4)
        elif 'May' in dt:
            months.append(5)
        elif 'Jun' in dt:
            months.append(6)
        elif 'Jul' in dt:
            months.append(7)
        else:
            print("Whoops!")
    g.d['month'] = months

def remove_zero_compound(key):
    g.d[key] = g.d[key][g.d[key]['compound'] != 0]

def pca(key):
    pca = PCA(2)
    g.d[key] = pca.fit_transform(g.d[key])

def compounds_df(keys, cols):
    dfs = []
    dct = dict()
    for key in keys:
        dfs.append(g.d[key])
    for i in range(len(dfs)):
        inner_lst = []
        for compound in dfs[i]['compound']:
            inner_lst.append(compound)
        dct[cols[i]] = inner_lst
    max_len = 0
    for lst in dct.values():
        #print(lst)
        if len(lst) > max_len:
            max_len = len(lst)
    #print(f'max_len: {max_len}')
    for lst in dct.values():
        for _ in range(max_len - len(lst)):
            lst.append(np.nan)
    return pd.DataFrame(dct)