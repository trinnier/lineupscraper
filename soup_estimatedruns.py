import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.fantasylabs.com/mlb/lineups/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)
