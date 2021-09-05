from celery import shared_task
from .models import Dota, Reward, GameMode, SiteName, Link
from django.db import IntegrityError

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




@shared_task
def addDota():
    # print("Hello")
    linkDota = 'https://weplay.tv/ru/tournaments/dota2'
    bot = webdriver.Chrome(r'C:\Users\injir\Documents\cyberTournaments\chromedriver.exe')
    wait = WebDriverWait(bot, 10)

    bot.get(linkDota)
    # bot.maximize_window()

    for i in range(1, 10):
        title = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(
                                                           i)))).text
        status = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[2]/span".format(i)).text
        image = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/a/div/img".format(
                i)).get_attribute('src')
        startTime = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[2]/p".format(i)).text
        gameMode = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[3]/p[1]/a".format(i)).text
        participant = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[5]/p".format(i)).text
        reward = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[6]/p".format(i)).text
        siteName = title.split()

        if reward == 'Уважение':
            reward = 0
            currency = 0
            typeReward = 0
        elif reward != 'Уважение':
            reward = reward.split()
            typeReward = (reward[1] + ' ' + reward[2]).replace('(', '').replace(')', '')
            reward = reward[0].replace('$', '')
            currency = '$'



        link = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(
                i)).get_attribute('href')



        print(title, status, startTime, gameMode, participant, reward, siteName[0], link, image, currency, typeReward)
        siteNameObject = SiteName.objects.get(name='WePlay')
        gameModeObject = GameMode.objects.get(mode=gameMode)

        try:
            rewardObject = Reward.objects.create(type=typeReward, count=reward, currency=currency)
            # gameModeObject = GameMode.objects.create(mode=gameMode)
            linkObject = Link.objects.create(image=image, tournament=link)
            newObject = Dota.objects.create(title=title, status=status, startTime=startTime, gameMode=gameModeObject, participant=participant, reward=rewardObject, siteName=siteNameObject, links=linkObject, ip='127.0.0.1')
        except IntegrityError:
            print("Updating row...")
            Dota.objects.filter(title=title).update(status=status, participant=participant)
    bot.quit()
    return True

