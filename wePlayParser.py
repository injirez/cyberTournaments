import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from addData import addData
import psycopg2
from datetime import datetime

linkDota = 'https://weplay.tv/ru/tournaments/dota2'

con = psycopg2.connect(
    host='localhost',
    database='cybertournaments',
    port='5432',
    user='rodionibragimov',
    password='3470')
cur = con.cursor()

class WePlay:

    def __init__(self, link):
        chromeOptions = Options()
        # chromeOptions.add_argument('--headless')

        self.bot = webdriver.Chrome(r'C:\Users\injir\Documents\cyberTournaments\chromedriver.exe')

        self.link = link

    def parser(self):
        bot = self.bot
        wait = WebDriverWait(bot, 10)

        bot.get(self.link)
        # bot.maximize_window()

        for i in range(1, 10):
            title = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(i)))).text
            status = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[2]/span".format(i)).text
            image = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/a/div/img".format(i)).get_attribute('src')
            startTime = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[2]/p".format(i)).text
            gameMode = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[3]/p[1]/a".format(i)).text
            participant = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[5]/p".format(i)).text
            reward = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[6]/p".format(i)).text
            siteName = title.split()
            link = bot.find_element_by_xpath(
                "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(
                    i)).get_attribute('href')
            print(title, status, startTime, gameMode, participant, reward, siteName[0], link, image)
            # addData(title, status, startTime, gameMode, participant, reward, siteName[0], link, image)
            # time.sleep(30)
            cur.execute(
                'insert into "Dota_dota" ("title", "status", "startTime", "gameMode", "participant", "reward", "siteName", "link", "dateTime", "img") values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (title, status, startTime, gameMode, participant, reward,
                 siteName[0], link,
                 datetime.now(), image))

            con.commit()

        cur.close()
        con.close()


rod = WePlay(linkDota)
rod.parser()

