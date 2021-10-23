# -*- coding: utf-8 -*-
# Download large file from gigapeta with Raspberry Pi.

import os
import time
from shutil import which
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

if which('img2txt.py') is None:
    print('Please run "pip3 install img2txt.py" first.')
    os._exit(0)

input('Please use screen since download might stop after session end.')
user = input('User: ')
password = input('Password: ')
url = input('URL: ')

driver_path = '/usr/lib/chromium-browser/chromedriver'  # For pi
options = Options()
options.add_argument('window-size=700,300')
options.add_argument("--headless")

# https://stackoverflow.com/questions/45631715
# https://stackoverflow.com/questions/57599776
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(driver_path, options=options)
params = {'behavior': 'allow', 'downloadPath': '/home/pi/Downloads'}
result = driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
# print('Headless download mode:', result)





try: 
	print('Opening the page, please wait.')
	driver.get(url)
	time.sleep(5)		# I am lazy.

	print('Trying to login...')
	login = driver.find_element_by_xpath('//input[@name="auth_login"]')
	passwd = driver.find_element_by_xpath('//input[@name="auth_passwd"]')
	login.send_keys(user)
	passwd.send_keys(password)
	passwd.send_keys(Keys.ENTER)

	print('Waiting for captcha...')
	time.sleep(15)
	driver.get_screenshot_as_file('captcha.png')
	img = driver.find_element_by_css_selector('#captcha td img')
	driver.execute_script('document.body.style.zoom = "700%";')
	driver.execute_script('arguments[0].scrollIntoView(true);', img)
	driver.get_screenshot_as_file('captcha.png')
	os.system('img2txt.py captcha.png --ansi')

	code = input('Please enter captcha: ')
	code_box = driver.find_element_by_xpath('//input[@name="captcha"]')
	code_box.send_keys(code)
	code_box.send_keys(Keys.ENTER)

	print('Checking download status...')
	time.sleep(2)
	driver.execute_script('document.body.style.zoom = "100%";')
	driver.execute_script('window.scrollTo(0,0)')
	# driver.maximize_window()
	driver.get_screenshot_as_file('download_status.png')
	try:
		error = driver.find_element_by_id('page_error').text
		print(error)
	except:
		print('Download should start!')
		# os.system('img2txt.py download_status.png --ansi')

	input('Press any key to end after download finished.')

finally:
    driver.quit()

