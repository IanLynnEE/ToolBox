# -*- coding: utf-8 -*-
# Download video from provided webpage of iLMS.
# DNF

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import urllib.request


def Download_Document(driver):
    global Doc, Path
    try:
        block = driver.find_element_by_class_name('block')
        for item in block.find_elements_by_tag_name('a'):
            driver.switch_to.window(driver.window_handles[0])
            title = item.get_attribute('title')
            if title not in Doc:
                item.click()
                time.sleep(1)
                Doc.append(title)
                print('Download', title)
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
            return 0
    except NoSuchElementException:
        return 1

Path = ''
user = ''
password = ''
url = input('URL: ')
Doc = []
page = []

driver = webdriver.Safari()
driver.get(url)
time.sleep(2)

# Password
driver.find_element_by_id('loginAccount').send_keys(user)
driver.find_element_by_id('loginPasswd').send_keys(password)
check = driver.find_elements_by_xpath('//div[@class="mnuBody"]/div')[4]
check.find_elements_by_xpath('./input')[1].click()
time.sleep(2)

table = driver.find_element_by_class_name('table')
content = table.find_elements_by_class_name('Econtent')
for item in content:
    page.append(item.find_element_by_tag_name('a').get_attribute('href'))

try:
    for nUrl in page:
        driver.get(nUrl)
        print(nUrl)
        time.sleep(2)
        if Download_Document(driver) == 1:
            try:
                title = driver.find_element_by_class_name('title').text
                article = driver.find_element_by_class_name('article')
                video = article.find_element_by_tag_name('video')
                vUrl = video.get_attribute('src')
                urllib.request.urlretrieve(vUrl, Path + title)
            except NoSuchElementException:
                print('Nothing Found!')
finally:
    driver.quit()
