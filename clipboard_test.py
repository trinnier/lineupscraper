import pandas as pd

df = pd.read_excel('FanDuel-MLB-2021-08-21.xlsx', 'FD')
dfOwn = pd.read_clipboard(sep='\s+')

dfOwn.to_csv('Own.csv')
