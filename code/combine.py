import pandas as pd
import os

files = os.listdir('../../../../Downloads/fb/data')
print(files)
print("Gathered data.")

lst = []
for file in files:
	if not file == 'datahuffingtonpost_facebook_statuses.csv':
		lst.append(pd.read_csv(f'../../../../Downloads/fb/data/{file}'))

pd.concat(lst).to_csv('../data/pickle/fb.csv')
print("Saved combined file.")