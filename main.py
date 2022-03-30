from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from random import randint
import time
import login
import getpages

username = ' '
password = ' '
driver = 0
refs = []
max_likes = 20		# total account restrictions for run_bot and trigger for timer
max_follows = 0


def main():
	global driver
	print('running script..')
	driver = webdriver.Chrome('D:\Python\chromedriver_win32\chromedriver.exe')
	l = login.Login(driver, username, password)
	l.signin()
	print('signin successful!')
	gp = getpages.Getpages(driver)
	#gp.get_followers()
	refs = gp.get_followers()
	print(gp.get_num_flw())
	run_bot(refs, driver, gp)

	L = 0  # how many pages were liked in one round of 25 accounts. Will reset after sleep.
	TL = 0  # grand Total of Likes in the whole sequence. Does not reset.
	TA = 0  # grand Total of Accounts liked in the whole sequence. Does not reset.

	for r in refs:
		driver.get('https://www.instagram.com' + r)
		time.sleep(2)
		if gp.get_num_flw() < 3000:
			if gp.is_public():
				if L < max_likes:
					#print('\n')
					try:
						gp.like_post()
						L += 1
						TL += 1
						TA += 1
						try:
							gp.like_post2()
							TL += 1
						except:
							print('*only one post*')

						print('\nideal account found:   ' + str(r))
						print("SUCCESS: " + str(L) + ' of 25')
						print('---------------------------------')
						print('Grand total Accounts: \t' + str(TA))
						print('Grand total Likes: \t' + str(TL))
						print('---------------------------------\n\n')
						list = open("accounts_liked.txt","a")  # record liked accounts in text file
						list.write(str(r) + "\n")
					except:
						print('could not like... moving on')
				else:
					# testing 6 hours = 21600  ||  2 hours = 7200  ||  5 minutes = 300 || ideal? -> 6 hours = 21600
					amount = 21600
					print('\nLimit reached! Sleeping for ' + str(amount / 60) + ' minutes.\n')
					time.sleep(amount)
					#reset 25 of 25 to 0, then like current profile
					L = 0;
					try:
						gp.like_post()
						L += 1
						TL += 1
						TA += 1
						try:
							gp.like_post2()
							TL += 1
						except:
							print('*only one post*')

						print('ideal account found:   ' + str(r))
						print("SUCCESS: " + str(L) + ' of 25')
						print('---------------------------------')
						print('Grand total Accounts: \t' + str(TA))
						print('Grand total Likes: \t' + str(TL))
						print('---------------------------------\n')
						list = open("accounts_liked.txt","a")  # record liked accounts in text file
						list.write(str(r) + "\n")
					except:
						print('could not like... moving on')
			else:
				print('account is private... moving on')
				time.sleep(randint(2,5))
		else:
			print('account has over 3K followers... moving on')



def run_bot(refs, driver, gp):
	print(len(refs))
	print('accounts targeted')





if __name__ == '__main__':
	main()	

