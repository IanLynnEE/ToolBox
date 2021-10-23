# -*- coding: utf-8 -*-
# To check if any deps can be removed.
# Use `diff brew_installed.txt brew_deps.txt | vim -R -` to check.

import os

testlist = [
    'automake', 'ffmpeg', 'imagemagick', 
    'opencv', 'pyqt', 'vim', 'youtube-dl'
]

whitelist = ['cmake', 'cpulimit', 'gnu-sed', 'ocrad', 'pandoc', 'wget']

for formula in testlist:
    os.system(f'brew deps {formula} >> temp.txt')
os.system('brew list --formula > brew_installed.txt')

with open('./temp.txt', 'r') as f:
    lines = f.read().splitlines()
deps = set(lines)

deps.update(testlist)
deps.update(whitelist)

with open('./brew_deps.txt', 'w') as f:
    for item in sorted(deps):
        f.write(item)
        f.write('\n')

os.remove('./temp.txt')
