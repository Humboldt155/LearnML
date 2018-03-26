import requests
from bs4 import BeautifulSoup
import re

url = 'https://leroymerlin.ru/product/radiator-monlan-500-70-15052760/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
attributes = soup.find_all('table', {'class': 'about__params__table'})

rows = attributes[0].find_all('td')

for i in range(0, len(rows)):
    rows[i] = str(rows[i]).replace("  ", "")
    rows[i] = str(rows[i]).replace("<td>", "")
    rows[i] = str(rows[i]).replace("</td>", "")
    rows[i] = str(rows[i]).replace("\n", "")
    rows[i] = re.sub('<[^>]+>', ' ', rows[i])
    rows[i] = str(rows[i]).replace(" ? ", "")

oneDict = {}
for i in range(0, len(rows), 2):
    oneDict[rows[i]] = rows[i + 1]

for key in oneDict:
    print(key + " " + oneDict[key])
