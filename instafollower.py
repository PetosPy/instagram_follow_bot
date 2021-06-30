from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "haraebm@gmail.com"
PASSWORD = "Rebelsie@29" 
FOLLOW_ACC = "pythonbrasil"
URL = "https://www.instagram.com/"


class InstaFollower:

	def __init__(self, driver_path):
		self.driver = webdriver.Chrome(executable_path=driver_path)
		self.driver.maximize_window()
		self.user_count = 0


	def login(self):
		self.driver.get(url=URL)
		self.username = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
		self.username.send_keys(EMAIL)
		self.password = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
		self.password.send_keys(PASSWORD)

		time.sleep(2)
		self.password.send_keys(Keys.ENTER)

		time.sleep(2)
		


	def find_followers(self):
		time.sleep(2)
		self.search_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
		self.search_bar.send_keys(FOLLOW_ACC)
		self.search_bar.send_keys(Keys.ENTER)
		self.select_account = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'))).click()
		# self.select_account.click()
		self.followers = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
		# self.followers.click()

	def follow(self):
		for x in range(0,100):

			self.follows = self.driver.find_elements_by_xpath(f'//li[{x}]//div[1]//div[3]//button[1]')
			for elem in self.follows:
				
				try:
					time.sleep(1)
					elem.click()
					self.user_count += 1
					print(self.user_count)
				except:
					already_following = self.driver.find_element_by_xpath("//button[normalize-space()='Cancel']")
					if already_following:
						already_following.click()
					else:
						continue

				else:
					continue



