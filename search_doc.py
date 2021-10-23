# -*- coding: utf-8 -*-
# DNF

import os
import re
import subprocess

keys = ['調漲', '分攤']
os.chdir('./b/')

flag = 0

for filename in sorted(os.listdir()):
    if 'doc' not in filename:
        continue
    text = subprocess.check_output(['antiword', filename]).decode('utf-8')
    flag = 0
    for key in keys:
        if key in text:
            flag += 1
    if flag == len(keys):
        print(filename)

