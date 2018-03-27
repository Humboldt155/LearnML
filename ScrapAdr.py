import requests
from bs4 import BeautifulSoup
import re

url = 'https://leroymerlin.ru/catalogue/dvernye-ruchki-na-rozetke-bez-mehanizma/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
attributes = soup.find_all('p', {'class': 'catalog__name'})

print(soup)

