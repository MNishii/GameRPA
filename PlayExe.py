import pyautogui as pg
import time
import datetime
import pyperclip
import schedule
import itertools as it
import copy
import random
from Offence import *
from Deffence import *

# マウスの現在位置を取得
# print(pg.position())

# 天鳳アプリを開く
# pg.press('win')
# time.sleep(1)
# pyperclip.copy('天鳳 v1.3')
# pg.hotkey('ctrl','v')
# time.sleep(1)
# pg.press('enter')
# time.sleep(2)

# スクリーンショットを取って保存する。
def ScreenShot():
    now = datetime.datetime.now()
    time = now.strftime('%Y%m%d-%H%M%S')
    screen_shot = pg.screenshot() 
    screen_shot.save('screen_shot_web/output_{}.png'.format(time))

# 音を消す(天鳳の BGM 設定に対して)
def denoise():
    pg.moveTo(1455, 867)
    pg.click()
    time.sleep(1)
    pg.moveTo(1455, 815)
    pg.click()
    time.sleep(1)
    pg.moveTo(1455, 867)
    pg.click()
    time.sleep(1)
    pg.moveTo(1455, 849)
    pg.click()

# 鳴かないボタンをオン、ツモ切りボタンをオフにする Signal_1 Signal_3
def AutoButton1():
    # print(' ------------------ ')
    #  鳴かないボタンをオン、ツモ切りボタンをオフにする
    p = pg.locateOnScreen("./img_web/Nakanai.png", confidence=0.9)
    if p != None:
        pg.moveTo(917, 1010)
        pg.click()
        pg.moveTo(935, 790)
    p2 = pg.locateOnScreen("./img_web/Tumokiri.png", confidence=0.9)
    if p2 != None:
        pg.moveTo(787, 1010)
        pg.click()
        pg.moveTo(935, 790)
    p3 = pg.locateOnScreen("./img_web/PonPass.png", confidence=0.9)
    print(p3)
    if p3 != None:
        pg.moveTo(935, 785)
        pg.click()
        pg.moveTo(935, 790)
    q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
    # print(q)
    if q == None:
        pg.moveTo(1029, 944)
        pg.click()
        pg.moveTo(935, 790)

O = O_Execusion()
D = D_Execusion()

# 局が始まった最初の手牌認識＝配牌認識
# 局情報の条件追加する
# Initial = D.MyArrangement1(12, 892, 982, 106)
# print('配牌: ', Initial)


# denoise()
# schedule.every(1).seconds.do(AutoButton1)
# schedule.every(1).seconds.do(O.AutoButton2)
schedule.every(0.1).seconds.do(D.AutoButton2)
# schedule.every(3).seconds.do(D.DoraCheck)
# schedule.every(60).seconds.do(ScreenShot)

while True:
    schedule.run_pending()



