""" Command Line Emailer

This program takes an email address and string of text from the CL and then,
using Selenium, logs into your email account and sends an email of the string
to the provided address.

You need to install chromedriver for selenium to work, and this script works
only with outlook emails. Change <your email> and <your password> to your email
and password respectively.

Usage:
    python Emailer.py <emailTo> <text>
"""

from selenium import webdriver
import sys, time

if len(sys.argv) != 3:
    print("Usage: python Emailer.py <emailTo> <text>")
    sys.exit()

driver = webdriver.Chrome()
driver.get('https://outlook.live.com')
elem = driver.find_element_by_class_name('buttonLargeBlue')
elem.click()
elem = driver.find_element_by_xpath("//input[@type='email']")
elem.send_keys("<your email>")
elem = driver.find_element_by_xpath("//input[@value='Next']")
elem.click()
elem = driver.find_element_by_xpath("//input[@type='password']")
elem.send_keys("<your password>")
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@value='Sign in']")
elem.click()
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//i[@data-icon-name='Add']")
elem.click()
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@type='text']")
elem.send_keys(sys.argv[1])
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@id='subjectLine0']")
elem.send_keys('Example')
driver.implicitly_wait(100)
elem = driver.find_element_by_xpath("//div[@dir='ltr']")
elem.send_keys(sys.argv[2])
driver.implicitly_wait(100)
elem = driver.find_element_by_xpath("//i[@data-icon-name='Send']")
elem.click()
driver.implicitly_wait(100)
elem = driver.find_element_by_xpath("//div[@title='Account']")
elem.click()
elem = driver.find_elements_by_xpath("//div[contains(text(), 'Sign out')]")
time.sleep(4)
elem[0].click()