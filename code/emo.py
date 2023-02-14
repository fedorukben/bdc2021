import pandas as pd
import text2emotion as te

df = pd.read_pickle('../data/pickle/parler.pkl')['text']

emos = []
for i,t in enumerate(df.tolist()):
    emo = te.get_emotion(t)
    emos.append(emo)
    if i % 1 == 0:
        print(i)