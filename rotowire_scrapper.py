import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.rotowire.com/baseball/daily-lineups.php'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#print(results)
##First approach
Teams = soup.find_all('div', {'class': 'lineup__teams'})
Pitchers = soup.find_all('div', {'class': 'lineup__player-highlight-name'})

ERA = soup.find_all('div', {'class': 'lineup__player-highlight-stats'})
Batter = soup.find_all('li', {'class': 'lineup__player'})
Bat = [b.text.strip() for b in Batter]
Team = [t.text.strip() for t in Teams]
ERA1 = [t.text.strip() for t in ERA]


Pitch = [b.text.strip() for b in Pitchers]
P1 = [b.split('\n') for b in Pitch]
print(Pitch)

B1 = [b.split('\n') for b in Bat]
t1 = [t.split('\n') for t in Team]
E1 = [b.split('\n') for b in ERA1]

df2 = pd.DataFrame(B1)
df2.to_csv('Output2.csv')
df3 = pd.DataFrame(P1)
df3.to_csv('Pitchers.csv')
df4 = pd.DataFrame(t1)
df4.to_csv('Teams.csv')
df5 = pd.DataFrame(E1)
df5.to_csv('ERA.csv')
print(t1)
x = 36

t2 = []
#for z in range(len(B1)):
for i in range(len(B1)):
#    print(B1[i][1])
    t2.append(B1[i][1])

df = pd.DataFrame(t2, columns=['Name'])
df = df.drop_duplicates()

df_Player = pd.read_csv('PlayerLookup.csv')
df_Fanduel = pd.read_csv('FanDuel-MLB-2021-09-24.csv')


df = pd.merge(df, df_Player, how = 'left', left_on=['Name'], right_on=['Rotowire Name'])
df_Fanduel = pd.merge(df_Fanduel, df,  how='left', left_on=['Nickname'], right_on=['Full Name'])
print(df)
df.to_csv('Output.csv')
df_Fanduel.to_csv('Fanduel.csv')

