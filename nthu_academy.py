# -*- coding: utf-8 -*-
# Get titles and links from NTHU Academic website.

import sys
import time
import requests
from bs4 import BeautifulSoup

endPage = sys.argv[1]

for page in range(1, endPage+1, 1):
    if page:
        time.sleep(5)
    url = f'http://academic.site.nthu.edu.tw/p/403-1007-1504-{page}.php'
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'lxml')
    # print('Working on page', page)

    target = soup.find('div', id = 'pageptlist')
    for div in target.find_all('div', class_ = 'mtitle'):
        date = div.find('i').string
        text = div.find('a').string.strip()
        href = div.find('a').get('href')
        print(date, text, href, sep='; ')

