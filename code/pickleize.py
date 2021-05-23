import pandas as pd
import os
import filecmp

def pickleize(name, cols):
    df = pd.read_csv(f'../data/original/{name}.csv')
    df = df[cols]
    df.to_pickle(f'../data/pickle/temp.pkl')
    if filecmp.cmp(f'../data/pickle/temp.pkl', f'../data/pickle/{name}.pkl'):
        print(f'Skipping {name}, as it is already up to date.')
        os.remove(f'../data/pickle/temp.pkl')
        return
    os.remove(f'../data/pickle/{name}.pkl')
    os.rename(f'../data/pickle/temp.pkl', f'../data/pickle/{name}.pkl')
    print(f"Pickle-ized {name}.")


pickleize('misinfo-type', ['status_created_at', 'annotation1'])