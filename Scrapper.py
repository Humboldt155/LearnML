import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import re

import pandas as pd

urls = pd.read_csv('urls.csv', header=None)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}


for row in urls.itertuples():
    dep = str(row[1])
    url = str(row[2])

    page = requests.get(url, headers=headers, auth=HTTPBasicAuth('greensight', 'greensight'), verify=False)

    soup = BeautifulSoup(page.content, 'html.parser')
    attributes = soup.find_all('table', {'class': 'about__params__table'})

    rows = attributes[0].find_all('td')

    for i in range(0, len(rows)):
        rows[i] = str(rows[i]).replace("<td>", "")
        rows[i] = str(rows[i]).replace("</td>", "")
        rows[i] = str(rows[i]).replace("\n", "")
        rows[i] = str(rows[i]).replace("  ", "")
        rows[i] = re.sub('<[^>]+>', ' ', rows[i])
        rows[i] = str(rows[i]).replace(" ? ", "")

    oneDict = {}
    for i in range(0, len(rows), 2):
        oneDict[rows[i]] = rows[i + 1]

    for key in oneDict:
        print(dep + " " + key + " " + oneDict[key])

