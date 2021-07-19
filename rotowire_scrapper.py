import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.rotowire.com/baseball/daily-lineups.php'
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.text, 'html.parser')
#soup.div_class
#print(soup)
#print(tag)
#results = soup.find('lineups')

#print(results)
##First approach
Teams = soup.find_all('div', {'class': 'lineup__teams'})
Pitchers = soup.find_all('div', {'class': 'lineup__player-highlight-name'})

ERA = soup.find_all('div', {'class': 'lineup__player-highlight-name'})
Batter = soup.find_all('li', {'class': 'lineup__player'})
#t1 = []
Bat = [b.text.strip() for b in Batter]
Team = [t.text.strip() for t in Teams]
#for t in Team:
#    t.rstrip('\n')
#    tt = t[:3]
#    tl = t[-3:]
    #print(tt)
 #   print(tl)
#    t1.append(tt)

B1 = [b.split('\n') for b in Bat]
t1 = [t.split('\n') for t in Team]


#print(B1)

#for b in B1:
#    print(b)
#print(B1[0][1])
print(t1)
x = 36
#print(len(B1))
t2 = []
#for z in range(len(B1)):
for i in range(len(B1)):
#    print(B1[i][1])
    t2.append(B1[i][1])

df = pd.DataFrame(t2, columns=['Name'])
df = df.drop_duplicates()

df_Player = pd.read_csv('PlayerLookup.csv')
df_Fanduel = pd.read_csv('FanDuel-MLB-2021-07-18.csv')


df = pd.merge(df, df_Player, how = 'left', left_on=['Name'], right_on=['Rotowire Name'])
df_Fanduel = pd.merge(df_Fanduel, df,  how='left', left_on=['Nickname'], right_on=['Full Name'])
print(df)
df.to_csv('Output.csv')
df_Fanduel.to_csv('Fanduel.csv')

#print(t1)
#print(Team)


#print(Bat)

#Second approach
#gameOdds = [g.text.strip() for g in oddsData]
#print(gameOdds)