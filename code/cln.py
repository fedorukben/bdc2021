import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import glbl as g

def clean():
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