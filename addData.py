from celery import shared_task

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# con = psycopg2.connect(
#     host='localhost',
#     database='cybertournaments',
#     port='5432',
#     user='rodionibragimov',
#     password='3470')
# cur = con.cursor()
#
# def addData(title, status, startTime, gameMode, participant, reward, siteName, link, img):
#     cur.execute(
#         'insert into "Dota_dota" ("title", "status", "startTime", "gameMode", "participant", "reward", "siteName", "link", "dateTime", "img") values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
#         (title, status, startTime, gameMode, participant, reward,
#          siteName, link,
#          datetime.now(), img))
#
#     con.commit()
#
#     cur.close()
#     con.close()

def addDotaCmode():
    linkDota = 'https://www.challengermode.com/dota2/tournaments?state=upcoming'
    bot = webdriver.Chrome(r'C:\Users\injir\Documents\cyberTournaments\chromedriver.exe')
    wait = WebDriverWait(bot, 10)

    for i in range(1, 10):
        bot.get(linkDota)

        tournamentLink = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[{}]/span/div/div/a".format(
                                                           i)))).get_attribute('href')
        # imageLink = bot.find_element_by_xpath(
        #     "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div[{}]/div/div/div[1]/div/div[1]/div/div/div/a/div/div/div/img".format(i)).get_attribute('href')
        imageLink = 'https://static-prod.weplay.tv/2020-09-06/w-2048/webp/973eedcbdec2f381fe92fd9199987288.120D2F-B20834-0AB9E4.jpeg'
        bot.get(tournamentLink)
        time.sleep(5)
        try:
            title = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/h1"))).text
        except NoSuchElementException:
            title = bot.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/h1").text
        status = "Будущий"
        startTime = "HUI"
        gameMode = bot.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[3]/div/div[2]/span[2]/span/span").text
        participantReg = bot.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[4]/div/div/div/div[2]/div[2]/div[1]/div[2]/a/div/div/div[2]/div[2]/span").text
        participantAll = bot.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[4]/div/div/div/div[2]/div[2]/div[1]/div[2]/a/div/div/div[3]/div[2]/span").text
        participant = participantReg + '/' + participantAll
        countReward = bot.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[5]/div/div[2]/span[2]/span/span").text.replace(
            '€', '')
        countReward = countReward.split('.')
        countReward = countReward[0]
        countReward = countReward.split()
        countReward = countReward[0]
        name = 'ChallengerMode'
        gameMode = gameMode.split(' ')
        gameMode = gameMode[0]
        if countReward.isalpha():
            countReward = 0
            currencyReward = 0
            typeReward = 0
        else:
            typeReward = 'Деньги'
            currencyReward = '€'

        print(title, status, startTime, gameMode, participant, countReward, name, tournamentLink, imageLink,
              currencyReward, typeReward)

        # siteNameObject = SiteName.objects.get(name='ChallengerMode')
        # gameModeObject = GameMode.objects.get(mode=gameMode)
        #
        # try:
        #     rewardObject = Reward.objects.create(type=typeReward, count=countReward, currency=currencyReward)
        #     linkObject = Link.objects.create(image=imageLink, tournament=tournamentLink)
        #     newObject = Dota.objects.create(title=title, status=status, startTime=startTime, gameMode=gameModeObject,
        #                                     participant=participant, reward=rewardObject, siteName=siteNameObject,
        #                                     links=linkObject, ip='127.0.0.1')
        #
        # except IntegrityError:
        #     print("Updating row...")
        #     Dota.objects.filter(title=title).update(status=status, participant=participant)

addDotaCmode()