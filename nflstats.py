from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.pro-football-reference.com/years/2021/passing.htm'
# Open URL and pass to BeautifulSoup
html = urlopen(url)
stats_page = BeautifulSoup(html, features="lxml")
column_headers = stats_page.findAll('tr')[0]
column_headers = [i.getText() for i in column_headers.findAll('th')]

# Collect table rows
rows = stats_page.findAll('tr')[1:]
# Get stats from each row
qb_stats = []
for i in range(len(rows)):
  qb_stats.append([col.getText() for col in rows[i].findAll('td')])

# Create DataFrame from our scraped data
data = pd.DataFrame(qb_stats, columns=column_headers[1:])
# Rename sack yards column to `Yds_Sack`
new_columns = data.columns.values
new_columns[-6] = 'Yds_Sack'
data.columns = new_columns
data['Player'] = data['Player'].str.replace('*', '')
data['Player'] = data['Player'].str.replace('+', '')
data = data.dropna()
#print(data)
data.to_csv('NFL.csv')

#### Recievers Data
url2 = 'https://www.pro-football-reference.com/years/2021/receiving.htm'
html = urlopen(url2)
stats_page1 = BeautifulSoup(html, features="lxml")
#print(stats_page)
column_headers = stats_page1.findAll('tr')[0]
#print(column_headers)
column_headers = [i.getText() for i in column_headers.findAll('th')]
#print(column_headers)
# Collect table rows
rows = stats_page1.findAll('tr')[1:]
# Get stats from each row
recv_stats = []
for i in range(len(rows)):
  recv_stats.append([col.getText() for col in rows[i].findAll('td')])

Recievers = pd.DataFrame(recv_stats, columns=column_headers[1:])
Recievers['Player'] = Recievers['Player'].str.replace('*', '')
Recievers['Player'] = Recievers['Player'].str.replace('+', '')
Recievers = Recievers.dropna()
Recievers.to_csv('Recievers.csv')

url = 'https://www.pro-football-reference.com/years/2020/rushing.htm'
html = urlopen(url)
stats_page = BeautifulSoup(html, features="lxml")
column_headers = stats_page.findAll('tr')[1]
column_headers = [i.getText() for i in column_headers.findAll('th')]
print(column_headers)
# Collect table rows
rows = stats_page.findAll('tr')[1:]
#print(rows)
# Get stats from each row
rush_stats = []
for i in range(len(rows)):
  rush_stats.append([col.getText() for col in rows[i].findAll('td')])
  
Rush = pd.DataFrame(rush_stats, columns=column_headers[1:])
Rush['Player'] = Rush['Player'].str.replace('*', '')
Rush['Player'] = Rush['Player'].str.replace('+', '')
Rush = Rush.dropna()
Rush.to_csv('Rush.csv')

url = 'https://www.pro-football-reference.com/years/2021/opp.htm'
html = urlopen(url)
stats_page = BeautifulSoup(html, features="lxml")
column_headers = stats_page.findAll('tr')[1]
column_headers = [i.getText() for i in column_headers.findAll('th')]

# Collect table rows
rows = stats_page.findAll('tr')[1:]
# Get stats from each row
defense_stats = []
for i in range(len(rows)):
  defense_stats.append([col.getText() for col in rows[i].findAll('td')])

Defense = pd.DataFrame(defense_stats, columns=column_headers[1:])
#Defense['Player'] = Defense['Player'].str.replace('*', '')
#Defense['Player'] = Defense['Player'].str.replace('+', '')
Defense = Defense.dropna()
Defense.to_csv('defense.csv')






