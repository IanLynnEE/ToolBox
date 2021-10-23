# -*- coding: utf-8 -*-
# Download large file from takefile with Raspberry Pi.
# DNF

import os
import time
from shutil import which
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

input('Please use screen since download might stop after session end.')
url = input('URL: ')

driver_path = '/usr/lib/chromium-browser/chromedriver'  	# For pi
options = Options()
options.add_argument('window-size=704,480')
options.add_argument("--headless")

# https://stackoverflow.com/questions/45631715
# https://stackoverflow.com/questions/57599776
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(driver_path, options=options)
params = {'behavior': 'allow', 'downloadPath': '/home/pi/Downloads'}
result = driver.execute_cdp_cmd('Page.setDownloadBehavior', params)


try: 
	print('Opening the page, please wait.')
	driver.get(url)
	time.sleep(5)

	print('Finding download button...')
	try:
		driver.find_element_by_id('downloadbtn').click()
	except:
		print(driver.find_element_by_class_name('err').text)
		driver.save_screenshot('TakefileError.png')
		print('Cannot free download.')
		os._exit(0)

	print('Waiting for download (60s)...')
	time.sleep(65)
	driver.find_element_by_id('downloadbtn').click()

	print('Waiting for link...')
	time.sleep(10)
	driver.save_screenshot('TakefileLog.png')
	try:	
		driver.find_element_by_xpath('//center/span/a').click()
	except:
		pass
	print('Download should start!')	
	input('Press any key to end after download finished.')

finally:
    driver.quit()

