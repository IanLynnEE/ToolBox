# -*- coding: utf-8 -*-
# Download all meeting minutes from Division of Student Housing, NTHU.
# DNF

import requests
from bs4 import BeautifulSoup
import re
import os

websites = {}
target = 'http://sthousing.site.nthu.edu.tw'

source = requests.get('http://sthousing.site.nthu.edu.tw/p/412-1254-3482.php?Lang=zh-tw')
soup = BeautifulSoup(source.text, 'lxml')
for div in soup.find_all('div', class_='mtitle'):
    a = div.find('a')
    year = a.get_text().strip()
    year = int( re.search('\d+', year).group() )
    websites[year] = a.get('href')


for key in websites.keys():
    os.mkdir(str(key))
    os.chdir(str(key))
    sub_source = requests.get(websites[key])
    sub_soup = BeautifulSoup(sub_source.text, 'lxml')
    for td in sub_soup.find_all('td'):
        # Some td have no link
        try:
            a = td.find('a')
            href = target + a.get('href')
            title = href.split('/')[-1]
            # Some files cannot download
            try:
                doc = requests.get(href)
                with open(title, 'wb') as f:
                    f.write(doc.content)
                print(title)
            except:
                print('Fail: ' + title)
        except:
            pass
    os.chdir('..')

