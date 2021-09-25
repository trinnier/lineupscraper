import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.rotowire.com/baseball/daily-lineups.php'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#print(soup.prettify())

print(list(soup.children))

print([type(item) for item in list(soup.children)])
