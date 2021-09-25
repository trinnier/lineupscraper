import pandas as pd


df = pd.read_excel('FanDuel-NFL-2021-09-19.xlsx', 'FanDuel-NFL-2021-09-19')

dfRush = pd.read_csv('Rush.csv')
dfRush = dfRush[['Player', 'Yds', 'TD', 'Y/G']]

dfQB = pd.read_csv('NFL.csv')
dfQB = dfQB[['Player','Cmp%','Yds','TD','TD%','Y/G', 'QBR']]

dfRecieve = pd.read_csv('Recievers.csv')
dfRecieve = dfRecieve[['Player', 'Ctch%', 'Y/R', 'Yds', 'TD', 'R/G','Y/G']]

dfDefense = pd.read_csv('defense.csv')
dfDefense = dfDefense[['Tm', 'Yds', 'Y/P', 'TO%']]

df1 = pd.merge(df, dfRush, how = 'left',
              left_on = ['Nickname'], right_on=['Player'])

df2 = pd.merge(df, dfQB, how = 'left',
              left_on = ['Nickname'], right_on=['Player'])

df3 = pd.merge(df, dfRecieve, how = 'left',
              left_on = ['Nickname'], right_on=['Player'])

df4 = pd.merge(df, dfDefense, how = 'left',
              left_on = ['Nickname'], right_on=['Tm'])
dffinal = pd.DataFrame()
dffinal = dffinal.append(df1, ignore_index = True)
dffinal = dffinal.append(df2, ignore_index = True)
dffinal = dffinal.append(df3, ignore_index = True)
dffinal = dffinal.append(df4, ignore_index = True)
dffinal.to_csv('FD_Output.csv')
