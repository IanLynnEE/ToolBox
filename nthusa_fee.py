# -*- coding: utf-8 -*-
# A lazy code to extract IDs from txt files.

import os
import csv

total = 0

os.chdir('txt')
out = open('output.csv', 'w')
writer = csv.writer(out)
writer.writerow(['ID', 'date', 'fee'])

file_name_list = sorted(os.listdir('.'))
for file_name in file_name_list:
    if 'txt' not in file_name:
        continue
    with open(file_name, 'r') as afile:
        text = afile.readlines()
    if len(text) < 1:
        continue
    day_sum = 0
    for row in text:
        try:
            id = row[15:24]
            date = row[24:30]
            fee = row[50:53]
            day_sum += int(fee)
            writer.writerow([id, date, fee])
        except:
            if day_sum != int(row[30:39]):
                print('Error in', file_name)
    total += day_sum
print('total =', total)
out.close()
