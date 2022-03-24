import pyautogui as pg
import time
import datetime
import pyperclip
import schedule
import itertools as it
import copy
import random

# BOX の Left 値の差分を取る。
def isMatch(box1, box2):
    a, b, c, d = box1
    e, f, g, h = box2
    return abs(e - a)

# locateAllOnScreen 機能での重複を排除
def BoxValue(boxlist):
    if len(boxlist) == 1:
        return boxlist
    elif len(boxlist) >= 2:
        for i, j in list(it.combinations(boxlist, 2)):
            # print('Candidates: ', i, j)
            if isMatch(i, j) <= 10 and j in boxlist:
                boxlist.remove(j)
        return boxlist

class O_Execusion():
    def __init__(self):
        self.flg = None
        self.MyArrangement = []
        self.Name = None
        self.Tumo = None
        self.Hou = []
        self.ReachState = 0
        self.Member = 0
        self.TiToi = 0
        self.SortRule = None
        self.SortRule2 = None
        self.SortRule3 = None
        self.HeadCheckList = None

        self.Name = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                    '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                    'E',  'S',  'We', 'N',  'Wh', 'G',  'R',
                    '5mr', '5pr', '5sr']

    # ツモ牌の認識と出力する関数
    def MyArrangement2(self, left, top, width, depth):
        # print(' ------------------ ')
        self.Tumo = []
        prtsc_range = (left, top, width, depth)
        t1 = time.time()
        q1 = pg.locateOnScreen("./img_web/1m.png", region=prtsc_range, confidence=0.8)
        if q1 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('1m')
            self.Tumo.append('1m')
            return(self.Tumo)
        q2 = pg.locateOnScreen("./img_web/2m.png", region=prtsc_range, confidence=0.8)
        if q2 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('2m')
            self.Tumo.append('2m')
            return(self.Tumo)
        q3 = pg.locateOnScreen("./img_web/3m.png", region=prtsc_range, confidence=0.8)
        if q3 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('3m')
            self.Tumo.append('3m')
            return(self.Tumo)
        q4 = pg.locateOnScreen("./img_web/4m.png", region=prtsc_range, confidence=0.8)
        if q4 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('4m')
            self.Tumo.append('4m')
            return(self.Tumo)
        q5a = pg.locateOnScreen("./img_web/5m.png", region=prtsc_range, confidence=0.8)
        q5b = pg.locateOnScreen("./img_web/5mr.png", region=prtsc_range, confidence=0.8)
        if q5a != None or q5b != None:
            t2 = time.time()
            # print(t2-t1)
            # print('5m')
            self.Tumo.append('5m')
            return(self.Tumo)
        q6 = pg.locateOnScreen("./img_web/6m.png", region=prtsc_range, confidence=0.8)
        if q6 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('6m')
            self.Tumo.append('6m')
            return(self.Tumo)
        q7 = pg.locateOnScreen("./img_web/7m.png", region=prtsc_range, confidence=0.8)
        if q7 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('7m')
            self.Tumo.append('7m')
            return(self.Tumo)
        q8 = pg.locateOnScreen("./img_web/8m.png", region=prtsc_range, confidence=0.8)
        if q8 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('8m')
            self.Tumo.append('8m')
            return(self.Tumo)
        q9 = pg.locateOnScreen("./img_web/9m.png", region=prtsc_range, confidence=0.8)
        if q9 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('9m')
            self.Tumo.append('9m')
            return(self.Tumo)
        q10 = pg.locateOnScreen("./img_web/1p.png", region=prtsc_range, confidence=0.8)
        if q10 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('1p')
            self.Tumo.append('1p')
            return(self.Tumo)
        q11 = pg.locateOnScreen("./img_web/2p.png", region=prtsc_range, confidence=0.8)
        if q11 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('2p')
            self.Tumo.append('2p')
            return(self.Tumo)
        q12 = pg.locateOnScreen("./img_web/3p.png", region=prtsc_range, confidence=0.8)
        if q12 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('3p')
            self.Tumo.append('3p')
            return(self.Tumo)
        q13 = pg.locateOnScreen("./img_web/4p.png", region=prtsc_range, confidence=0.8)
        if q13 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('4p')
            self.Tumo.append('4p')
            return(self.Tumo)
        q14a = pg.locateOnScreen("./img_web/5p.png", region=prtsc_range, confidence=0.8)
        q14b = pg.locateOnScreen("./img_web/5pr.png", region=prtsc_range, confidence=0.8)
        if q14a != None or q14b != None:
            t2 = time.time()
            # print(t2-t1)
            # print('5p')
            self.Tumo.append('5p')
            return(self.Tumo)
        q15 = pg.locateOnScreen("./img_web/6p.png", region=prtsc_range, confidence=0.8)
        if q15 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('6p')
            self.Tumo.append('6p')
            return(self.Tumo)
        q16 = pg.locateOnScreen("./img_web/7p.png", region=prtsc_range, confidence=0.8)
        if q16 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('7p')
            self.Tumo.append('7p')
            return(self.Tumo)
        q17 = pg.locateOnScreen("./img_web/8p.png", region=prtsc_range, confidence=0.8)
        if q17 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('8p')
            self.Tumo.append('8p')
            return(self.Tumo)
        q18 = pg.locateOnScreen("./img_web/9p.png", region=prtsc_range, confidence=0.8)
        if q18 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('9p')
            self.Tumo.append('9p')
            return(self.Tumo)
        q19 = pg.locateOnScreen("./img_web/1s.png", region=prtsc_range, confidence=0.8)
        if q19 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('1s')
            self.Tumo.append('1s')
            return(self.Tumo)
        q20 = pg.locateOnScreen("./img_web/2s.png", region=prtsc_range, confidence=0.8)
        if q20 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('2s')
            self.Tumo.append('2s')
            return(self.Tumo)
        q21 = pg.locateOnScreen("./img_web/3s.png", region=prtsc_range, confidence=0.7)
        if q21 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('3s')
            self.Tumo.append('3s')
            return(self.Tumo)
        q22 = pg.locateOnScreen("./img_web/4s.png", region=prtsc_range, confidence=0.8)
        if q22 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('4s')
            self.Tumo.append('4s')
            return(self.Tumo)
        q23a = pg.locateOnScreen("./img_web/5s.png", region=prtsc_range, confidence=0.8)
        q23b = pg.locateOnScreen("./img_web/5sr.png", region=prtsc_range, confidence=0.8)
        if q23a != None or q23b != None:
            t2 = time.time()
            # print(t2-t1)
            # print('5s')
            self.Tumo.append('5s')
            return(self.Tumo)
        q24 = pg.locateOnScreen("./img_web/6s.png", region=prtsc_range, confidence=0.8)
        if q24 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('6s')
            self.Tumo.append('6s')
            return(self.Tumo)
        q25 = pg.locateOnScreen("./img_web/7s.png", region=prtsc_range, confidence=0.8)
        if q25 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('7s')
            self.Tumo.append('7s')
            return(self.Tumo)
        q26 = pg.locateOnScreen("./img_web/8s.png", region=prtsc_range, confidence=0.8)
        if q26 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('8s')
            self.Tumo.append('8s')
            return(self.Tumo)
        q27 = pg.locateOnScreen("./img_web/9s.png", region=prtsc_range, confidence=0.8)
        if q27 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('9s')
            self.Tumo.append('9s')
            return(self.Tumo)
        q28 = pg.locateOnScreen("./img_web/E.png", region=prtsc_range, confidence=0.8)
        if q28 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('E')
            self.Tumo.append('E')
            return(self.Tumo)
        q29 = pg.locateOnScreen("./img_web/S.png", region=prtsc_range, confidence=0.8)
        if q29 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('S')
            self.Tumo.append('S')
            return(self.Tumo)
        q30 = pg.locateOnScreen("./img_web/We.png", region=prtsc_range, confidence=0.8)
        if q30 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('We')
            self.Tumo.append('We')
            return(self.Tumo)
        q31 = pg.locateOnScreen("./img_web/N.png", region=prtsc_range, confidence=0.8)
        if q31 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('N')
            self.Tumo.append('N')
            return(self.Tumo)
        q32 = pg.locateOnScreen("./img_web/Wh.png", region=prtsc_range, confidence=0.8)
        if q32 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('Wh')
            self.Tumo.append('Wh')
            return(self.Tumo)
        q33 = pg.locateOnScreen("./img_web/G.png", region=prtsc_range, confidence=0.8)
        if q33 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('G')
            self.Tumo.append('G')
            return(self.Tumo)
        q34 = pg.locateOnScreen("./img_web/R.png", region=prtsc_range, confidence=0.8)
        if q34 != None:
            t2 = time.time()
            # print(t2-t1)
            # print('R')
            self.Tumo.append('R')
            return(self.Tumo)
        # q35 = pg.locateOnScreen("./img_web/5mr.png", region=prtsc_range, confidence=0.8)
        # if q35 != None:
        #     t2 = time.time()
        #     # print(t2-t1)
        #     # print('5mr')
        #     self.Tumo.append('5mr')
        #     return(self.Tumo)
        # q36 = pg.locateOnScreen("./img_web/5pr.png", region=prtsc_range, confidence=0.8)
        # if q36 != None:
        #     t2 = time.time()
        #     # print(t2-t1)
        #     # print('5pr')
        #     self.Tumo.append('5pr')
        #     return(self.Tumo)
        # q37 = pg.locateOnScreen("./img_web/5sr.png", region=prtsc_range, confidence=0.8)
        # if q37 != None:
        #     t2 = time.time()
        #     # print(t2-t1)
        #     # print('5sr')
        #     self.Tumo.append('5sr')
        #     return(self.Tumo)

    # まず、ヘッドの数をカウント。七対子へ行くか判断する。 return HeadCheckList
    def PreliminarySelection(self, Select):
        self.TiToi = 0
        PieceCheck = 0
        self.HeadCheckList = []
        for i, j in list(it.combinations(Select, 2)):
            l = []
            l.append(i)
            l.append(j)
            if l in [['1m', '1m'], ['2m', '2m'], ['3m', '3m'], ['4m', '4m'], 
                     ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'], ['9m', '9m'],
                     ['1p', '1p'], ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], 
                     ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'], ['9p', '9p'],
                     ['1s', '1s'], ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], 
                     ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s'], ['9s', '9s'],
                     ['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], 
                     ['Wh', 'Wh'], ['G', 'G'], ['R', 'R']
                     ]:
                if l not in self.HeadCheckList:
                    self.HeadCheckList.append(l)
                    PieceCheck += 1
        if PieceCheck >= 5:
            self.TiToi = 1
            print('七対子')
            print(' ')   
        return self.HeadCheckList, self.TiToi

    # 切る牌を選択する関数（５，４，３ 個牌への処理） return(MemberCheck)
    def FirstSelection(self, Select, FourFlg):
        MemberCheck = 0
        TartsCheck = 0

        # まだ仮だが、聴牌の時捨てる牌をスムーズに選ぶため、雀頭なしケースでの四つ系は一回だけ抽出する。
        FourPiece = 0

        # 九つ系（１）３面子・・・確定した面子を抜き取るのは悪くないはず。
        for i, j, k, m, n, o, p, q, r in list(it.combinations(Select, 9)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            l.append(o)
            l.append(p)
            l.append(q)
            l.append(r)
            if l in [['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m'], ['1m', '2m', '3m', '3m', '4m', '4m', '5m', '5m', '6m'], 
                     ['1m', '2m', '2m', '3m', '3m', '4m', '5m', '6m', '7m'], ['1m', '2m', '3m', '3m', '4m', '5m', '6m', '7m', '8m'],
                     ['1m', '2m', '3m', '3m', '4m', '5m', '5m', '6m', '7m'], ['1m', '2m', '3m', '4m', '4m', '5m', '5m', '6m', '6m'], 
                     ['1m', '2m', '3m', '4m', '5m', '5m', '6m', '6m', '7m'], ['2m', '3m', '4m', '4m', '5m', '5m', '6m', '6m', '7m'],
                     ['3m', '4m', '5m', '6m', '7m', '7m', '8m', '8m', '9m'], ['2m', '3m', '4m', '5m', '6m', '7m', '7m', '8m', '9m'], 
                     ['3m', '4m', '5m', '5m', '6m', '7m', '7m', '8m', '9m'],  
                     ['3m', '4m', '4m', '5m', '5m', '6m', '7m', '8m', '9m'], ['3m', '4m', '5m', '5m', '6m', '6m', '7m', '7m', '8m'],
                     ['4m', '5m', '6m', '6m', '7m', '7m', '8m', '8m', '9m'], ['4m', '5m', '5m', '6m', '6m', '7m', '7m', '8m', '9m'],
                     ['1m', '1m', '2m', '2m', '2m', '3m', '3m', '3m', '4m'], ['2m', '2m', '3m', '3m', '3m', '4m', '4m', '4m', '5m'],
                     ['3m', '3m', '4m', '4m', '4m', '5m', '5m', '5m', '6m'], ['4m', '4m', '5m', '5m', '5m', '6m', '6m', '6m', '7m'],
                     ['5m', '5m', '6m', '6m', '6m', '7m', '7m', '7m', '8m'], ['6m', '6m', '7m', '7m', '7m', '8m', '8m', '8m', '9m'],


                     ['1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p'], ['1p', '2p', '3p', '3p', '4p', '4p', '5p', '5p', '6p'], 
                     ['1p', '2p', '2p', '3p', '3p', '4p', '5p', '6p', '7p'], ['1p', '2p', '3p', '3p', '4p', '5p', '6p', '7p', '8p'],
                     ['1p', '2p', '3p', '3p', '4p', '5p', '5p', '6p', '7p'], ['1p', '2p', '3p', '4p', '4p', '5p', '5p', '6p', '6p'], 
                     ['1p', '2p', '3p', '4p', '5p', '5p', '6p', '6p', '7p'], ['2p', '3p', '4p', '4p', '5p', '5p', '6p', '6p', '7p'],
                     ['3p', '4p', '5p', '6p', '7p', '7p', '8p', '8p', '9p'], ['2p', '3p', '4p', '5p', '6p', '7p', '7p', '8p', '9p'], 
                     ['3p', '4p', '5p', '5p', '6p', '7p', '7p', '8p', '9p'], 
                     ['3p', '4p', '4p', '5p', '5p', '6p', '7p', '8p', '9p'], ['3p', '4p', '5p', '5p', '6p', '6p', '7p', '7p', '8p'],
                     ['4p', '5p', '6p', '6p', '7p', '7p', '8p', '8p', '9p'], ['4p', '5p', '5p', '6p', '6p', '7p', '7p', '8p', '9p'],
                     ['1p', '1p', '2p', '2p', '2p', '3p', '3p', '3p', '4p'], ['2p', '2p', '3p', '3p', '3p', '4p', '4p', '4p', '5p'],
                     ['3p', '3p', '4p', '4p', '4p', '5p', '5p', '5p', '6p'], ['4p', '4p', '5p', '5p', '5p', '6p', '6p', '6p', '7p'],
                     ['5p', '5p', '6p', '6p', '6p', '7p', '7p', '7p', '8p'], ['6p', '6p', '7p', '7p', '7p', '8p', '8p', '8p', '9p'],


                     ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s'], ['1s', '2s', '3s', '3s', '4s', '4s', '5s', '5s', '6s'], 
                     ['1s', '2s', '2s', '3s', '3s', '4s', '5s', '6s', '7s'], ['1s', '2s', '3s', '3s', '4s', '5s', '6s', '7s', '8s'],
                     ['1s', '2s', '3s', '3s', '4s', '5s', '5s', '6s', '7s'], ['1s', '2s', '3s', '4s', '4s', '5s', '5s', '6s', '6s'], 
                     ['1s', '2s', '3s', '4s', '5s', '5s', '6s', '6s', '7s'], ['2s', '3s', '4s', '4s', '5s', '5s', '6s', '6s', '7s'],
                     ['3s', '4s', '5s', '6s', '7s', '7s', '8s', '8s', '9s'], ['2s', '3s', '4s', '5s', '6s', '7s', '7s', '8s', '9s'], 
                     ['3s', '4s', '5s', '5s', '6s', '7s', '7s', '8s', '9s'],  
                     ['3s', '4s', '4s', '5s', '5s', '6s', '7s', '8s', '9s'], ['3s', '4s', '5s', '5s', '6s', '6s', '7s', '7s', '8s'],
                     ['4s', '5s', '6s', '6s', '7s', '7s', '8s', '8s', '9s'], ['4s', '5s', '5s', '6s', '6s', '7s', '7s', '8s', '9s'],
                     ['1s', '1s', '2s', '2s', '2s', '3s', '3s', '3s', '4s'], ['2s', '2s', '3s', '3s', '3s', '4s', '4s', '4s', '5s'],
                     ['3s', '3s', '4s', '4s', '4s', '5s', '5s', '5s', '6s'], ['4s', '4s', '5s', '5s', '5s', '6s', '6s', '6s', '7s'],
                     ['5s', '5s', '6s', '6s', '6s', '7s', '7s', '7s', '8s'], ['6s', '6s', '7s', '7s', '7s', '8s', '8s', '8s', '9s'],



                     ['1m', '1m', '1m', '2m', '2m', '3m', '3m', '4m', '4m'], ['2m', '2m', '2m', '3m', '3m', '4m', '4m', '5m', '5m'], 
                     ['3m', '3m', '3m', '4m', '4m', '5m', '5m', '6m', '6m'], ['4m', '4m', '4m', '5m', '5m', '6m', '6m', '7m', '7m'],
                     ['5m', '5m', '5m', '6m', '6m', '7m', '7m', '8m', '8m'], ['6m', '6m', '6m', '7m', '7m', '8m', '8m', '9m', '9m'],
                     ['1m', '1m', '1m', '2m', '2m', '2m', '3m', '4m', '5m'], ['2m', '2m', '2m', '3m', '3m', '3m', '4m', '5m', '6m'], 
                     ['3m', '3m', '3m', '4m', '4m', '4m', '5m', '6m', '7m'], ['4m', '4m', '4m', '5m', '5m', '5m', '6m', '7m', '8m'],
                     ['5m', '5m', '5m', '6m', '6m', '6m', '7m', '8m', '9m'],
                     ['1p', '1p', '1p', '2p', '2p', '3p', '3p', '4p', '4p'], ['2p', '2p', '2p', '3p', '3p', '4p', '4p', '5p', '5p'], 
                     ['3p', '3p', '3p', '4p', '4p', '5p', '5p', '6p', '6p'], ['4p', '4p', '4p', '5p', '5p', '6p', '6p', '7p', '7p'],
                     ['5p', '5p', '5p', '6p', '6p', '7p', '7p', '8p', '8p'], ['6p', '6p', '6p', '7p', '7p', '8p', '8p', '9p', '9p'],
                     ['1p', '1p', '1p', '2p', '2p', '2p', '3p', '4p', '5p'], ['2p', '2p', '2p', '3p', '3p', '3p', '4p', '5p', '6p'], 
                     ['3p', '3p', '3p', '4p', '4p', '4p', '5p', '6p', '7p'], ['4p', '4p', '4p', '5p', '5p', '5p', '6p', '7p', '8p'],
                     ['5p', '5p', '5p', '6p', '6p', '6p', '7p', '8p', '9p'],
                     ['1s', '1s', '1s', '2s', '2s', '3s', '3s', '4s', '4s'], ['2s', '2s', '2s', '3s', '3s', '4s', '4s', '5s', '5s'], 
                     ['3s', '3s', '3s', '4s', '4s', '5s', '5s', '6s', '6s'], ['4s', '4s', '4s', '5s', '5s', '6s', '6s', '7s', '7s'],
                     ['5s', '5s', '5s', '6s', '6s', '7s', '7s', '8s', '8s'], ['6s', '6s', '6s', '7s', '7s', '8s', '8s', '9s', '9s'],
                     ['1s', '1s', '1s', '2s', '2s', '2s', '3s', '4s', '5s'], ['2s', '2s', '2s', '3s', '3s', '3s', '4s', '5s', '6s'], 
                     ['3s', '3s', '3s', '4s', '4s', '4s', '5s', '6s', '7s'], ['4s', '4s', '4s', '5s', '5s', '5s', '6s', '7s', '8s'],
                     ['5s', '5s', '5s', '6s', '6s', '6s', '7s', '8s', '9s'],

                     ['1m', '1m', '1m', '2m', '3m', '4m', '5m', '6m', '7m'], ['2m', '2m', '2m', '3m', '4m', '5m', '6m', '7m', '8m'], 
                     ['3m', '3m', '3m', '4m', '5m', '6m', '7m', '8m', '9m'], 
                     ['1m', '1m', '1m', '2m', '3m', '3m', '4m', '4m', '5m'], ['2m', '2m', '2m', '3m', '4m', '4m', '5m', '5m', '6m'], 
                     ['3m', '3m', '3m', '4m', '5m', '5m', '6m', '6m', '7m'], ['4m', '4m', '4m', '5m', '6m', '6m', '7m', '7m', '8m'],
                     ['5m', '5m', '5m', '6m', '7m', '7m', '8m', '8m', '9m'], 
                     ['1m', '1m', '1m', '1m', '2m', '3m', '4m', '5m', '6m'], ['2m', '2m', '2m', '2m', '3m', '4m', '5m', '6m', '7m'], 
                     ['3m', '3m', '3m', '3m', '4m', '5m', '6m', '7m', '8m'], ['4m', '4m', '4m', '4m', '5m', '6m', '7m', '8m', '9m'],
                     ['1p', '1p', '1p', '2p', '3p', '4p', '5p', '6p', '7p'], ['2p', '2p', '2p', '3p', '4p', '5p', '6p', '7p', '8p'], 
                     ['3p', '3p', '3p', '4p', '5p', '6p', '7p', '8p', '9p'], 
                     ['1p', '1p', '1p', '2p', '3p', '3p', '4p', '4p', '5p'], ['2p', '2p', '2p', '3p', '4p', '4p', '5p', '5p', '6p'], 
                     ['3p', '3p', '3p', '4p', '5p', '5p', '6p', '6p', '7p'], ['4p', '4p', '4p', '5p', '6p', '6p', '7p', '7p', '8p'],
                     ['5p', '5p', '5p', '6p', '7p', '7p', '8p', '8p', '9p'], ['4p', '4p', '4p', '4p', '5p', '6p', '7p', '8p', '9p'],
                     ['1p', '1p', '1p', '1p', '2p', '3p', '4p', '5p', '6p'], ['2p', '2p', '2p', '2p', '3p', '4p', '5p', '6p', '7p'], 
                     ['3p', '3p', '3p', '3p', '4p', '5p', '6p', '7p', '8p'], 
                     ['1s', '1s', '1s', '2s', '3s', '4s', '5s', '6s', '7s'], ['2s', '2s', '2s', '3s', '4s', '5s', '6s', '7s', '8s'], 
                     ['3s', '3s', '3s', '4s', '5s', '6s', '7s', '8s', '9s'], 
                     ['1s', '1s', '1s', '2s', '3s', '3s', '4s', '4s', '5s'], ['2s', '2s', '2s', '3s', '4s', '4s', '5s', '5s', '6s'], 
                     ['3s', '3s', '3s', '4s', '5s', '5s', '6s', '6s', '7s'], ['4s', '4s', '4s', '5s', '6s', '6s', '7s', '7s', '8s'],
                     ['5s', '5s', '5s', '6s', '7s', '7s', '8s', '8s', '9s'], ['4s', '4s', '4s', '4s', '5s', '6s', '7s', '8s', '9s'],
                     ['1s', '1s', '1s', '1s', '2s', '3s', '4s', '5s', '6s'], ['2s', '2s', '2s', '2s', '3s', '4s', '5s', '6s', '7s'], 
                     ['3s', '3s', '3s', '3s', '4s', '5s', '6s', '7s', '8s'], 
                     
                     ['1m', '1m', '1m', '1m', '2m', '3m', '3m', '4m', '5m'], ['2m', '2m', '2m', '2m', '3m', '4m', '4m', '5m', '6m'], 
                     ['3m', '3m', '3m', '3m', '4m', '5m', '5m', '6m', '7m'], ['4m', '4m', '4m', '4m', '5m', '6m', '6m', '7m', '8m'],
                     ['5m', '5m', '5m', '5m', '6m', '7m', '7m', '8m', '9m'],
                     ['1p', '1p', '1p', '1p', '2p', '3p', '3p', '4p', '5p'], ['2p', '2p', '2p', '2p', '3p', '4p', '4p', '5p', '6p'], 
                     ['3p', '3p', '3p', '3p', '4p', '5p', '5p', '6p', '7p'], ['4p', '4p', '4p', '4p', '5p', '6p', '6p', '7p', '8p'],
                     ['5p', '5p', '5p', '5p', '6p', '7p', '7p', '8p', '9p'],
                     ['1s', '1s', '1s', '1s', '2s', '3s', '3s', '4s', '5s'], ['2s', '2s', '2s', '2s', '3s', '4s', '4s', '5s', '6s'], 
                     ['3s', '3s', '3s', '3s', '4s', '5s', '5s', '6s', '7s'], ['4s', '4s', '4s', '4s', '5s', '6s', '6s', '7s', '8s'],
                     ['5s', '5s', '5s', '5s', '6s', '7s', '7s', '8s', '9s'],

                     ['1m', '1m', '1m', '1m', '2m', '2m', '3m', '3m', '4m'], ['2m', '2m', '2m', '2m', '3m', '3m', '4m', '4m', '5m'], 
                     ['3m', '3m', '3m', '3m', '4m', '4m', '5m', '5m', '6m'], ['4m', '4m', '4m', '4m', '5m', '5m', '6m', '6m', '7m'],
                     ['5m', '5m', '5m', '5m', '6m', '6m', '7m', '7m', '8m'], ['6m', '6m', '6m', '6m', '7m', '7m', '8m', '8m', '9m'], 
                     ['1p', '1p', '1p', '1p', '2p', '2p', '3p', '3p', '4p'], ['2p', '2p', '2p', '2p', '3p', '3p', '4p', '4p', '5p'], 
                     ['3p', '3p', '3p', '3p', '4p', '4p', '5p', '5p', '6p'], ['4p', '4p', '4p', '4p', '5p', '5p', '6p', '6p', '7p'],
                     ['5p', '5p', '5p', '5p', '6p', '6p', '7p', '7p', '8p'], ['6p', '6p', '6p', '6p', '7p', '7p', '8p', '8p', '9p'],
                     ['1s', '1s', '1s', '1s', '2s', '2s', '3s', '3s', '4s'], ['2s', '2s', '2s', '2s', '3s', '3s', '4s', '4s', '5s'], 
                     ['3s', '3s', '3s', '3s', '4s', '4s', '5s', '5s', '6s'], ['4s', '4s', '4s', '4s', '5s', '5s', '6s', '6s', '7s'],
                     ['5s', '5s', '5s', '5s', '6s', '6s', '7s', '7s', '8s'], ['6s', '6s', '6s', '6s', '7s', '7s', '8s', '8s', '9s'],

                     ['1m', '2m', '3m', '3m', '3m', '3m', '4m', '5m', '6m'], ['2m', '3m', '4m', '4m', '4m', '4m', '5m', '6m', '7m'],
                     ['3m', '4m', '5m', '5m', '5m', '5m', '6m', '7m', '8m'], ['4m', '5m', '6m', '6m', '6m', '6m', '7m', '8m', '9m'],
                     ['1p', '2p', '3p', '3p', '3p', '3p', '4p', '5p', '6p'], ['2p', '3p', '4p', '4p', '4p', '4p', '5p', '6p', '7p'],
                     ['3p', '4p', '5p', '5p', '5p', '5p', '6p', '7p', '8p'], ['4p', '5p', '6p', '6p', '6p', '6p', '7p', '8p', '9p'],
                     ['1s', '2s', '3s', '3s', '3s', '3s', '4s', '5s', '6s'], ['2s', '3s', '4s', '4s', '4s', '4s', '5s', '6s', '7s'],
                     ['3s', '4s', '5s', '5s', '5s', '5s', '6s', '7s', '8s'], ['4s', '5s', '6s', '6s', '6s', '6s', '7s', '8s', '9s'],

                     ['1m', '1m', '2m', '2m', '3m', '3m', '3m', '4m', '5m'], ['1m', '1m', '2m', '2m', '3m', '3m', '4m', '5m', '6m'],
                     ['2m', '2m', '3m', '3m', '4m', '4m', '4m', '5m', '6m'], ['2m', '2m', '3m', '3m', '4m', '4m', '5m', '6m', '7m'],
                     ['3m', '3m', '4m', '4m', '5m', '5m', '5m', '6m', '7m'], ['3m', '3m', '4m', '4m', '5m', '5m', '6m', '7m', '8m'],
                     ['4m', '4m', '5m', '5m', '6m', '6m', '6m', '7m', '8m'], ['4m', '4m', '5m', '5m', '6m', '6m', '7m', '8m', '9m'],
                     ['1p', '1p', '2p', '2p', '3p', '3p', '3p', '4p', '5p'], ['1p', '1p', '2p', '2p', '3p', '3p', '4p', '5p', '6p'],
                     ['2p', '2p', '3p', '3p', '4p', '4p', '4p', '5p', '6p'], ['2p', '2p', '3p', '3p', '4p', '4p', '5p', '6p', '7p'],
                     ['3p', '3p', '4p', '4p', '5p', '5p', '5p', '6p', '7p'], ['3p', '3p', '4p', '4p', '5p', '5p', '6p', '7p', '8p'],
                     ['4p', '4p', '5p', '5p', '6p', '6p', '6p', '7p', '8p'], ['4p', '4p', '5p', '5p', '6p', '6p', '7p', '8p', '9p'],
                     ['1s', '1s', '2s', '2s', '3s', '3s', '3s', '4s', '5s'], ['1s', '1s', '2s', '2s', '3s', '3s', '4s', '5s', '6s'],
                     ['2s', '2s', '3s', '3s', '4s', '4s', '4s', '5s', '6s'], ['2s', '2s', '3s', '3s', '4s', '4s', '5s', '6s', '7s'],
                     ['3s', '3s', '4s', '4s', '5s', '5s', '5s', '6s', '7s'], ['3s', '3s', '4s', '4s', '5s', '5s', '6s', '7s', '8s'],
                     ['4s', '4s', '5s', '5s', '6s', '6s', '6s', '7s', '8s'], ['4s', '4s', '5s', '5s', '6s', '6s', '7s', '8s', '9s'], 

                     ['1m', '2m', '2m', '3m', '3m', '4m', '4m', '5m', '6m'], ['1m', '2m', '2m', '3m', '3m', '3m', '4m', '4m', '5m'],
                     ['2m', '3m', '3m', '4m', '4m', '5m', '5m', '6m', '7m'], ['2m', '3m', '3m', '4m', '4m', '4m', '5m', '5m', '6m'],
                     ['3m', '4m', '4m', '5m', '5m', '6m', '6m', '7m', '8m'], ['3m', '4m', '4m', '5m', '5m', '5m', '6m', '6m', '7m'],
                     ['4m', '5m', '5m', '6m', '6m', '7m', '7m', '8m', '9m'], ['4m', '5m', '5m', '6m', '6m', '6m', '7m', '7m', '8m'],
                     ['1p', '2p', '2p', '3p', '3p', '4p', '4p', '5p', '6p'], ['1p', '2p', '2p', '3p', '3p', '3p', '4p', '4p', '5p'],
                     ['2p', '3p', '3p', '4p', '4p', '5p', '5p', '6p', '7p'], ['2p', '3p', '3p', '4p', '4p', '4p', '5p', '5p', '6p'],
                     ['3p', '4p', '4p', '5p', '5p', '6p', '6p', '7p', '8p'], ['3p', '4p', '4p', '5p', '5p', '5p', '6p', '6p', '7p'],
                     ['4p', '5p', '5p', '6p', '6p', '7p', '7p', '8p', '9p'], ['4p', '5p', '5p', '6p', '6p', '6p', '7p', '7p', '8p'],
                     ['1s', '2s', '2s', '3s', '3s', '4s', '4s', '5s', '6s'], ['1s', '2s', '2s', '3s', '3s', '3s', '4s', '4s', '5s'],
                     ['2s', '3s', '3s', '4s', '4s', '5s', '5s', '6s', '7s'], ['2s', '3s', '3s', '4s', '4s', '4s', '5s', '5s', '6s'],
                     ['3s', '4s', '4s', '5s', '5s', '6s', '6s', '7s', '8s'], ['3s', '4s', '4s', '5s', '5s', '5s', '6s', '6s', '7s'],
                     ['4s', '5s', '5s', '6s', '6s', '7s', '7s', '8s', '9s'], ['4s', '5s', '5s', '6s', '6s', '6s', '7s', '7s', '8s'],
                     
                     ['1m', '1m', '1m', '2m', '2m', '2m', '3m', '3m', '3m'], ['2m', '2m', '2m', '3m', '3m', '3m', '4m', '4m', '4m'],
                     ['3m', '3m', '3m', '4m', '4m', '4m', '5m', '5m', '5m'], ['4m', '4m', '4m', '5m', '5m', '5m', '6m', '6m', '6m'],
                     ['5m', '5m', '5m', '6m', '6m', '6m', '7m', '7m', '7m'], ['6m', '6m', '6m', '7m', '7m', '7m', '8m', '8m', '8m'],
                     ['7m', '7m', '7m', '8m', '8m', '8m', '9m', '9m', '9m'],
                     ['1p', '1p', '1p', '2p', '2p', '2p', '3p', '3p', '3p'], ['2p', '2p', '2p', '3p', '3p', '3p', '4p', '4p', '4p'],
                     ['3p', '3p', '3p', '4p', '4p', '4p', '5p', '5p', '5p'], ['4p', '4p', '4p', '5p', '5p', '5p', '6p', '6p', '6p'],
                     ['5p', '5p', '5p', '6p', '6p', '6p', '7p', '7p', '7p'], ['6p', '6p', '6p', '7p', '7p', '7p', '8p', '8p', '8p'],
                     ['7p', '7p', '7p', '8p', '8p', '8p', '9p', '9p', '9p'],
                     ['1s', '1s', '1s', '2s', '2s', '2s', '3s', '3s', '3s'], ['2s', '2s', '2s', '3s', '3s', '3s', '4s', '4s', '4s'],
                     ['3s', '3s', '3s', '4s', '4s', '4s', '5s', '5s', '5s'], ['4s', '4s', '4s', '5s', '5s', '5s', '6s', '6s', '6s'],
                     ['5s', '5s', '5s', '6s', '6s', '6s', '7s', '7s', '7s'], ['6s', '6s', '6s', '7s', '7s', '7s', '8s', '8s', '8s'],
                     ['7s', '7s', '7s', '8s', '8s', '8s', '9s', '9s', '9s'],                     


                     ['1m', '2m', '2m', '2m', '2m', '3m', '3m', '4m', '5m'], ['2m', '3m', '3m', '3m', '3m', '4m', '4m', '5m', '6m'],
                     ['3m', '4m', '4m', '4m', '4m', '5m', '5m', '6m', '7m'], ['4m', '5m', '5m', '5m', '5m', '6m', '6m', '7m', '8m'],
                     ['5m', '6m', '6m', '6m', '6m', '7m', '7m', '8m', '9m'],
                     ['1p', '2p', '2p', '2p', '2p', '3p', '3p', '4p', '5p'], ['2p', '3p', '3p', '3p', '3p', '4p', '4p', '5p', '6p'],
                     ['3p', '4p', '4p', '4p', '4p', '5p', '5p', '6p', '7p'], ['4p', '5p', '5p', '5p', '5p', '6p', '6p', '7p', '8p'],
                     ['5p', '6p', '6p', '6p', '6p', '7p', '7p', '8p', '9p'], 
                     ['1s', '2s', '2s', '2s', '2s', '3s', '3s', '4s', '5s'], ['2s', '3s', '3s', '3s', '3s', '4s', '4s', '5s', '6s'],
                     ['3s', '4s', '4s', '4s', '4s', '5s', '5s', '6s', '7s'], ['4s', '5s', '5s', '5s', '5s', '6s', '6s', '7s', '8s'],
                     ['5s', '6s', '6s', '6s', '6s', '7s', '7s', '8s', '9s'], 




                    ] and self.TiToi == 0:
                print('九つ系（１）：3面子 ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select and o in Select and p in Select and q in Select and r in Select:
                    Select.remove(i)
                    Select.remove(j)
                    Select.remove(k)
                    Select.remove(m)
                    Select.remove(n)
                    Select.remove(o)
                    Select.remove(p)
                    Select.remove(q)
                    Select.remove(r)
                    MemberCheck += 3
        
        # 九つ系（２）ウィング型・・・暗刻があるのに除いたりと、いやな予感はするが、しばらく使ってみる。
        for i, j, k, m, n, o, p, q, r in list(it.combinations(Select, 9)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            l.append(o)
            l.append(p)
            l.append(q)
            l.append(r)
            if l in [['1m', '2m', '2m', '3m', '4m', '5m', '6m', '6m', '7m'],
                     ['2m', '3m', '3m', '4m', '5m', '6m', '7m', '7m', '8m'],
                     ['3m', '4m', '4m', '5m', '6m', '7m', '8m', '8m', '9m'],
                     ['1p', '2p', '2p', '3p', '4p', '5p', '6p', '6p', '7p'], 
                     ['2p', '3p', '3p', '4p', '5p', '6p', '7p', '7p', '8p'],
                     ['3p', '4p', '4p', '5p', '6p', '7p', '8p', '8p', '9p'], 
                     ['1s', '2s', '2s', '3s', '4s', '5s', '6s', '6s', '7s'], 
                     ['2s', '3s', '3s', '4s', '5s', '6s', '7s', '7s', '8s'],
                     ['3s', '4s', '4s', '5s', '6s', '7s', '8s', '8s', '9s'],  
                    ] and self.TiToi == 0:
                print('九つ系(2)： ウィング型 ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select and o in Select and p in Select and q in Select and r in Select:
                    Select.remove(i)
                    Select.remove(j)
                    Select.remove(k)
                    Select.remove(m)
                    Select.remove(n)
                    Select.remove(o)
                    Select.remove(p)
                    Select.remove(q)
                    Select.remove(r)
                    MemberCheck += 2

        # 六つ系 連続両面や暗刻＋面子
        for i, j, k, m, n, o in list(it.combinations(Select, 6)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            l.append(o)
            Muttsu = copy.deepcopy(Select)
            if l in [['1m', '2m', '3m', '4m', '5m', '6m'], ['2m', '3m', '4m', '5m', '6m', '7m'], ['3m', '4m', '5m', '6m', '7m', '8m'], ['4m', '5m', '6m', '7m', '8m', '9m'], 
                     ['1m', '2m', '3m', '3m', '4m', '5m'], ['2m', '3m', '4m', '4m', '5m', '6m'], ['3m', '4m', '5m', '5m', '6m', '7m'], ['4m', '5m', '6m', '6m', '7m', '8m'], ['5m', '6m', '7m', '7m', '8m', '9m'],
                     ['1m', '2m', '2m', '3m', '3m', '4m'], ['2m', '3m', '3m', '4m', '4m', '5m'], ['3m', '4m', '4m', '5m', '5m', '6m'], 
                     ['4m', '5m', '5m', '6m', '6m', '7m'], ['5m', '6m', '6m', '7m', '7m', '8m'], ['6m', '7m', '7m', '8m', '8m', '9m'],
                     ['1m', '1m', '2m', '2m', '3m', '3m'], ['2m', '2m', '3m', '3m', '4m', '4m'], ['3m', '3m', '4m', '4m', '5m', '5m'], ['4m', '4m', '5m', '5m', '6m', '6m'],
                     ['5m', '5m', '6m', '6m', '7m', '7m'], ['6m', '6m', '7m', '7m', '8m', '8m'], ['7m', '7m', '8m', '8m', '9m', '9m'],
                     ['1p', '2p', '3p', '4p', '5p', '6p'], ['2p', '3p', '4p', '5p', '6p', '7p'], ['3p', '4p', '5p', '6p', '7p', '8p'], ['4p', '5p', '6p', '7p', '8p', '9p'], 
                     ['1p', '2p', '3p', '3p', '4p', '5p'], ['2p', '3p', '4p', '4p', '5p', '6p'], ['3p', '4p', '5p', '5p', '6p', '7p'], ['4p', '5p', '6p', '6p', '7p', '8p'], ['5p', '6p', '7p', '7p', '8p', '9p'],
                     ['1p', '2p', '2p', '3p', '3p', '4p'], ['2p', '3p', '3p', '4p', '4p', '5p'], ['3p', '4p', '4p', '5p', '5p', '6p'], 
                     ['4p', '5p', '5p', '6p', '6p', '7p'], ['5p', '6p', '6p', '7p', '7p', '8p'], ['6p', '7p', '7p', '8p', '8p', '9p'],
                     ['1p', '1p', '2p', '2p', '3p', '3p'], ['2p', '2p', '3p', '3p', '4p', '4p'], ['3p', '3p', '4p', '4p', '5p', '5p'], ['4p', '4p', '5p', '5p', '6p', '6p'],
                     ['5p', '5p', '6p', '6p', '7p', '7p'], ['6p', '6p', '7p', '7p', '8p', '8p'], ['7p', '7p', '8p', '8p', '9p', '9p'],
                     ['1s', '2s', '3s', '4s', '5s', '6s'], ['2s', '3s', '4s', '5s', '6s', '7s'], ['3s', '4s', '5s', '6s', '7s', '8s'], ['4s', '5s', '6s', '7s', '8s', '9s'], 
                     ['1s', '2s', '3s', '3s', '4s', '5s'], ['2s', '3s', '4s', '4s', '5s', '6s'], ['3s', '4s', '5s', '5s', '6s', '7s'], ['4s', '5s', '6s', '6s', '7s', '8s'], ['5s', '6s', '7s', '7s', '8s', '9s'],
                     ['1s', '2s', '2s', '3s', '3s', '4s'], ['2s', '3s', '3s', '4s', '4s', '5s'], ['3s', '4s', '4s', '5s', '5s', '6s'], 
                     ['4s', '5s', '5s', '6s', '6s', '7s'], ['5s', '6s', '6s', '7s', '7s', '8s'], ['6s', '7s', '7s', '8s', '8s', '9s'],
                     ['1s', '1s', '2s', '2s', '3s', '3s'], ['2s', '2s', '3s', '3s', '4s', '4s'], ['3s', '3s', '4s', '4s', '5s', '5s'], ['4s', '4s', '5s', '5s', '6s', '6s'],
                     ['5s', '5s', '6s', '6s', '7s', '7s'], ['6s', '6s', '7s', '7s', '8s', '8s'], ['7s', '7s', '8s', '8s', '9s', '9s'],

                     ['1m', '1m', '1m', '2m', '3m', '4m'], ['2m', '2m', '2m', '3m', '4m', '5m'], ['3m', '3m', '3m', '4m', '5m', '6m'], ['4m', '4m', '4m', '5m', '6m', '7m'], ['5m', '5m', '5m', '6m', '7m', '8m'], ['6m', '6m', '6m', '7m', '8m', '9m'], 
                     ['1m', '2m', '3m', '4m', '4m', '4m'], ['2m', '3m', '4m', '5m', '5m', '5m'], ['3m', '4m', '5m', '6m', '6m', '6m'], ['4m', '5m', '6m', '7m', '7m', '7m'], ['5m', '6m', '7m', '8m', '8m', '8m'], ['6m', '7m', '8m', '9m', '9m', '9m'],
                     ['1p', '1p', '1p', '2p', '3p', '4p'], ['2p', '2p', '2p', '3p', '4p', '5p'], ['3p', '3p', '3p', '4p', '5p', '6p'], ['4p', '4p', '4p', '5p', '6p', '7p'], ['5p', '5p', '5p', '6p', '7p', '8p'], ['6p', '6p', '6p', '7p', '8p', '9p'], 
                     ['1p', '2p', '3p', '4p', '4p', '4p'], ['2p', '3p', '4p', '5p', '5p', '5p'], ['3p', '4p', '5p', '6p', '6p', '6p'], ['4p', '5p', '6p', '7p', '7p', '7p'], ['5p', '6p', '7p', '8p', '8p', '8p'], ['6p', '7p', '8p', '9p', '9p', '9p'],
                     ['1s', '1s', '1s', '2s', '3s', '4s'], ['2s', '2s', '2s', '3s', '4s', '5s'], ['3s', '3s', '3s', '4s', '5s', '6s'], ['4s', '4s', '4s', '5s', '6s', '7s'], ['5s', '5s', '5s', '6s', '7s', '8s'], ['6s', '6s', '6s', '7s', '8s', '9s'], 
                     ['1s', '2s', '3s', '4s', '4s', '4s'], ['2s', '3s', '4s', '5s', '5s', '5s'], ['3s', '4s', '5s', '6s', '6s', '6s'], ['4s', '5s', '6s', '7s', '7s', '7s'], ['5s', '6s', '7s', '8s', '8s', '8s'], ['6s', '7s', '8s', '9s', '9s', '9s'],    
                    ] and self.TiToi == 0:
                print('六つ系：連続両面 or 暗刻＋面子 ')
                print(' ', l)
                if i in Muttsu:
                    Muttsu.remove(i)  
                    if j in Muttsu:
                        Muttsu.remove(j)        
                        if k in Muttsu:
                            Muttsu.remove(k)
                            if m in Muttsu:
                                Muttsu.remove(m)
                                if n in Muttsu:
                                    Muttsu.remove(n)
                                    if o in Muttsu:
                                        Select.remove(i)
                                        Select.remove(j)
                                        Select.remove(k)
                                        Select.remove(m)
                                        Select.remove(n)
                                        Select.remove(o)
                                        MemberCheck += 2

        # 五つ系（１－１）槓子があり、暗刻とターツで使うケース
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            # print(l)
            Kantsu = copy.deepcopy(Select)
            if l in [['1m', '2m', '2m', '2m', '2m'], ['2m', '2m', '2m', '2m', '3m'], 
                    ['2m', '3m', '3m', '3m', '3m'], ['3m', '3m', '3m', '3m', '4m'], ['3m', '4m', '4m', '4m', '4m'], ['4m', '4m', '4m', '4m', '5m'], 
                    ['4m', '5m', '5m', '5m', '5m'], ['5m', '5m', '5m', '5m', '6m'], ['5m', '6m', '6m', '6m', '6m'], ['6m', '6m', '6m', '6m', '7m'],
                    ['6m', '7m', '7m', '7m', '7m'], ['7m', '7m', '7m', '7m', '8m'], ['7m', '8m', '8m', '8m', '8m'], ['8m', '8m', '8m', '8m', '9m'],
                    ['1p', '2p', '2p', '2p', '2p'], ['2p', '2p', '2p', '2p', '3p'], 
                    ['2p', '3p', '3p', '3p', '3p'], ['3p', '3p', '3p', '3p', '4p'], ['3p', '4p', '4p', '4p', '4p'], ['4p', '4p', '4p', '4p', '5p'], 
                    ['4p', '5p', '5p', '5p', '5p'], ['5p', '5p', '5p', '5p', '6p'], ['5p', '6p', '6p', '6p', '6p'], ['6p', '6p', '6p', '6p', '7p'],
                    ['6p', '7p', '7p', '7p', '7p'], ['7p', '7p', '7p', '7p', '8p'], ['7p', '8p', '8p', '8p', '8p'], ['8p', '8p', '8p', '8p', '9p'],
                    ['1m', '2s', '2s', '2s', '2s'], ['2s', '2s', '2s', '2s', '3s'],
                    ['2s', '3s', '3s', '3s', '3s'], ['3s', '3s', '3s', '3s', '4s'], ['3s', '4s', '4s', '4s', '4s'], ['4s', '4s', '4s', '4s', '5s'], 
                    ['4s', '5s', '5s', '5s', '5s'], ['5s', '5s', '5s', '5s', '6s'], ['5s', '6s', '6s', '6s', '6s'], ['6s', '6s', '6s', '6s', '7s'],
                    ['6s', '7s', '7s', '7s', '7s'], ['7s', '7s', '7s', '7s', '8s'], ['7s', '8s', '8s', '8s', '8s'], ['8s', '8s', '8s', '8s', '9s']
                    ] and self.TiToi == 0:
                print('槓子(暗刻＋両面): ')
                print(' ', l)
                if j in Kantsu:
                    Kantsu.remove(j)           
                    if k in Kantsu:
                        Kantsu.remove(k)
                        if m in Kantsu:
                            Kantsu.remove(m)
                            # ターツを残すため、真ん中３つを除く
                            # Select.remove(i)
                            Select.remove(j)
                            Select.remove(k)
                            Select.remove(m)
                            # Select.remove(n)
                            MemberCheck += 1

        # 槓子対応（１－２）---- しばらくは、カンはしない運用
        for i, j, k, m in list(it.combinations(Select, 4)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            if l in [['1m', '1m', '1m', '1m'], ['2m', '2m', '2m', '2m'], ['3m', '3m', '3m', '3m'], ['4m', '4m', '4m', '4m'], ['5m', '5m', '5m', '5m'], 
                     ['6m', '6m', '6m', '6m'], ['7m', '7m', '7m', '7m'], ['8m', '8m', '8m', '8m'], ['9m', '9m', '9m', '9m'], 
                     ['1p', '1p', '1p', '1p'], ['2p', '2p', '2p', '2p'], ['3p', '3p', '3p', '3p'], ['4p', '4p', '4p', '4p'], ['5p', '5p', '5p', '5p'], 
                     ['6p', '6p', '6p', '6p'], ['7p', '7p', '7p', '7p'], ['8p', '8p', '8p', '8p'], ['9p', '9p', '9p', '9p'], 
                     ['1s', '1s', '1s', '1s'], ['2s', '2s', '2s', '2s'], ['3s', '3s', '3s', '3s'], ['4s', '4s', '4s', '4s'], ['5s', '5s', '5s', '5s'], 
                     ['6s', '6s', '6s', '6s'], ['7s', '7s', '7s', '7s'], ['8s', '8s', '8s', '8s'], ['9s', '9s', '9s', '9s'], 
                     ['E', 'E', 'E', 'E'], ['S', 'S', 'S', 'S'], ['We', 'We', 'We', 'We'], ['N', 'N', 'N', 'N'], ['Wh', 'Wh', 'Wh', 'Wh'],
                     ['G', 'G', 'G', 'G'], ['R', 'R', 'R', 'R']
                    ] and self.TiToi == 0:
                print('槓子(暗刻抽出): ')
                print(' ', l)
                if j in Kantsu:
                    Kantsu.remove(j)
                if j not in Kantsu:
                    continue            
                if k in Kantsu:
                    Kantsu.remove(k)
                if k not in Kantsu:
                    continue
                if m in Kantsu:
                    Select.remove(j)
                    Select.remove(k)
                    Select.remove(m)
                    # Select.remove(n)
                    MemberCheck += 1
                if m not in Kantsu:
                    continue

        # 五つ系（２）3面チャン
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['2m', '3m', '4m', '5m', '6m'], ['3m', '4m', '5m', '6m', '7m'], ['4m', '5m', '6m', '7m', '8m'], 
                     ['2p', '3p', '4p', '5p', '6p'], ['3p', '4p', '5p', '6p', '7p'], ['4p', '5p', '6p', '7p', '8p'], 
                     ['2s', '3s', '4s', '5s', '6s'], ['3s', '4s', '5s', '6s', '7s'], ['4s', '5s', '6s', '7s', '8s']
                    ] and self.TiToi == 0:
                print('3面チャン')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                # 面子数が３つで、残り５牌で、全部残すとエラーになるので、、、、三暗刻を諦める。
                    if FourFlg != True or FourPiece >= 1:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                        FourPiece += 1
                    MemberCheck += 1

        # 五つ系（３）両面被り ---右側面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['2m', '3m', '3m', '4m', '5m'], ['3m', '4m', '4m', '5m', '6m'], ['4m', '5m', '5m', '6m', '7m'], ['5m', '6m', '6m', '7m', '8m'], ['6m', '7m', '7m', '8m', '9m'],
                    ['2p', '3p', '3p', '4p', '5p'], ['3p', '4p', '4p', '5p', '6p'], ['4p', '5p', '5p', '6p', '7p'], ['5p', '6p', '6p', '7p', '8p'], ['6p', '7p', '7p', '8p', '9p'],
                    ['2s', '3s', '3s', '4s', '5s'], ['3s', '4s', '4s', '5s', '6s'], ['4s', '5s', '5s', '6s', '7s'], ['5s', '6s', '6s', '7s', '8s'], ['6s', '7s', '7s', '8s', '9s'],
                    ] and self.TiToi == 0:
                print('両面被り--右面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        # Select.remove(i)
                        # Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        Select.remove(i)
                        Select.remove(j)
                        # Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                        FourPiece += 1
                    MemberCheck += 1
        
        # 五つ系（４）両面被り ---左側面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '2m', '3m', '3m', '4m'], ['2m', '3m', '4m', '4m', '5m'], ['3m', '4m', '5m', '5m', '6m'], ['4m', '5m', '6m', '6m', '7m'], ['5m', '6m', '7m', '7m', '8m'],
                    ['1p', '2p', '3p', '3p', '4p'], ['2p', '3p', '4p', '4p', '5p'], ['3p', '4p', '5p', '5p', '6p'], ['4p', '5p', '6p', '6p', '7p'], ['5p', '6p', '7p', '7p', '8p'],
                    ['1s', '2s', '3s', '3s', '4s'], ['2s', '3s', '4s', '4s', '5s'], ['3s', '4s', '5s', '5s', '6s'], ['4s', '5s', '6s', '6s', '7s'], ['5s', '6s', '7s', '7s', '8s']
                    ] and self.TiToi == 0:
                print('両面被り--左面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    # 面子牌を残す。
                    if FourFlg != True or FourPiece >= 1:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        # Select.remove(m)
                        # Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        # Select.remove(m)
                        Select.remove(n)
                        FourPiece += 1
                    MemberCheck += 1
        
        # 五つ系（５）右端5枚
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['5m', '6m', '7m', '8m', '9m'], 
                     ['5p', '6p', '7p', '8p', '9p'],
                     ['5s', '6s', '7s', '8s', '9s']
                    ] and self.TiToi == 0:
                print('5つ系-右端5枚-右面子救済: ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        # Select.remove(i)
                        # Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        # どちらを除くかは、もう少し考慮しても良い。ここでは赤引きとタンヤオを考慮して。乱数でもいいかも。
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                        FourPiece += 1
                    MemberCheck += 1

        # 五つ系（５）左端5枚
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '2m', '3m', '4m', '5m'], 
                     ['1p', '2p', '3p', '4p', '5p'], 
                     ['1s', '2s', '3s', '4s', '5s']
                    ] and self.TiToi == 0:
                print('5つ系-左端5枚-左面子救済: ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                # 面子数が３つで、残り５牌で、全部残すとエラーになるので、、、、三暗刻を諦める。
                    if FourFlg != True or FourPiece >= 1:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        # Select.remove(m)
                        # Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        # どちらを除くかは、もう少し考慮しても良い。ここでは赤引きとタンヤオを考慮して。乱数でもいいかも。
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                        FourPiece += 1
                    MemberCheck += 1

        # 五つ系（６）複合形から面子部位が除去されないように 右3つを救済
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '1m', '3m', '4m', '5m'], ['2m', '2m', '4m', '5m', '6m'], ['3m', '3m', '5m', '6m', '7m'], ['4m', '4m', '6m', '7m', '8m'], ['5m', '5m', '7m', '8m', '9m'], 
                     ['1m', '3m', '5m', '6m', '7m'], ['2m', '4m', '6m', '7m', '8m'], ['3m', '5m', '7m', '8m', '9m'], 
                     ['1m', '1m', '2m', '3m', '4m'], ['2m', '2m', '3m', '4m', '5m'], ['3m', '3m', '4m', '5m', '6m'], ['4m', '4m', '5m', '6m', '7m'], ['5m', '5m', '6m', '7m', '8m'], ['6m', '6m', '7m', '8m', '9m'],
                     ['1p', '1p', '3p', '4p', '5p'], ['2p', '2p', '4p', '5p', '6p'], ['3p', '3p', '5p', '6p', '7p'], ['4p', '4p', '6p', '7p', '8p'], ['5p', '5p', '7p', '8p', '9p'], 
                     ['1p', '3p', '5p', '6p', '7p'], ['2p', '4p', '6p', '7p', '8p'], ['3p', '5p', '7p', '8p', '9p'], 
                     ['1p', '1p', '2p', '3p', '4p'], ['2p', '2p', '3p', '4p', '5p'], ['3p', '3p', '4p', '5p', '6p'], ['4p', '4p', '5p', '6p', '7p'], ['5p', '5p', '6p', '7p', '8p'], ['6p', '6p', '7p', '8p', '9p'],
                     ['1s', '1s', '3s', '4s', '5s'], ['2s', '2s', '4s', '5s', '6s'], ['3s', '3s', '5s', '6s', '7s'], ['4s', '4s', '6s', '7s', '8s'], ['5s', '5s', '7s', '8s', '9s'], 
                     ['1s', '3s', '5s', '6s', '7s'], ['2s', '4s', '6s', '7s', '8s'], ['3s', '5s', '7s', '8s', '9s'], 
                     ['1s', '1s', '2s', '3s', '4s'], ['2s', '2s', '3s', '4s', '5s'], ['3s', '3s', '4s', '5s', '6s'], ['4s', '4s', '5s', '6s', '7s'], ['5s', '5s', '6s', '7s', '8s'], ['6s', '6s', '7s', '8s', '9s'],
                    ] and self.TiToi == 0:
                print('5つ系-右面子救済: ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    # Select.remove(i)
                    # Select.remove(j)
                    Select.remove(k)
                    Select.remove(m)
                    Select.remove(n)
                    MemberCheck += 1

        # 五つ系（７）複合形から面子部位が除去されないように 左3つを救済
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '2m', '3m', '5m', '5m'], ['2m', '3m', '4m', '6m', '6m'], ['3m', '4m', '5m', '7m', '7m'], ['4m', '5m', '6m', '8m', '8m'], ['5m', '6m', '7m', '9m', '9m'], 
                     ['1m', '2m', '3m', '5m', '7m'], ['2m', '3m', '4m', '6m', '8m'], ['3m', '4m', '5m', '7m', '9m'], 
                     ['1m', '2m', '3m', '4m', '4m'], ['2m', '3m', '4m', '5m', '5m'], ['3m', '4m', '5m', '6m', '6m'], ['4m', '5m', '6m', '7m', '7m'], ['5m', '6m', '7m', '8m', '8m'], ['6m', '7m', '8m', '9m', '9m'],
                     ['1p', '2p', '3p', '5p', '5p'], ['2p', '3p', '4p', '6p', '6p'], ['3p', '4p', '5p', '7p', '7p'], ['4p', '5p', '6p', '8p', '8p'], ['5p', '6p', '7p', '9p', '9p'], 
                     ['1p', '2p', '3p', '5p', '7p'], ['2p', '3p', '4p', '6p', '8p'], ['3p', '4p', '5p', '7p', '9p'], 
                     ['1p', '2p', '3p', '4p', '4p'], ['2p', '3p', '4p', '5p', '5p'], ['3p', '4p', '5p', '6p', '6p'], ['4p', '5p', '6p', '7p', '7p'], ['5p', '6p', '7p', '8p', '8p'], ['6p', '7p', '8p', '9p', '9p'],
                     ['1s', '2s', '3s', '5s', '5s'], ['2s', '3s', '4s', '6s', '6s'], ['3s', '4s', '5s', '7s', '7s'], ['4s', '5s', '6s', '8s', '8s'], ['5s', '6s', '7s', '9s', '9s'], 
                     ['1s', '2s', '3s', '5s', '7s'], ['2s', '3s', '4s', '6s', '8s'], ['3s', '4s', '5s', '7s', '9s'], 
                     ['1s', '2s', '3s', '4s', '4s'], ['2s', '3s', '4s', '5s', '5s'], ['3s', '4s', '5s', '6s', '6s'], ['4s', '5s', '6s', '7s', '7s'], ['5s', '6s', '7s', '8s', '8s'], ['6s', '7s', '8s', '9s', '9s'],
                    ] and self.TiToi == 0:
                print('5つ形-左面子救済: ')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    Select.remove(i)
                    Select.remove(j)
                    Select.remove(k)
                    # Select.remove(m)
                    # Select.remove(n)
                    MemberCheck += 1

         # 五つ系（８）カンチャン＋四連形--右面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '3m', '4m', '5m', '6m'], 
                    ['1p', '3p', '4p', '5p', '6p'], 
                    ['1s', '3s', '4s', '5s', '6s']
                    ] and self.TiToi == 0:
                print('カンチャン＋四連形--右面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        # Select.remove(i)
                        # Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    MemberCheck += 1
        
        # 五つ系（９）四連形＋カンチャン--左面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['4m', '5m', '6m', '7m', '9m'],
                    ['4p', '5p', '6p', '7p', '9p'],
                    ['4s', '5s', '6s', '7s', '9s'],
                    ] and self.TiToi == 0:
                print('四連形＋カンチャン--左面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        # Select.remove(m)
                        # Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                    MemberCheck += 1

        # 五つ系（１０）カンチャン＋四連形１ ---センター面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['1m', '2m', '3m', '4m', '6m'], ['2m', '3m', '4m', '5m', '7m'], ['3m', '4m', '5m', '6m', '8m'],
                     ['1p', '2p', '3p', '4p', '6p'], ['2p', '3p', '4p', '5p', '7p'], ['3p', '4p', '5p', '6p', '8p'], 
                     ['1s', '2s', '3s', '4s', '6s'], ['2s', '3s', '4s', '5s', '7s'], ['3s', '4s', '5s', '6s', '8s']
                    ] and self.TiToi == 0:
                print('四連形＋カンチャン１--センター面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                    MemberCheck += 1

        # 五つ系（１１）カンチャン＋四連形２ ---センター面子残し
        for i, j, k, m, n in list(it.combinations(Select, 5)):
            l = []
            l.append(i)
            l.append(j)
            l.append(k)
            l.append(m)
            l.append(n)
            if l in [['2m', '4m', '5m', '6m', '7m'], ['3m', '5m', '6m', '7m', '8m'], ['4m', '6m', '7m', '8m', '9m'],
                     ['2p', '4p', '5p', '6p', '7p'], ['3p', '5p', '6p', '7p', '8p'], ['4p', '6p', '7p', '8p', '9p'],
                     ['2s', '4s', '5s', '6s', '7s'], ['3s', '5s', '6s', '7s', '8s'], ['4s', '6s', '7s', '8s', '9s'],
                    ] and self.TiToi == 0:
                print('四連形＋カンチャン２--センター面子残し')
                print(' ', l)
                if i in Select and j in Select and k in Select and m in Select and n in Select:
                    if FourFlg != True or FourPiece >= 1:
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # Select.remove(n)
                    if FourFlg == True and FourPiece == 0:
                        # Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        Select.remove(n)
                    MemberCheck += 1

        # 四つ系（１） 暗刻くっつき
        if len(Select) >= 5 and FourFlg == True:
            for i, j, k, m in list(it.combinations(Select, 4)):
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                l.append(m)
                # print(l)
                # 残さない形：
                # ['1m', '1m', '1m', '2m'], ['1m', '2m', '2m', '2m'], ['1m', '3m', '3m', '3m'], ['2m', '4m', '4m', '4m'], ['6m', '6m', '6m', '8m'], ['7m', '7m', '7m', '9m'], ['8m', '9m', '9m', '9m'], ['8m', '8m', '8m', '9m'],
                if l in [['1m', '1m', '1m', '3m'], ['2m', '2m', '2m', '3m'], ['2m', '2m', '2m', '4m'], ['3m', '3m', '3m', '4m'], ['3m', '3m', '3m', '5m'], ['2m', '3m', '3m', '3m'],
                        ['4m', '4m', '4m', '5m'], ['4m', '4m', '4m', '6m'], ['3m', '4m', '4m', '4m'], ['5m', '5m', '5m', '6m'], ['5m', '5m', '5m', '7m'], ['3m', '5m', '5m', '5m'], 
                        ['4m', '5m', '5m', '5m'], ['6m', '6m', '6m', '7m'], ['4m', '6m', '6m', '6m'], ['5m', '6m', '6m', '6m'], ['7m', '7m', '7m', '8m'], ['5m', '7m', '7m', '7m'],
                        ['6m', '7m', '7m', '7m'], ['6m', '8m', '8m', '8m'], ['7m', '8m', '8m', '8m'], ['7m', '9m', '9m', '9m'],
                        ['1p', '1p', '1p', '3p'], ['2p', '2p', '2p', '3p'], ['2p', '2p', '2p', '4p'], ['3p', '3p', '3p', '4p'], ['3p', '3p', '3p', '5p'], ['2p', '3p', '3p', '3p'],
                        ['4p', '4p', '4p', '5p'], ['4p', '4p', '4p', '6p'], ['3p', '4p', '4p', '4p'], ['5p', '5p', '5p', '6p'], ['5p', '5p', '5p', '7p'], ['3p', '5p', '5p', '5p'], 
                        ['4p', '5p', '5p', '5p'], ['6p', '6p', '6p', '7p'], ['4p', '6p', '6p', '6p'], ['5p', '6p', '6p', '6p'], ['7p', '7p', '7p', '8p'], ['5p', '7p', '7p', '7p'],
                        ['6p', '7p', '7p', '7p'], ['6p', '8p', '8p', '8p'], ['7p', '8p', '8p', '8p'], ['7p', '9p', '9p', '9p'],
                        ['1s', '1s', '1s', '3s'], ['2s', '2s', '2s', '3s'], ['2s', '2s', '2s', '4s'], ['3s', '3s', '3s', '4s'], ['3s', '3s', '3s', '5s'], ['2s', '3s', '3s', '3s'],
                        ['4s', '4s', '4s', '5s'], ['4s', '4s', '4s', '6s'], ['3s', '4s', '4s', '4s'], ['5s', '5s', '5s', '6s'], ['5s', '5s', '5s', '7s'], ['3s', '5s', '5s', '5s'], 
                        ['4s', '5s', '5s', '5s'], ['6s', '6s', '6s', '7s'], ['4s', '6s', '6s', '6s'], ['5s', '6s', '6s', '6s'], ['7s', '7s', '7s', '8s'], ['5s', '7s', '7s', '7s'],
                        ['6s', '7s', '7s', '7s'], ['6s', '8s', '8s', '8s'], ['7s', '8s', '8s', '8s'], ['7s', '9s', '9s', '9s'],
                        ] and self.TiToi == 0 and FourPiece == 0:
                    FourPiece += 1
                    print('暗刻くっつき: ')
                    print(' ', l)
                    # ５＋５＋４のケースもあるので、break を入れておく。
                    if len(Select) <= 4:
                        break
                    if i in Select and j in Select and k in Select and m in Select:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        MemberCheck += 1


        # 四つ系（２）優先順位にそってノベタン形を並び替え
        if len(Select) >= 5 and FourFlg == True:
            self.SortRule2 = [['3m', '4m', '5m', '6m'], ['4m', '5m', '6m', '7m'], ['2m', '3m', '4m', '5m'], ['5m', '6m', '7m', '8m'], ['1m', '2m', '3m', '4m'], ['6m', '7m', '8m', '9m'],
                    ['3p', '4p', '5p', '6p'], ['4p', '5p', '6p', '7p'], ['2p', '3p', '4p', '5p'], ['5p', '6p', '7p', '8p'], ['1p', '2p', '3p', '4p'], ['6p', '7p', '8p', '9p'],
                    ['3s', '4s', '5s', '6s'], ['4s', '5s', '6s', '7s'], ['2s', '3s', '4s', '5s'], ['5s', '6s', '7s', '8s'], ['1s', '2s', '3s', '4s'], ['6s', '7s', '8s', '9s'],
                    ]

            Mentsu = []
            for y in range(len(self.SortRule2)):
                for i, j, k, m in list(it.combinations(Select, 4)):
                    l = []
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    l.append(m)
                    if l == self.SortRule2[y]:
                        Mentsu.append(l)

            Mentsu = sorted(Mentsu, key = self.SortRule2.index)
            
            for i, j, k, m in Mentsu:
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                l.append(m)
                if l in [['3m', '4m', '5m', '6m'], ['4m', '5m', '6m', '7m'], ['2m', '3m', '4m', '5m'], ['5m', '6m', '7m', '8m'], ['1m', '2m', '3m', '4m'], ['6m', '7m', '8m', '9m'],
                            ['3p', '4p', '5p', '6p'], ['4p', '5p', '6p', '7p'], ['2p', '3p', '4p', '5p'], ['5p', '6p', '7p', '8p'], ['1p', '2p', '3p', '4p'], ['6p', '7p', '8p', '9p'],
                            ['3s', '4s', '5s', '6s'], ['4s', '5s', '6s', '7s'], ['2s', '3s', '4s', '5s'], ['5s', '6s', '7s', '8s'], ['1s', '2s', '3s', '4s'], ['6s', '7s', '8s', '9s'],
                            ] and self.TiToi == 0 and FourPiece == 0:
                    FourPiece += 1
                    print('ノベタン: ')
                    print(' ', l)
                    # ５＋５＋４のケースもあるので、break を入れておく。
                    if len(Select) <= 4:
                        break
                    if i in Select and j in Select and k in Select and m in Select:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        MemberCheck += 1           

        # 面子チェック(３つ系)  優先順位にそって
        if len(Select) >= 4:
            self.SortRule3 = [['4m', '5m', '6m'], ['3m', '4m', '5m'], ['5m', '6m', '7m'], ['2m', '3m', '4m'], ['6m', '7m', '8m'], ['1m', '2m', '3m'], ['7m', '8m', '9m'],
                                    ['4p', '5p', '6p'], ['3p', '4p', '5p'], ['5p', '6p', '7p'], ['2p', '3p', '4p'], ['6p', '7p', '8p'], ['1p', '2p', '3p'], ['7p', '8p', '9p'],
                                    ['4s', '5s', '6s'], ['3s', '4s', '5s'], ['5s', '6s', '7s'], ['2s', '3s', '4s'], ['6s', '7s', '8s'], ['1s', '2s', '3s'], ['7s', '8s', '9s']
                                    ]
            Mentsu = []
            for y in range(len(self.SortRule3)):
                for i, j, k in list(it.combinations(Select, 3)):
                    l = []
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    if l == self.SortRule3[y]:
                        Mentsu.append(l)

            Mentsu = sorted(Mentsu, key = self.SortRule3.index)
            
            for i, j, k in Mentsu:
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                if l in [['4m', '5m', '6m'], ['3m', '4m', '5m'], ['5m', '6m', '7m'], ['2m', '3m', '4m'], ['6m', '7m', '8m'], ['1m', '2m', '3m'], ['7m', '8m', '9m'],
                        ['4p', '5p', '6p'], ['3p', '4p', '5p'], ['5p', '6p', '7p'], ['2p', '3p', '4p'], ['6p', '7p', '8p'], ['1p', '2p', '3p'], ['7p', '8p', '9p'],
                        ['4s', '5s', '6s'], ['3s', '4s', '5s'], ['5s', '6s', '7s'], ['2s', '3s', '4s'], ['6s', '7s', '8s'], ['1s', '2s', '3s'], ['7s', '8s', '9s']
                        ] and self.TiToi == 0:
                    print('面子: ', l)
                    if len(Select) <= 3:
                        break
                    if i in Select and j in Select and k in Select:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        MemberCheck += 1

        # 四つ系（３）変則3面形からターツが除去されないように 右2つを救済
        if len(Select) >= 5:
            for i, j, k, m in list(it.combinations(Select, 4)):
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                l.append(m)
                # print(l)
                if l in [['1m', '1m', '3m', '4m'], ['2m', '2m', '4m', '5m'], ['3m', '3m', '5m', '6m'], ['4m', '4m', '6m', '7m'], ['5m', '5m', '7m', '8m'], 
                        ['1m', '3m', '5m', '6m'], ['2m', '4m', '6m', '7m'], ['3m', '5m', '7m', '8m'], 
                        ['1p', '1p', '3p', '4p'], ['2p', '2p', '4p', '5p'], ['3p', '3p', '5p', '6p'], ['4p', '4p', '6p', '7p'], ['5p', '5p', '7p', '8p'], 
                        ['1p', '3p', '5p', '6p'], ['2p', '4p', '6p', '7p'], ['3p', '5p', '7p', '8p'],
                        ['1s', '1s', '3s', '4s'], ['2s', '2s', '4s', '5s'], ['3s', '3s', '5s', '6s'], ['4s', '4s', '6s', '7s'], ['5s', '5s', '7s', '8s'], 
                        ['1s', '3s', '5s', '6s'], ['2s', '4s', '6s', '7s'], ['3s', '5s', '7s', '8s']
                        ] and self.TiToi == 0:
                    print('変則3面形-右ターツ救済: ')
                    print(' ', l)
                    # ５＋５＋４のケースもあるので、break を入れておく。
                    if len(Select) <= 4:
                        break
                    if i in Select and j in Select and k in Select and m in Select:
                        # Select.remove(i)
                        # Select.remove(j)
                        Select.remove(k)
                        Select.remove(m)
                        # ターツを加える
                        TartsCheck += 1

        # 四つ系（４）変則3面形からターツが除去されないように 左2つを救済
        if len(Select) >= 5:
            for i, j, k, m in list(it.combinations(Select, 4)):
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                l.append(m)
                if l in [['2m', '3m', '5m', '5m'], ['3m', '4m', '6m', '6m'], ['4m', '5m', '7m', '7m'], ['5m', '6m', '8m', '8m'], ['6m', '7m', '9m', '9m'], 
                        ['2m', '3m', '5m', '7m'], ['3m', '4m', '6m', '8m'], ['4m', '5m', '7m', '9m'], 
                        ['2p', '3p', '5p', '5p'], ['3p', '4p', '6p', '6p'], ['4p', '5p', '7p', '7p'], ['5p', '6p', '8p', '8p'], ['6p', '7p', '9p', '9p'], 
                        ['2p', '3p', '5p', '7p'], ['3p', '4p', '6p', '8p'], ['4p', '5p', '7p', '9p'], 
                        ['2s', '3s', '5s', '5s'], ['3s', '4s', '6s', '6s'], ['4s', '5s', '7s', '7s'], ['5s', '6s', '8s', '8s'], ['6s', '7s', '9s', '9s'], 
                        ['2s', '3s', '5s', '7s'], ['3s', '4s', '6s', '8s'], ['4s', '5s', '7s', '9s']
                        ] and self.TiToi == 0:
                    print('変則3面形-左ターツ救済: ')
                    print(' ', l)
                    # ５＋５＋４のケースもあるので、break を入れておく。
                    if len(Select) <= 4:
                        break
                    if i in Select and j in Select and k in Select and m in Select:
                        Select.remove(i)
                        Select.remove(j)
                        # Select.remove(k)
                        # Select.remove(m)
                        # ターツを加える
                        TartsCheck += 1

        # 暗刻チェック(３つ系)
        if len(Select) >= 4:
            for i, j, k in list(it.combinations(Select, 3)):
                l = []
                l.append(i)
                l.append(j)
                l.append(k)
                if l in [['1m', '1m', '1m'], ['2m', '2m', '2m'], ['3m', '3m', '3m'], ['4m', '4m', '4m'], 
                        ['5m', '5m', '5m'], ['6m', '6m', '6m'], ['7m', '7m', '7m'], ['8m', '8m', '8m'], ['9m', '9m', '9m'],
                        ['1p', '1p', '1p'], ['2p', '2p', '2p'], ['3p', '3p', '3p'], ['4p', '4p', '4p'], 
                        ['5p', '5p', '5p'], ['6p', '6p', '6p'], ['7p', '7p', '7p'], ['8p', '8p', '8p'], ['9p', '9p', '9p'],
                        ['1s', '1s', '1s'], ['2s', '2s', '2s'], ['3s', '3s', '3s'], ['4s', '4s', '4s'], 
                        ['5s', '5s', '5s'], ['6s', '6s', '6s'], ['7s', '7s', '7s'], ['8s', '8s', '8s'], ['9s', '9s', '9s'],
                        ['E', 'E', 'E'], ['S', 'S', 'S'], ['We', 'We', 'We'], ['N', 'N', 'N'], 
                        ['Wh', 'Wh', 'Wh'], ['G', 'G', 'G'], ['R', 'R', 'R']
                        ]  and self.TiToi == 0:
                    print('暗刻: ', l)
                    if len(Select) <= 3:
                        break
                    if i in Select and j in Select and k in Select:
                        Select.remove(i)
                        Select.remove(j)
                        Select.remove(k)
                        MemberCheck += 1

        return Select, MemberCheck, TartsCheck

    # 切る牌を選択する関数, 面子を抽出した後の選択方法
    def SecondSelection(self, Select, HeadNumber):
        # For Head Selection
        TartsCheck = 0

        # 一向聴までは考慮する。３連トイツ形。
        if (self.Member == 0 or self.Member == 1 or self.Member == 2) and self.TiToi == 0:
            # 五つ系（７）三連対子
            if len(Select) >= 6:
                for i, j, k, m, n in list(it.combinations(Select, 5)):
                    l = []
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    l.append(m)
                    l.append(n)
                    if l in [['1m', '1m', '3m', '5m', '5m'], ['2m', '2m', '4m', '6m', '6m'], ['3m', '3m', '5m', '7m', '7m'], ['4m', '4m', '6m', '8m', '8m'], ['5m', '5m', '7m', '9m', '9m'], 
                            ['1p', '1p', '3p', '5p', '5p'], ['2p', '2p', '4p', '6p', '6p'], ['3p', '3p', '5p', '7p', '7p'], ['4p', '4p', '6p', '8p', '8p'], ['5p', '5p', '7p', '9p', '9p'], 
                            ['1s', '1s', '3s', '5s', '5s'], ['2s', '2s', '4s', '6s', '6s'], ['3s', '3s', '5s', '7s', '7s'], ['4s', '4s', '6s', '8s', '8s'], ['5s', '5s', '7s', '9s', '9s']
                            ] and self.TiToi == 0:
                        print('三連対子: ')
                        print(' ', l)
                        if i in Select and j in Select and k in Select and m in Select and n in Select:
                            Select.remove(i)
                            Select.remove(j)
                            Select.remove(k)
                            Select.remove(m)
                            Select.remove(n)
                            # MemberCheck += 1
                            # 念の為、一度だけの処理にする。
                            break

        # 一向聴までは残したい変則3枚形
        if (self.Member == 0 or self.Member == 1 or self.Member == 2) and self.TiToi == 0:
            if len(Select) >= 4:
                for i, j, k in list(it.combinations(Select, 3)):
                    l = []
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    # print(l)
                    # [1,2,2] [1,3,3] は含めない
                    if l in [['1m', '1m', '2m'], ['1m', '1m', '3m'], ['2m', '2m', '3m'], ['2m', '2m', '4m'], ['2m', '3m', '3m'], ['2m', '4m', '4m'],
                            ['3m', '3m', '4m'], ['3m', '3m', '5m'], ['3m', '4m', '4m'], ['3m', '5m', '5m'], ['4m', '4m', '5m'], ['4m', '4m', '6m'], ['4m', '5m', '5m'], ['4m', '6m', '6m'],
                            ['5m', '5m', '6m'], ['5m', '5m', '7m'], ['5m', '6m', '6m'], ['5m', '7m', '7m'], ['6m', '6m', '7m'], ['6m', '6m', '8m'], ['6m', '7m', '7m'], ['6m', '8m', '8m'],
                            ['7m', '7m', '8m'], ['7m', '8m', '8m'], ['7m', '9m', '9m'], ['8m', '9m', '9m'],
                            ['1m', '3m', '5m'], ['2m', '4m', '6m'], ['3m', '5m', '7m'], ['4m', '6m', '8m'], ['5m', '7m', '9m'], 
                            ['1p', '1p', '2p'], ['1p', '1p', '3p'], ['2p', '2p', '3p'], ['2p', '2p', '4p'], ['2p', '3p', '3p'], ['2p', '4p', '4p'],
                            ['3p', '3p', '4p'], ['3p', '3p', '5p'], ['3p', '4p', '4p'], ['3p', '5p', '5p'], ['4p', '4p', '5p'], ['4p', '4p', '6p'], ['4p', '5p', '5p'], ['4p', '6p', '6p'],
                            ['5p', '5p', '6p'], ['5p', '5p', '7p'], ['5p', '6p', '6p'], ['5p', '7p', '7p'], ['6p', '6p', '7p'], ['6p', '6p', '8p'], ['6p', '7p', '7p'], ['6p', '8p', '8p'],
                            ['7p', '7p', '8p'], ['7p', '8p', '8p'], ['7p', '9p', '9p'], ['8p', '9p', '9p'],
                            ['1p', '3p', '5p'], ['2p', '4p', '6p'], ['3p', '5p', '7p'], ['4p', '6p', '8p'], ['5p', '7p', '9p'], 
                            ['1s', '1s', '2s'], ['1s', '1s', '3s'], ['2s', '2s', '3s'], ['2s', '2s', '4s'], ['2s', '3s', '3s'], ['2s', '4s', '4s'],
                            ['3s', '3s', '4s'], ['3s', '3s', '5s'], ['3s', '4s', '4s'], ['3s', '5s', '5s'], ['4s', '4s', '5s'], ['4s', '4s', '6s'], ['4s', '5s', '5s'], ['4s', '6s', '6s'],
                            ['5s', '5s', '6s'], ['5s', '5s', '7s'], ['5s', '6s', '6s'], ['5s', '7s', '7s'], ['6s', '6s', '7s'], ['6s', '6s', '8s'], ['6s', '7s', '7s'], ['6s', '8s', '8s'],
                            ['7s', '7s', '8s'], ['7s', '8s', '8s'], ['7s', '9s', '9s'], ['8s', '9s', '9s'],
                            ['1s', '3s', '5s'], ['2s', '4s', '6s'], ['3s', '5s', '7s'], ['4s', '6s', '8s'], ['5s', '7s', '9s']
                            ]:
                        print('変則3枚形: ', l)
                        SelectTmp = copy.deepcopy(Select)
                        if len(Select) <= 3:
                            break
                        if i in SelectTmp:
                            SelectTmp.remove(i)
                            if j in SelectTmp:
                                SelectTmp.remove(j)
                                if k in SelectTmp:
                                    Select.remove(i)
                                    Select.remove(j)
                                    Select.remove(k)

        # 対子が1個以下で、一向聴までは対子優先
        if HeadNumber <= 1 or self.TiToi == 1:
            self.SortRule = [['1m', '1m'], ['2m', '2m'], ['3m', '3m'], ['4m', '4m'], 
                        ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'], ['9m', '9m'],
                        ['1p', '1p'], ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], 
                        ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'], ['9p', '9p'],
                        ['1s', '1s'], ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], 
                        ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s'], ['9s', '9s'],
                        ['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], 
                        ['Wh', 'Wh'], ['G', 'G'], ['R', 'R'],
                        ['4m', '5m'], ['5m', '6m'], ['3m', '4m'], ['6m', '7m'], ['2m', '3m'], ['7m', '8m'], 
                        ['4p', '5p'], ['5p', '6p'], ['3p', '4p'], ['6p', '7p'], ['2p', '3p'], ['7p', '8p'], 
                        ['4s', '5s'], ['5s', '6s'], ['3s', '4s'], ['6s', '7s'], ['2s', '3s'], ['7s', '8s'], 
                        ['4m', '6m'], ['3m', '5m'], ['5m', '7m'], ['2m', '4m'], ['6m', '8m'], ['1m', '2m'], ['8m', '9m'], ['1m', '3m'], ['7m', '9m'], 
                        ['4p', '6p'], ['3p', '5p'], ['5p', '7p'], ['2p', '4p'], ['6p', '8p'], ['1p', '2p'], ['8p', '9p'], ['1p', '3p'], ['7p', '9p'], 
                        ['4s', '6s'], ['3s', '5s'], ['5s', '7s'], ['2s', '4s'], ['6s', '8s'], ['1s', '2s'], ['8s', '9s'], ['1s', '3s'], ['7s', '9s']
                        ]

        # 対子が２個以上あれば、両面優先
        if HeadNumber > 1 and self.TiToi != 1:
            self.SortRule = [['4m', '5m'], ['5m', '6m'], ['3m', '4m'], ['6m', '7m'], ['2m', '3m'], ['7m', '8m'], 
                        ['4p', '5p'], ['5p', '6p'], ['3p', '4p'], ['6p', '7p'], ['2p', '3p'], ['7p', '8p'], 
                        ['4s', '5s'], ['5s', '6s'], ['3s', '4s'], ['6s', '7s'], ['2s', '3s'], ['7s', '8s'],  
                        ['1m', '1m'], ['2m', '2m'], ['3m', '3m'], ['4m', '4m'], 
                        ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'], ['9m', '9m'],
                        ['1p', '1p'], ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], 
                        ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'], ['9p', '9p'],
                        ['1s', '1s'], ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], 
                        ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s'], ['9s', '9s'],
                        ['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], 
                        ['Wh', 'Wh'], ['G', 'G'], ['R', 'R'],
                        ['4m', '6m'], ['3m', '5m'], ['5m', '7m'], ['2m', '4m'], ['6m', '8m'], ['1m', '2m'], ['8m', '9m'], ['1m', '3m'], ['7m', '9m'], 
                        ['4p', '6p'], ['3p', '5p'], ['5p', '7p'], ['2p', '4p'], ['6p', '8p'], ['1p', '2p'], ['8p', '9p'], ['1p', '3p'], ['7p', '9p'], 
                        ['4s', '6s'], ['3s', '5s'], ['5s', '7s'], ['2s', '4s'], ['6s', '8s'], ['1s', '2s'], ['8s', '9s'], ['1s', '3s'], ['7s', '9s']
                        ]

        # 2個牌の処理
        Tarts = []
        if len(Select) >= 3:
            for k in range(len(self.SortRule)):
                for i, j in list(it.combinations(Select, 2)):
                    l = []
                    l.append(i)
                    l.append(j)
                    if l == self.SortRule[k]:
                        Tarts.append(l)
        
        Tarts = sorted(Tarts, key = self.SortRule.index)
        if self.TiToi == 1:
            print('七対子チェック用')

        # 槓子対策のため、HeadCheckList(重複なし対子リスト)を利用する。・・・
        Tmp_HeadCheckList = copy.deepcopy(self.HeadCheckList)
        # print('対子リスト: ', Tmp_HeadCheckList)

        if self.TiToi == 1:
            for l in Tmp_HeadCheckList:
                if l in [['1m', '1m'], ['2m', '2m'], ['3m', '3m'], ['4m', '4m'], 
                        ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'], ['9m', '9m'],
                        ['1p', '1p'], ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], 
                        ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'], ['9p', '9p'],
                        ['1s', '1s'], ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], 
                        ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s'], ['9s', '9s'],
                        ['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], 
                        ['Wh', 'Wh'], ['G', 'G'], ['R', 'R']
                        ]:
                    print('対子: ', l)
                    SelectTmp = copy.deepcopy(Select) 
                    if len(Select) <= 2:
                        break
                    if l[0] in SelectTmp:
                        SelectTmp.remove(l[0])
                        if l[1] in SelectTmp and len(SelectTmp) != 0:
                            Select.remove(l[0])
                            Select.remove(l[1])

        if self.TiToi != 1:
            for i, j in Tarts:
                l = []
                l.append(i)
                l.append(j)

                if l in [['1m', '1m'], ['2m', '2m'], ['3m', '3m'], ['4m', '4m'], 
                        ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'], ['9m', '9m'],
                        ['1p', '1p'], ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], 
                        ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'], ['9p', '9p'],
                        ['1s', '1s'], ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], 
                        ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s'], ['9s', '9s'],
                        ['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], 
                        ['Wh', 'Wh'], ['G', 'G'], ['R', 'R']
                        ]:
                    print('対子: ', l)
                    SelectTmp = copy.deepcopy(Select) 
                    if l in Tmp_HeadCheckList:
                        if len(Select) <= 2:
                            break
                        if i in SelectTmp:
                            SelectTmp.remove(i)
                            if j in SelectTmp and len(SelectTmp) != 0:
                                Select.remove(i)
                                Select.remove(j)
            
                if l in [['2m', '3m'], ['3m', '4m'], ['4m', '5m'], ['5m', '6m'], ['6m', '7m'], ['7m', '8m'], 
                        ['2p', '3p'], ['3p', '4p'], ['4p', '5p'], ['5p', '6p'], ['6p', '7p'], ['7p', '8p'], 
                        ['2s', '3s'], ['3s', '4s'], ['4s', '5s'], ['5s', '6s'], ['6s', '7s'], ['7s', '8s']
                        ]:
                    print('強塔子: ', l)
                    SelectTmp = copy.deepcopy(Select) 
                    if len(Select) <= 2:
                        break
                    if i in SelectTmp:
                        SelectTmp.remove(i)
                        if j in SelectTmp and len(SelectTmp) != 0:
                            Select.remove(i)
                            Select.remove(j)
                            TartsCheck += 1
                        # 強ターツは雀頭選択のアルゴリズムで考慮させたいので、出力しておく。
                        
                if l in [['1m', '2m'], ['1m', '3m'], ['2m', '4m'], ['3m', '5m'], ['4m', '6m'], ['5m', '7m'], ['6m', '8m'], ['7m', '9m'], ['8m', '9m'],
                        ['1p', '2p'], ['1p', '3p'], ['2p', '4p'], ['3p', '5p'], ['4p', '6p'], ['5p', '7p'], ['6p', '8p'], ['7p', '9p'], ['8p', '9p'],
                        ['1s', '2s'], ['1s', '3s'], ['2s', '4s'], ['3s', '5s'], ['4s', '6s'], ['5s', '7s'], ['6s', '8s'], ['7s', '9s'], ['8s', '9s']
                        ]:
                    print('弱塔子: ', l)
                    SelectTmp = copy.deepcopy(Select) 
                    if len(Select) <= 2:
                        break
                    if i in SelectTmp:
                        SelectTmp.remove(i)
                        if j in SelectTmp and len(SelectTmp) != 0:
                            Select.remove(i)
                            Select.remove(j)
                    
        return TartsCheck

    # 切る牌を選択する関数 return Results
    def SelectionExe(self, Arrangement, EscapeSouece, ReachBox, CareBox, Dora):
        Escape = EscapeSouece
        # print('Escape1: ', Escape)
        FinalMember = 0
        Select = copy.deepcopy(Arrangement)
        Select = sorted(Select, key = self.Name.index)
        # print('手牌 切る前: ', Select)

        self.HeadCheckList, self.TiToi = O.PreliminarySelection(Select)

        # ヘッドを最初に考慮する場合（手が込んでくると効果を発揮する）
        print('１－雀頭考慮')
        # 面子数カウントのリセット
        self.Member = 0
        Head_Index = 0
        Head_Index_Another = None
        TrueSelect = None

        if len(self.HeadCheckList) != 0:
            MaxMember = 0
            HeadDic = {}
            HeadDicTanyao = {}

            # ★雀頭を厳密に選択するアルゴリズムは難しそうなので、とりあえず、ランダムにする。
            random.shuffle(self.HeadCheckList)

            for x in range(len(self.HeadCheckList)):
                if x == 0:
                    print('対子リスト:' , self.HeadCheckList)

                SelectTmp = copy.deepcopy(Arrangement)
                SelectTmp = sorted(SelectTmp, key = self.Name.index)
                
                # HeadCheckList[x] の中の二つの要素 [0], [1] を除く
                SelectTmp.remove(self.HeadCheckList[x][0])
                SelectTmp.remove(self.HeadCheckList[x][1])
                
                print(' ')
                print('雀頭候補 ', self.HeadCheckList[x])

                # くっつき牌の考慮
                HeadDic[tuple(self.HeadCheckList[x])] = 0
                if self.HeadCheckList[x] in [['2m', '2m'], ['3m', '3m'], ['4m', '4m'], ['5m', '5m'], ['6m', '6m'], ['7m', '7m'], ['8m', '8m'],
                            ['2p', '2p'], ['3p', '3p'], ['4p', '4p'], ['5p', '5p'], ['6p', '6p'], ['7p', '7p'], ['8p', '8p'],
                            ['2s', '2s'], ['3s', '3s'], ['4s', '4s'], ['5s', '5s'], ['6s', '6s'], ['7s', '7s'], ['8s', '8s']
                            ]:
                    for k in range(len(SelectTmp)):
                        case = O.Pair_Rev([self.HeadCheckList[x]], SelectTmp[k])
                        # くっつき有る時 1 を加算
                        HeadDic[tuple(self.HeadCheckList[x])] += case

                # FourFlg を考慮する意味がまだ整理できていが、、、ヘッドを選ぶ段階では、暗刻くっつきだと強ターツを取り損ねるので不要、多分。
                Select, MemberCheck, TartsCheck = O.FirstSelection(SelectTmp, False)
                print('面子数： ', MemberCheck)
                # Select, MemberCheck, TartsCheck = O.FirstSelection(SelectTmp, True)

                # ターツを考慮する(TC: TartsCheck)
                TC = 0
                SelectTmp = copy.deepcopy(Select)
                TC = O.SecondSelection(SelectTmp, len(self.HeadCheckList)) + TartsCheck

                # タンヤオ判定： もう少し練り直しがいる・・・多分、一番最初で行った方がいい。
                # HeadDicTanyao[tuple(self.HeadCheckList[x])] = 0
                # if self.HeadCheckList[x] in [['E', 'E'], ['S', 'S'], ['We', 'We'], ['N', 'N'], ['Wh', 'Wh'], ['G', 'G'], ['R', 'R'],
                #                              ['1m', '1m'], ['9m', '9m'], ['1p', '1p'], ['9p', '9p'], ['1s', '1s'], ['9s', '9s'],] and MemberCheck >= 1:
                #     # 19字牌ヘッドで、1 に。
                #     HeadDicTanyao[tuple(self.HeadCheckList[x])] = 1
                #     for k in range(len(SelectTmp)):
                #         if SelectTmp[k] not in ['3m', '4m', '5m', '6m', '7m', '3p', '4p', '5p', '6p', '7p', '3s', '4s', '5s', '6s', '7s']:
                #             # タンヤオ行くべきでない時は、2 に。つまり、1 ならタンヤオ選択（ヘッドとして優先して選ばない）
                #             HeadDicTanyao[tuple(self.HeadCheckList[x])] = 2
                #             break

                if MaxMember < MemberCheck:
                    print('★雀頭更新--面子多い ', self.HeadCheckList[x])
                    MaxMember = MemberCheck
                    Head_Index = x                    
                    TrueSelect = copy.deepcopy(Select)
                    TrueTC = copy.deepcopy(TC)
                    # くっつき有る時 TrueNext は 1 
                    TrueNext = HeadDic[tuple(self.HeadCheckList[x])]
                    # TrueTanyao = HeadDicTanyao[tuple(self.HeadCheckList[x])]
                    continue

                # 面子数が同じ時のヘッド選択： くっつき牌を考慮。くっつきが少ない方を優先してヘッドにする。
                # くっつき有る時 1 
                if MaxMember == MemberCheck and MaxMember != 0 and TrueNext >= 1:
                    if HeadDic[tuple(self.HeadCheckList[x])] < TrueNext:
                        print('★雀頭更新--くっつき牌少ない ', self.HeadCheckList[x])
                        MaxMember = MemberCheck
                        Head_Index = x                    
                        TrueSelect = copy.deepcopy(Select)
                        TrueTC = copy.deepcopy(TC)
                        TrueNext = HeadDic[tuple(self.HeadCheckList[x])]
                        continue
                
                # タンヤオ分岐 一度更新したヘッドが、19字牌（TrueTanyao==1) でかつ、今回のヘッドが19字牌で無い (0) 場合
                # if MaxMember == MemberCheck and MaxMember != 0 and TrueTanyao == 1 and HeadDicTanyao[tuple(self.HeadCheckList[x])] == 0:
                #     print('★雀頭更新--タンヤオ狙い ', self.HeadCheckList[x])
                #     MaxMember = MemberCheck
                #     Head_Index = x                    
                #     TrueSelect = copy.deepcopy(Select)
                #     TrueTC = copy.deepcopy(TC)
                #     continue

                # 一度だけ、雀頭候補を追加する。シャボの最終系を考慮。
                # if MaxMember == MemberCheck and Head_Index_Another == None and MemberCheck != 0:
                #     CandidateCheck = 0
                #     print('雀頭他候補 ', self.HeadCheckList[x])
                #     print(' ')
                #     if len(TrueSelect) > 1:
                #         if self.HeadCheckList[x][0] in TrueSelect:
                #             TrueSelect.remove(self.HeadCheckList[x][0])
                #             CandidateCheck = 1
                #         if self.HeadCheckList[x][1] in TrueSelect:
                #             TrueSelect.remove(self.HeadCheckList[x][1])
                #             Head_Index_Another = x
                #             CandidateCheck = 0
                #         if CandidateCheck == 1:
                #             TrueSelect.append(self.HeadCheckList[x][0])
            
            print(' ')
            print('面子数（雀頭考慮）: ', MaxMember)

        # ヘッドを最初に考慮しない場合
        print(' ')
        print('２－雀頭未考慮')
        SelectTmp = copy.deepcopy(Arrangement)
        SelectTmp = sorted(SelectTmp, key = self.Name.index)

        # ヘッドを考慮しない場合は、ノベタンや暗刻くっつきで聴牌を取るケースがあるので、Trueに。
        Select, self.Member, _ = O.FirstSelection(SelectTmp, True)
        print(' ')
        print('面子数（雀頭未考慮）: ', self.Member)

        # ヘッドを決定する。
        if len(self.HeadCheckList) != 0:
            if (self.Member <= MaxMember and TrueSelect != None) or (self.Member == 4 and MaxMember == 3 and TrueTC == 1):
                # 上列後半は、対子 in 4面子かつ、残り2枚が強塔子のケース
                FinalMember = MaxMember
                Select = copy.deepcopy(TrueSelect)
                print(' ')
                print('⇒ ★１－雀頭は固定： ', self.HeadCheckList[Head_Index])
                if Head_Index_Another != None:
                    print('雀頭追加（シャボ想定）： ', self.HeadCheckList[Head_Index], self.HeadCheckList[Head_Index_Another])

            if  self.Member == 0 or (self.Member > MaxMember and (self.Member != 4 or MaxMember != 3 or TrueTC != 1)):
                print(' ')
                print('⇒ ★２－雀頭は固定しない')
                FinalMember = self.Member
            
            # 降りるかどうかの判断(1) 今の所、一度降りたらずっと降りっぱなしにしておく
            # [0]:手作りを進める, [1]: 降りる'
            if MaxMember >= 2 and TrueTC == 1 and len(Escape) <= 1 and Escape == [] :
                Escape = []
                Escape.append(0)
                print(' ')
                print('Escape2: ', Escape)

        if len(self.HeadCheckList) == 0:
            print(' ')
            print('⇒ ★まだ雀頭なし')
            

        print(' ')
        print('面子数(決定)： ', FinalMember)
        print('面子以外の牌: ', Select)

        O.SecondSelection(Select, len(self.HeadCheckList))

        # 降りるかどうかの判断(2) 今の所、一度降りたらずっと降りっぱなしにしておく
        # [0]:相手が攻めて来ても押す, [1]: 降りる'
        if len(self.HeadCheckList) == 0 and len(Escape) <= 1 and Escape == []:
            if self.Member >= 3:
                Escape = []
                Escape.append(0)
                print(' ')
                print('Escape3: ', Escape)

        Priority = ['N',  'We', 'S',  'E',  'Wh', 'G',  'R', '1m', '1p', '1s', '9m', '9p', '9s', 
                    '2m', '2p', '2s', '8m', '8p', '8s', '3m', '3p', '3s', '7m', '7p', '7s', '4m', '4p', '4s', 
                    '6m', '6p', '6s', '5m', '5p', '5s',                  
                    '5mr', '5pr', '5sr']
        Results = []
        print(' ')
        print('捨てる候補: ', Select)

        # 降りる牌の選択
        if Escape == [1] or Escape == [1, 1] or Escape == [1, 1, 1]:
            print(' ')
            print('★降りる★')
            Results = O.EscapeExe(Arrangement, Select, Dora, ReachBox, CareBox)

        # 相手が攻めてこない、あるいは押していく時の捨て牌選択。ドラを考慮。
        if Escape != [1] and Escape != [1, 1] and Escape != [1, 1, 1]:
            for i in range(len(Priority)):
                if Priority[i] in Select:
                    if Dora != []:
                        if Priority[i] != Dora[0]:
                            Results.append(Priority[i])
                        if Priority[i] == Dora[0] and len(Select) == 1:
                            Results.append(Priority[i])
                        if Priority[i] == Dora[0] and len(Select) >= 2:
                            continue
                    if Dora == []:
                        Results.append(Priority[i])
            
            # ['3m', '3m', '4m'] などの完全イーシャンテンパーツを聴牌まで残すための措置。
            print('捨てる候補(ソート): ', Results)

            #  くっつき対子があるタンヤオ牌は優先して残す。
            ResultsTmp = copy.deepcopy(Results)
            for k in range(len(Results)):
                if Results[k] in ['2m', '3m', '4m', '5m', '6m', '7m', '8m', 
                                  '2p', '3p', '4p', '5p', '6p', '7p', '8p',
                                  '2s', '3s', '4s', '5s', '6s', '7s', '8s'] and self.TiToi != 1 and len(Results) >= 2:
                    case = O.Pair(self.HeadCheckList, Results[k])
                    if case == 1 and len(ResultsTmp) >=2:
                        ResultsTmp.remove(Results[k])
            Results = ResultsTmp
        
        # 七対子では、暗刻の残り一つを打牌優先する。カンチャンとかで拾われてしまい、捨てリストに残らない事があるので。
        if self.TiToi == 1:
            TitBox = []
            TitBox2 = []
            for i in range(len(self.HeadCheckList)):
                TitBox.append(self.HeadCheckList[i][0])
            for j in range(len(Results)):
                if Results[j] in TitBox:
                    TitBox2.append(Results[j])
                    Results = TitBox2
                    break
            print('七対子')
            print(' ') 

        print('選択結果: ', Results[0])
        print(' ')

        # 赤牌対策
        RedSign = 0
        Select = copy.deepcopy(Arrangement)
        if Select.count(Results[0]) >= 2 and Results[0] in ['5m', '5p', '5s']:
            RedSign = 1

        return Results, RedSign, Escape
    
    # 降りる牌を選択する関数
    def EscapeExe(self, Arrangement, Select, Dora, ReachBox, CareBox):
        Results = []
        Priority = ['N',  'We', 'S',  'E',  'Wh', 'G',  'R', '1m', '1p', '1s', '9m', '9p', '9s', 
            '2m', '2p', '2s', '8m', '8p', '8s', '3m', '3p', '3s', '7m', '7p', '7s', '4m', '4p', '4s', 
            '6m', '6p', '6s', '5m', '5p', '5s',                  
            '5mr', '5pr', '5sr']
        # リーチへの対応が優先
        if ReachBox != []:
            for i in range(len(Arrangement)):
                if Arrangement[i] in ReachBox:
                    Results.append(Arrangement[i])
            print('リーチが入っての降り牌：', Results)

        if ReachBox == [] and CareBox != []:
            for i in range(len(Arrangement)):
                if Arrangement[i] in CareBox:
                    Results.append(Arrangement[i])
            print('鳴きが入っての降り牌：', Results)
                        
        # 降りる牌が無い時。Arrangement から Priority に沿って Results に格納していく。
        if Results == []:
            for i in range(len(Priority)):
                if Priority[i] in Arrangement:
                    if Dora != [] and Priority[i] != Dora[0]:
                        Results.append(Priority[i])
                    if Dora == []:
                        Results.append(Priority[i])
            print('降り牌が無い場合の捨て牌候補：', Results)

        return Results

    def Pair(self, HeadCheckList, Candidate):
        case = 0
        Pair = {'2m': [['3m', '3m']], '3m': [['2m', '2m'], ['4m', '4m']], '4m': [['3m', '3m'], ['5m', '5m']], '5m': [['4m', '4m'], ['6m', '6m']],
                '6m': [['5m', '5m'], ['7m', '7m']], '7m': [['8m', '8m'], ['6m', '6m']], '8m': [['7m', '7m']],
                '2p': [['3p', '3p']], '3p': [['2p', '2p'], ['4p', '4p']], '4p': [['3p', '3p'], ['5p', '5p']], '5p': [['4p', '4p'], ['6p', '6p']],
                '6p': [['5p', '5p'], ['7p', '7p']], '7p': [['8p', '8p'], ['6p', '6p']], '8p': [['7p', '7p']],
                '2s': [['3s', '3s']], '3s': [['2s', '2s'], ['4s', '4s']], '4s': [['3s', '3s'], ['5s', '5s']], '5s': [['4s', '4s'], ['6s', '6s']],
                '6s': [['5s', '5s'], ['7s', '7s']], '7s': [['8s', '8s'], ['6s', '6s']], '8s': [['7s', '7s']],
                }
        for i in range(len(HeadCheckList)):
            if HeadCheckList[i] in Pair[Candidate]:
                print('捨てる候補のくっつき対子', HeadCheckList[i], '-', Candidate)
                case = 1
        return case
    
    def Pair_Rev(self, HeadCheckList, Candidate):
        case = 0
        Pair = {('2m', '2m'): ['3m', '4m'], ('3m', '3m'): ['2m', '4m', '5m'], ('4m', '4m'): ['2m', '3m', '5m', '6m'], ('5m', '5m'): ['3m', '4m', '6m', '7m'], 
                ('6m', '6m'): ['4m', '5m', '7m', '8m'], ('7m', '7m'): ['5m', '6m', '8m'], ('8m', '8m'): ['6m', '7m'],
                ('2p', '2p'): ['3p', '4p'], ('3p', '3p'): ['2p', '4p', '5p'], ('4p', '4p'): ['2p', '3p', '5p', '6p'], ('5p', '5p'): ['3p', '4p', '6p', '7p'], 
                ('6p', '6p'): ['4p', '5p', '7p', '8p'], ('7p', '7p'): ['5p', '6p', '8p'], ('8p', '8p'): ['6p', '7p'],
                ('2s', '2s'): ['3s', '4s'], ('3s', '3s'): ['2s', '4s', '5s'], ('4s', '4s'): ['2s', '3s', '5s', '6s'], ('5s', '5s'): ['3s', '4s', '6s', '7s'], 
                ('6s', '6s'): ['4s', '5s', '7s', '8s'], ('7s', '7s'): ['5s', '6s', '8s'], ('8s', '8s'): ['6s', '7s'],
                }
        for i in range(len(HeadCheckList)):
            # タプル：要素を変更できない（＝順番が決まっている）
            if Candidate in Pair[tuple(HeadCheckList[i])]:
                print('ヘッド選択のくっつきチェック', HeadCheckList[i], Candidate)
                case = 1
        return case

O = O_Execusion()