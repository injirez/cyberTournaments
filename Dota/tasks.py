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
def addDotaWeplay():
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
        reward = reward.split()

        if reward == 'Уважение':
            reward = 0
            currency = 0
            typeReward = 0
        elif reward != 'Уважение':
            if len(reward) > 2:
                # reward = reward.split()
                typeReward = (reward[1] + ' ' + reward[2]).replace('(', '').replace(')', '')
                reward = reward[0].replace('$', '')
                currency = '$'
            else:
                # reward = reward.split()
                typeReward = 'Деньги'
                reward = reward[0]
                currency = reward[1]



        link = bot.find_element_by_xpath(
            "//*[@id='app']/div/main/div[1]/div/div/div/div[2]/table/tbody/tr[{}]/td[1]/div/div/a".format(
                i)).get_attribute('href')



        print(title, status, startTime, gameMode, participant, reward, 'WePlay', link, image, currency, typeReward)
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


@shared_task
def addDotaGamelix():
    linkDota = 'https://gamelix.com/dota-2/tournaments/1'
    bot = webdriver.Chrome(r'C:\Users\injir\Documents\cyberTournaments\chromedriver.exe')
    wait = WebDriverWait(bot, 10)

    # bot.get(linkDota)
    # bot.maximize_window()

    for i in range(1, 10):
        bot.get(linkDota)
        title = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]/div/div[1]/p".format(
                                                           i)))).text

        status = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]/div/div[5]/div/h4".format(i)).text
        image = "https://static-prod.weplay.tv/2020-09-06/w-2048/webp/973eedcbdec2f381fe92fd9199987288.120D2F-B20834-0AB9E4.jpeg"

        gameMode = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]/div/div[2]/p/span".format(i)).text
        participant = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]/div/div[3]/p".format(i)).text
        reward = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]/div/div[4]/span".format(i)).text

        siteName = 'GameLix'
        typeReward = 'Деньги'
        reward = reward.split()
        reward = reward[0]
        currency = reward[1]


        # if reward == 'Уважение':
        #     reward = 0
        #     currency = 0
        #     typeReward = 0
        # elif reward != 'Уважение':
        #     reward = reward.split()
        #     typeReward = (reward[1] + ' ' + reward[2]).replace('(', '').replace(')', '')
        #     reward = reward[0].replace('$', '')
        #     currency = '$'



        link = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/a[{}]".format(
                i)).get_attribute('href')
        bot.get(link)
        startTime = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div[2]/div/div[2]/p".format(i)).text
        startTime = startTime.split()
        startTime = startTime[3] + ' ' + startTime[4]




        print(title, status, startTime, gameMode, participant, reward, siteName, link, image, currency, typeReward)

        siteNameObject = SiteName.objects.get(name='GameLix')
        if gameMode == '1x1':
            gameModeObject = GameMode.objects.get(mode='1v1')
        elif gameMode == '5x5':
            gameModeObject = GameMode.objects.get(mode='5v5')

        try:
            rewardObject = Reward.objects.create(type=typeReward, count=reward, currency=currency)
            linkObject = Link.objects.create(image=image, tournament=link)
            newObject = Dota.objects.create(title=title, status=status, startTime=startTime, gameMode=gameModeObject, participant=participant, reward=rewardObject, siteName=siteNameObject, links=linkObject, ip='127.0.0.1')
        except IntegrityError:
            print("Updating row...")
            Dota.objects.filter(title=title).update(status=status, participant=participant)

    bot.quit()
    return True

