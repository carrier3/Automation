from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Login:
	def __init__(self, driver, username, password):
		self.driver = driver
		self.username = username
		self.password = password
	def signin(self):
		print('opening')
		self.driver.get('https://www.instagram.com/accounts/login')
		# insert cookie message click
		uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
		uid.click()
		uid.send_keys(self.username)
		print('username entered')
		pswd = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
		pswd.click()
		pswd.send_keys(self.password)
		print('password entered')
		btn = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
		btn.click()
		time.sleep(5)




#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input

#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input

#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)

