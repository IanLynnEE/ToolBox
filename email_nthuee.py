# -*- coding: utf-8 -*-
# List all email addresses of professors from EE, NTHU.

import clipboard
# import requests
from bs4 import BeautifulSoup

# url = 'https://www.ee.nthu.edu.tw/iframe/list_teacher.php?type=ALL&col=2'
# soup = BeautifulSoup(requests.get(rul).text, 'lxml')
soup = BeautifulSoup(str(clipboard.paste()), 'lxml')

i = 0
for div in soup.find_all('div', class_='person-info'):
    for a in div.find_all('a'):
        if 'mailto' in a.get('href'):
            print(a.get_text(), end=', ')
            i += 1
print('Total:', i)

