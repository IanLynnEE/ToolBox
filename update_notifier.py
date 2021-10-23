# -*- coding: utf-8 -*-
# Check and notify update of a website every minute.
# macOS only. It is recommended to install terminal-notifier first.

import os
import platform     # Check macOS
import shutil       # Check terminal-notifier
import time
import requests
from bs4 import BeautifulSoup

def notify(title, text, url=None, sound='default'):
    if shutil.which('terminal-notifier') == None:
        os.system('''
            osascript -e 'display notification "{}" with title "{}" sound name "{}"'
        '''.format(text, title, sound))
    elif url == None:
        os.system('''
            terminal-notifier -title '{}' -message '{}' -sound '{}'
        '''.format(title, text, sound))
    else:
        os.system('''
            terminal-notifier -title '{}' -message '{}' -open '{}' -sound '{}'
        '''.format(title, text, url, sound))
    return

def main(url, limit):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'lxml')
    body = soup.find('body')

    if os.path.isfile('temp.html'):
        with open('temp.html', 'r') as f:
            old = f.read()
    else:
        print('First time visit! Creating file...')
        old = str(body)
        with open('temp.html', 'w') as f:
            f.write(str(body))

    for i in range(limit):
        print(f'{limit-i:4d} minutes till session end.' % (limit-i), end='\r')
        time.sleep(60)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        body = soup.find('body')
        if old != str(body):
            notify('New Content Found!', 'The web page has updated.', url)
            print('New Content Found! Ending session...')
            with open('temp.html', 'w') as f:
                f.write(str(body))
            return
    notify('Nothing Found...', f'Session ends after {limit} minutes.')
    print(f'Nothing Found. Session ends after {limit} minutes.')
    return

def check_platform():
    if platform.system() != 'Darwin':
        print('The program is design for macOS only.', 
                'Modifing source code is necessary for linux.')
        return 1
    return 0



if __name__ == '__main__':
    if check_platform():
        os._exit(1)
    print('The program will check any update of a website every minute.')
    url = input('Target: ')
    limit = int(input('Session minutes: '))
    main(url, limit)

