
import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'https://leroymerlin.ru/product/kraska-vodno-dispersionnaya-cvet-belyy-2-5-kg-17664292/'

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
#       }

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

attributes = soup.find('table', {'class': 'about__params__table'})

print(attributes)


# with open('test.html', 'w') as output_file:
#     output_file.write(page.text.encode('cp1251'))