from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from random import randint
import time

class Getpages:
	def __init__(self, driver):
		self.driver = driver
		self.driver.get('https://www.instagram.com/readersvibes')
		self.hrefs = []

	# 12 followers per scroll
	def get_num_flw(self):
		flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
		followers = sflw.findAll('span', {'class':'g47SY'})
		f = followers[1].getText().replace(',', '')
		if 'k' in f:
			f = float(f[:-1]) * 10**3
			return f
		elif 'm' in f:
			f = float(f[:-1]) * 10**6
			return f
		else:
			return float(f)

	# collect the target account's followers
	def get_followers(self):
		time.sleep(2)
		flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
		flw_btn.click()
		print('follow list opened')
		time.sleep(3)
		self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]')))  #'/html/body/div[5]/div/div/div[2]'
		for h in range(11):
			time.sleep(1)
			print('scrolling')
			print(h)
			print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)))
			self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
			if h == 5:
				break
		for i in range(100): # range = how many times it scrolls down to collect followers || 12 followers per scroll
			time.sleep(2)
			self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
		self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]')))  #same as above
		b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
		for p in b_popup.findAll('li', {'class': 'wo9IH'}):
			try:
				hlink = p.find_all('a')[0]['href']
				print(hlink)
				if 'div' in hlink:
					print('div found not adding to list')
				else:
					self.hrefs.append(hlink)
			except:
				pass
		return self.hrefs
			
				
	# check if the account is public
	def is_public(self):
		try:
			astate = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
			if astate.text == 'This Account is Private':
				return False
			else:
				return True
		except:
			return True


	# post 1 row 1
	def like_post(self):
		post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)')
		html = post.get_attribute('innerHTML')
		h = b(html, 'html.parser')
		href = h.a['href']
		self.driver.get('https://www.instagram.com' + href)
		like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
		like_btn.click()
		time.sleep(1)
		self.driver.back()
		time.sleep(randint(1,2))


	# post 2 row 1
	def like_post2(self):
		post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(2)')
		html = post.get_attribute('innerHTML')
		h = b(html,'html.parser')
		href = h.a['href']
		self.driver.get('https://www.instagram.com' + href)
		like_btn = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
		like_btn.click()
		time.sleep(1)
		self.driver.back()
		time.sleep(randint(1,2))
		

		# try:
		# 	post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(2)')
		# 	html = post.get_attribute('innerHTML')
		# 	h = b(html, 'html.parser')
		# 	href = h.a['href']
		# 	self.driver.get('https://www.instagram.com' + href)
		# 	like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
		# 	like_btn.click()
		# 	time.sleep(1)
		# 	self.driver.back()
		# 	time.sleep(randint(1,2))
		# except:
		# 	print('only one post.. movin on')
		# 	return
