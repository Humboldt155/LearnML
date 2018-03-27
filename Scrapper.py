import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import re

import pandas as pd

urls = pd.read_csv(open('URL Адреса для теста.csv', 'r'), delimiter=';')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

#

listAll = []

ind = 0

for row in urls.itertuples():
    ind += 1
    if ind > 20: break
    dep = str(row[1])
    model = str(row[2])
    code = str(row[3])
    url_lm = row[4]
    url_bitrix_step = row[5]

    page_lm = requests.get(url_lm, headers=headers, verify=False)
    page_bitrix_step = requests.get(url_bitrix_step, headers=headers, auth=HTTPBasicAuth('greensight', 'greensight'),
                                    verify=False)

    soup_lm = BeautifulSoup(page_lm.content, 'html.parser')
    soup_bitrix_step = BeautifulSoup(page_bitrix_step.content, 'html.parser')

    attributes_lm = soup_lm.find_all('table', {'class': 'about__params__table'})
    attributes_bitrix_step = soup_bitrix_step.find_all('table', {'class': 'about__params__table'})

    rows_lm = attributes_lm[0].find_all('td')
    rows_bitrix_step = attributes_bitrix_step[0].find_all('td')

    maxLines = max(len(rows_lm), len(rows_bitrix_step))

    attrDict = {}

    for i in range(0, len(rows_lm)):
        rows_lm[i] = str(rows_lm[i]).replace("<td>", "")
        rows_lm[i] = str(rows_lm[i]).replace("</td>", "")
        rows_lm[i] = str(rows_lm[i]).replace("\n", "")
        rows_lm[i] = str(rows_lm[i]).replace("  ", "")
        rows_lm[i] = re.sub('<[^>]+>', ' ', rows_lm[i])
        rows_lm[i] = str(rows_lm[i]).replace(" ? ", "")

    for i in range(0, len(rows_bitrix_step)):
        rows_bitrix_step[i] = str(rows_bitrix_step[i]).replace("<td>", "")
        rows_bitrix_step[i] = str(rows_bitrix_step[i]).replace("</td>", "")
        rows_bitrix_step[i] = str(rows_bitrix_step[i]).replace("\n", "")
        rows_bitrix_step[i] = str(rows_bitrix_step[i]).replace("  ", "")
        rows_bitrix_step[i] = re.sub('<[^>]+>', ' ', rows_bitrix_step[i])
        rows_bitrix_step[i] = str(rows_bitrix_step[i]).replace(" ? ", "")

    for i in range(0, len(rows_lm), 2):
        attrDict[rows_lm[i]] = [rows_lm[i], rows_lm[i + 1], '', '']

    for i in range(0, len(rows_bitrix_step), 2):
        if rows_bitrix_step[i] in attrDict:
            attrDict[rows_bitrix_step[i]][2] = rows_bitrix_step[i]
            attrDict[rows_bitrix_step[i]][3] = rows_bitrix_step[i+1]
        else:
            attrDict[rows_bitrix_step[i]] = ['', '', rows_bitrix_step[i], rows_bitrix_step[i+1]]


    for attr in attrDict:
        listAll.append([dep, model, code, attrDict[attr][0], attrDict[attr][1], attrDict[attr][2], attrDict[attr][3]])

for row in listAll:
    print(row)
