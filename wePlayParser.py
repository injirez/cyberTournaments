from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time

linkDota = 'https://weplay.tv/ru/tournaments/dota2'


class WePlay:

	def __init__(self, link):

		chromeOptions = Options()
		# chromeOptions.add_argument('--headless')
		
		self.bot = webdriver.Chrome(r'C:\Projects\cyberTournaments\chromedriver.exe')

		self.link = link

	def parser(self):

		bot = self.bot
		wait = WebDriverWait(bot, 10)

		bot.get(self.link)
		# bot.maximize_window()

		for i in range(1, 10):
			title = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(i)))).text
			image = bot.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/a/div/img".format(i)).get_attribute('src')
			startTime = bot.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[2]/p".format(i)).text
			gameMode = bot.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[3]/p[1]/a".format(i)).text
			participant = bot.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[5]/p".format(i)).text
			reward = bot.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[6]/p".format(i)).text
			print(title, image, startTime, gameMode, participant, reward)

		

rod = WePlay(linkDota)
rod.parser()

# //*[@id="app"]/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/a/div/img