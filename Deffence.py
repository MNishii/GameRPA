import pyautogui as pg
import time
import datetime
import pyperclip
import schedule
import itertools as it
import copy
import random

from Offence import *

# スクリーンショットを取って保存する。
def ScreenShot():
    now = datetime.datetime.now()
    time = now.strftime('%Y%m%d-%H%M%S')
    screen_shot = pg.screenshot() 
    screen_shot.save('screen_shot_web/output_{}.png'.format(time))

# ここは自分の手牌と違う。Top も考慮
# BOX の Left 値および Top 値の差分を取る。
def isMatch_D(box1, box2):
    a, b, c, d = box1
    e, f, g, h = box2
    return abs(e - a), abs(f - b)

# locateAllOnScreen 機能での重複を排除
def BoxValue_D(boxlist):
    if len(boxlist) == 1:
        return boxlist
    elif len(boxlist) >= 2:
        for i, j in list(it.combinations(boxlist, 2)):
            # print('Candidates: ', i, j)
            Match_1, Match_2 = isMatch_D(i, j)
            # ここも自分の手牌と違い、Top も考慮
            if Match_1 <= 10 and Match_2 <= 10 and j in boxlist:
                boxlist.remove(j)
        return boxlist

# リスト成分の差分を求める
def list_difference(list1, list2):
    result = copy.deepcopy(list1)
    for value in list2:
        if value in result:
            result.remove(value)
    return result

class D_Execusion():
    def __init__(self):
        self.UpdateRight = []
        self.UpdateCenter = []
        self.UpdateLeft = []
        self.RightList = []
        self.CenterList = []
        self.LeftList = []
        self.ReachBox = []
        self.CareBox = []
        self.MyArrangement = []
        self.ReachState = []
        self.Member = 0
        self.Hou = []
        self.s_r = None
        self.s_c = None
        self.s_l = None 
        self.r_attack = []
        self.c_attack = []
        self.l_attack = []
        self.Alert = []
        self.Dora = []
        self.Turn = []
        self.r_ReachPiece = []
        self.c_ReachPiece = []
        self.l_ReachPiece = []
        self.Escape = []

        self.Name = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                     '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                     '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                     'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #            '5mr', '5pr', '5sr']
        self.Name2 = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                      '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',
                      '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                      'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #             '5mr', '5pr', '5sr']
        self.Name3 = ['1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                      '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                      '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                      'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #             '5mr', '5pr', '5sr']
        self.Name4 = ['1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                      '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                      '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                      'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #             '5mr', '5pr', '5sr']
        self.Name5 = ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                      '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',
                      '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', 
                      'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #             '5mr', '5pr', '5sr']
        self.Name6 = ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                      '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                      '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',
                      'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
        #             '5mr', '5pr', '5sr']

    def r_ReachPieceCheck(self):
        r_ReachPiece = []
        # 対面の捨て牌を利用（向きが同じなため）
        # 範囲は下家↓
        prtsc_range = (688, 359, 256, 306)
        q101 = list(pg.locateAllOnScreen("./img_web/c_1m.png", region=prtsc_range, confidence=0.9))
        q102 = list(pg.locateAllOnScreen("./img_web/c_2m.png", region=prtsc_range, confidence=0.9))
        q103 = list(pg.locateAllOnScreen("./img_web/c_3m.png", region=prtsc_range, confidence=0.9))
        q104 = list(pg.locateAllOnScreen("./img_web/c_4m.png", region=prtsc_range, confidence=0.9))
        q105a = list(pg.locateAllOnScreen("./img_web/c_5m.png", region=prtsc_range, confidence=0.9))
        q105b = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.9))
        q105 = q105a + q105b
        q106 = list(pg.locateAllOnScreen("./img_web/c_6m.png", region=prtsc_range, confidence=0.9))
        q107 = list(pg.locateAllOnScreen("./img_web/c_7m.png", region=prtsc_range, confidence=0.9))
        q108 = list(pg.locateAllOnScreen("./img_web/c_8m.png", region=prtsc_range, confidence=0.9))
        q109 = list(pg.locateAllOnScreen("./img_web/c_9m.png", region=prtsc_range, confidence=0.9))
        q110 = list(pg.locateAllOnScreen("./img_web/c_1p.png", region=prtsc_range, confidence=0.9))
        q111 = list(pg.locateAllOnScreen("./img_web/c_2p.png", region=prtsc_range, confidence=0.9))
        q112 = list(pg.locateAllOnScreen("./img_web/c_3p.png", region=prtsc_range, confidence=0.9))
        q113 = list(pg.locateAllOnScreen("./img_web/c_4p.png", region=prtsc_range, confidence=0.9))
        q114a = list(pg.locateAllOnScreen("./img_web/c_5p.png", region=prtsc_range, confidence=0.9))
        q114b = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.9))
        q114 = q114a + q114b
        q115 = list(pg.locateAllOnScreen("./img_web/c_6p.png", region=prtsc_range, confidence=0.9))
        q116 = list(pg.locateAllOnScreen("./img_web/c_7p.png", region=prtsc_range, confidence=0.9))
        q117 = list(pg.locateAllOnScreen("./img_web/c_8p.png", region=prtsc_range, confidence=0.9))
        q118 = list(pg.locateAllOnScreen("./img_web/c_9p.png", region=prtsc_range, confidence=0.9))
        q119 = list(pg.locateAllOnScreen("./img_web/c_1s.png", region=prtsc_range, confidence=0.9))
        q120 = list(pg.locateAllOnScreen("./img_web/c_2s.png", region=prtsc_range, confidence=0.9))
        q121 = list(pg.locateAllOnScreen("./img_web/c_3s.png", region=prtsc_range, confidence=0.9))
        q122 = list(pg.locateAllOnScreen("./img_web/c_4s.png", region=prtsc_range, confidence=0.9))
        q123a = list(pg.locateAllOnScreen("./img_web/c_5s.png", region=prtsc_range, confidence=0.9))
        q123b = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.9))
        q123 = q123a + q123b
        q124 = list(pg.locateAllOnScreen("./img_web/c_6s.png", region=prtsc_range, confidence=0.9))
        q125 = list(pg.locateAllOnScreen("./img_web/c_7s.png", region=prtsc_range, confidence=0.9))
        q126 = list(pg.locateAllOnScreen("./img_web/c_8s.png", region=prtsc_range, confidence=0.9))
        q127 = list(pg.locateAllOnScreen("./img_web/c_9s.png", region=prtsc_range, confidence=0.9))
        q128 = list(pg.locateAllOnScreen("./img_web/c_E.png", region=prtsc_range, confidence=0.9))
        q129 = list(pg.locateAllOnScreen("./img_web/c_S.png", region=prtsc_range, confidence=0.9))
        q130 = list(pg.locateAllOnScreen("./img_web/c_We.png", region=prtsc_range, confidence=0.9))
        q131 = list(pg.locateAllOnScreen("./img_web/c_N.png", region=prtsc_range, confidence=0.9))
        q132 = list(pg.locateAllOnScreen("./img_web/c_Wh.png", region=prtsc_range, confidence=0.9))
        q133 = list(pg.locateAllOnScreen("./img_web/c_G.png", region=prtsc_range, confidence=0.9))
        q134 = list(pg.locateAllOnScreen("./img_web/c_R.png", region=prtsc_range, confidence=0.9))
        # q135 = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.90))
        # q136 = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.90))
        # q137 = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.95))
        MySet = [q101,  q102,  q103,  q104,  q105,  q106,  q107,  q108,  q109, 
            q110, q111, q112, q113, q114, q115, q116, q117, q118, 
            q119, q120, q121, q122, q123, q124, q125, q126, q127, 
            q128, q129, q130, q131, q132, q133, q134]
        for i in range(34):
            if BoxValue_D(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    r_ReachPiece.append(self.Name[i])
        
        return r_ReachPiece

    def c_ReachPieceCheck(self):
        c_ReachPiece = []
        # 上家の捨て牌を利用（向きが同じなため）
        # 範囲は対面↓
        prtsc_range = (388, 175, 340, 222)
        q201 = list(pg.locateAllOnScreen("./img_web/l_1m.png", region=prtsc_range, confidence=0.9))
        q202 = list(pg.locateAllOnScreen("./img_web/l_2m.png", region=prtsc_range, confidence=0.9))
        q203 = list(pg.locateAllOnScreen("./img_web/l_3m.png", region=prtsc_range, confidence=0.9))
        q204 = list(pg.locateAllOnScreen("./img_web/l_4m.png", region=prtsc_range, confidence=0.9))
        q205a = list(pg.locateAllOnScreen("./img_web/l_5m.png", region=prtsc_range, confidence=0.9))
        q205b = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.9))
        q205 = q205a + q205b
        q206 = list(pg.locateAllOnScreen("./img_web/l_6m.png", region=prtsc_range, confidence=0.9))
        q207 = list(pg.locateAllOnScreen("./img_web/l_7m.png", region=prtsc_range, confidence=0.9))
        q208 = list(pg.locateAllOnScreen("./img_web/l_8m.png", region=prtsc_range, confidence=0.9))
        q209 = list(pg.locateAllOnScreen("./img_web/l_9m.png", region=prtsc_range, confidence=0.9))
        q210 = list(pg.locateAllOnScreen("./img_web/l_1p.png", region=prtsc_range, confidence=0.9))
        q211 = list(pg.locateAllOnScreen("./img_web/l_2p.png", region=prtsc_range, confidence=0.9))
        q212 = list(pg.locateAllOnScreen("./img_web/l_3p.png", region=prtsc_range, confidence=0.9))
        q213 = list(pg.locateAllOnScreen("./img_web/l_4p.png", region=prtsc_range, confidence=0.9))
        q214a = list(pg.locateAllOnScreen("./img_web/l_5p.png", region=prtsc_range, confidence=0.9))
        q214b = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.9))
        q214 = q214a + q214b
        q215 = list(pg.locateAllOnScreen("./img_web/l_6p.png", region=prtsc_range, confidence=0.9))
        q216 = list(pg.locateAllOnScreen("./img_web/l_7p.png", region=prtsc_range, confidence=0.9))
        q217 = list(pg.locateAllOnScreen("./img_web/l_8p.png", region=prtsc_range, confidence=0.9))
        q218 = list(pg.locateAllOnScreen("./img_web/l_9p.png", region=prtsc_range, confidence=0.9))
        q219 = list(pg.locateAllOnScreen("./img_web/l_1s.png", region=prtsc_range, confidence=0.9))
        q220 = list(pg.locateAllOnScreen("./img_web/l_2s.png", region=prtsc_range, confidence=0.9))
        q221 = list(pg.locateAllOnScreen("./img_web/l_3s.png", region=prtsc_range, confidence=0.9))
        q222 = list(pg.locateAllOnScreen("./img_web/l_4s.png", region=prtsc_range, confidence=0.9))
        q223a = list(pg.locateAllOnScreen("./img_web/l_5s.png", region=prtsc_range, confidence=0.9))
        q223b = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.9))
        q223 = q223a + q223b
        q224 = list(pg.locateAllOnScreen("./img_web/l_6s.png", region=prtsc_range, confidence=0.9))
        q225 = list(pg.locateAllOnScreen("./img_web/l_7s.png", region=prtsc_range, confidence=0.9))
        q226 = list(pg.locateAllOnScreen("./img_web/l_8s.png", region=prtsc_range, confidence=0.9))
        q227 = list(pg.locateAllOnScreen("./img_web/l_9s.png", region=prtsc_range, confidence=0.9))
        q228 = list(pg.locateAllOnScreen("./img_web/l_E.png", region=prtsc_range, confidence=0.9))
        q229 = list(pg.locateAllOnScreen("./img_web/l_S.png", region=prtsc_range, confidence=0.9))
        q230 = list(pg.locateAllOnScreen("./img_web/l_We.png", region=prtsc_range, confidence=0.9))
        q231 = list(pg.locateAllOnScreen("./img_web/l_N.png", region=prtsc_range, confidence=0.9))
        q232 = list(pg.locateAllOnScreen("./img_web/l_Wh.png", region=prtsc_range, confidence=0.9))
        q233 = list(pg.locateAllOnScreen("./img_web/l_G.png", region=prtsc_range, confidence=0.9))
        q234 = list(pg.locateAllOnScreen("./img_web/l_R.png", region=prtsc_range, confidence=0.9))
        # q235 = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.90))
        # q236 = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.90))
        # q237 = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.95))
        MySet = [q201,  q202,  q203,  q204,  q205,  q206,  q207,  q208,  q209, 
            q210, q211, q212, q213, q214, q215, q216, q217, q218, 
            q219, q220, q221, q222, q223, q224, q225, q226, q227, 
            q228, q229, q230, q231, q232, q233, q234]
        for i in range(34):
            if BoxValue_D(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    c_ReachPiece.append(self.Name[i])
        return c_ReachPiece

    def l_ReachPieceCheck(self):
        l_ReachPiece = []
        # 自分の捨て牌を利用（向きが同じなため）
        # 範囲は上家↓
        prtsc_range = (186, 357, 264, 282)
        q301 = list(pg.locateAllOnScreen("./img_web/f_1m.png", region=prtsc_range, confidence=0.9))
        q302 = list(pg.locateAllOnScreen("./img_web/f_2m.png", region=prtsc_range, confidence=0.9))
        q303 = list(pg.locateAllOnScreen("./img_web/f_3m.png", region=prtsc_range, confidence=0.9))
        q304 = list(pg.locateAllOnScreen("./img_web/f_4m.png", region=prtsc_range, confidence=0.9))
        q305a = list(pg.locateAllOnScreen("./img_web/f_5m.png", region=prtsc_range, confidence=0.9))
        q305b = list(pg.locateAllOnScreen("./img_web/f_5mr.png", region=prtsc_range, confidence=0.9))
        q305 = q305a + q305b
        q306 = list(pg.locateAllOnScreen("./img_web/f_6m.png", region=prtsc_range, confidence=0.9))
        q307 = list(pg.locateAllOnScreen("./img_web/f_7m.png", region=prtsc_range, confidence=0.9))
        q308 = list(pg.locateAllOnScreen("./img_web/f_8m.png", region=prtsc_range, confidence=0.9))
        q309 = list(pg.locateAllOnScreen("./img_web/f_9m.png", region=prtsc_range, confidence=0.9))
        q310 = list(pg.locateAllOnScreen("./img_web/f_1p.png", region=prtsc_range, confidence=0.9))
        q311 = list(pg.locateAllOnScreen("./img_web/f_2p.png", region=prtsc_range, confidence=0.9))
        q312 = list(pg.locateAllOnScreen("./img_web/f_3p.png", region=prtsc_range, confidence=0.9))
        q313 = list(pg.locateAllOnScreen("./img_web/f_4p.png", region=prtsc_range, confidence=0.9))
        q314a = list(pg.locateAllOnScreen("./img_web/f_5p.png", region=prtsc_range, confidence=0.9))
        q314b = list(pg.locateAllOnScreen("./img_web/f_5pr.png", region=prtsc_range, confidence=0.9))
        q314 = q314a + q314b
        q315 = list(pg.locateAllOnScreen("./img_web/f_6p.png", region=prtsc_range, confidence=0.9))
        q316 = list(pg.locateAllOnScreen("./img_web/f_7p.png", region=prtsc_range, confidence=0.9))
        q317 = list(pg.locateAllOnScreen("./img_web/f_8p.png", region=prtsc_range, confidence=0.9))
        q318 = list(pg.locateAllOnScreen("./img_web/f_9p.png", region=prtsc_range, confidence=0.9))
        q319 = list(pg.locateAllOnScreen("./img_web/f_1s.png", region=prtsc_range, confidence=0.9))
        q320 = list(pg.locateAllOnScreen("./img_web/f_2s.png", region=prtsc_range, confidence=0.9))
        q321 = list(pg.locateAllOnScreen("./img_web/f_3s.png", region=prtsc_range, confidence=0.9))
        q322 = list(pg.locateAllOnScreen("./img_web/f_4s.png", region=prtsc_range, confidence=0.9))
        q323a = list(pg.locateAllOnScreen("./img_web/f_5s.png", region=prtsc_range, confidence=0.9))
        q323b = list(pg.locateAllOnScreen("./img_web/f_5sr.png", region=prtsc_range, confidence=0.9))
        q323 = q323a + q323b
        q324 = list(pg.locateAllOnScreen("./img_web/f_6s.png", region=prtsc_range, confidence=0.9))
        q325 = list(pg.locateAllOnScreen("./img_web/f_7s.png", region=prtsc_range, confidence=0.9))
        q326 = list(pg.locateAllOnScreen("./img_web/f_8s.png", region=prtsc_range, confidence=0.9))
        q327 = list(pg.locateAllOnScreen("./img_web/f_9s.png", region=prtsc_range, confidence=0.9))
        q328 = list(pg.locateAllOnScreen("./img_web/f_E.png", region=prtsc_range, confidence=0.9))
        q329 = list(pg.locateAllOnScreen("./img_web/f_S.png", region=prtsc_range, confidence=0.9))
        q330 = list(pg.locateAllOnScreen("./img_web/f_We.png", region=prtsc_range, confidence=0.9))
        q331 = list(pg.locateAllOnScreen("./img_web/f_N.png", region=prtsc_range, confidence=0.9))
        q332 = list(pg.locateAllOnScreen("./img_web/f_Wh.png", region=prtsc_range, confidence=0.9))
        q333 = list(pg.locateAllOnScreen("./img_web/f_G.png", region=prtsc_range, confidence=0.9))
        q334 = list(pg.locateAllOnScreen("./img_web/f_R.png", region=prtsc_range, confidence=0.9))
        # q335 = list(pg.locateAllOnScreen("./img_web/f_5mr.png", region=prtsc_range, confidence=0.90))
        # q336 = list(pg.locateAllOnScreen("./img_web/f_5pr.png", region=prtsc_range, confidence=0.90))
        # q337 = list(pg.locateAllOnScreen("./img_web/f_5sr.png", region=prtsc_range, confidence=0.95))
        MySet = [q301,  q302,  q303,  q304,  q305,  q306,  q307,  q308,  q309, 
            q310, q311, q312, q313, q314, q315, q316, q317, q318, 
            q319, q320, q321, q322, q323, q324, q325, q326, q327, 
            q328, q329, q330, q331, q332, q333, q334]
        for i in range(34):
            if BoxValue_D(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    l_ReachPiece.append(self.Name[i])
        return l_ReachPiece
        
    def DoraCheck(self, Dora, Turn):
        t1=time.time()
        self.Name = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
            'E',  'S',  'We', 'N',  'Wh', 'G',  'R', 
            '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
            'E',  'S',  'We', 'N',  'Wh', 'G',  'R', 
            '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
            'E',  'S',  'We', 'N',  'Wh', 'G',  'R',
            '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
            '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
            '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
            'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
            
        # 下家前の山のドラサーチ
        prtsc_range = (900, 133, 90, 668)
        q0 = pg.locateOnScreen("./img_web/r_DoraYama.png", region=prtsc_range, confidence=0.7)
        # print(q0)
        if q0 != None:
            # print('path1')
            q1 = list(pg.locateAllOnScreen("./img_web/r_1m.png", region=prtsc_range, confidence=0.9))
            q2 = list(pg.locateAllOnScreen("./img_web/r_2m.png", region=prtsc_range, confidence=0.9))
            q3 = list(pg.locateAllOnScreen("./img_web/r_3m.png", region=prtsc_range, confidence=0.9))
            q4 = list(pg.locateAllOnScreen("./img_web/r_4m.png", region=prtsc_range, confidence=0.9))
            q5a = list(pg.locateAllOnScreen("./img_web/r_5m.png", region=prtsc_range, confidence=0.9))
            q5b = list(pg.locateAllOnScreen("./img_web/r_5mr.png", region=prtsc_range, confidence=0.9))
            q5 = q5a + q5b
            q6 = list(pg.locateAllOnScreen("./img_web/r_6m.png", region=prtsc_range, confidence=0.9))
            q7 = list(pg.locateAllOnScreen("./img_web/r_7m.png", region=prtsc_range, confidence=0.9))
            q8 = list(pg.locateAllOnScreen("./img_web/r_8m.png", region=prtsc_range, confidence=0.9))
            q9 = list(pg.locateAllOnScreen("./img_web/r_9m.png", region=prtsc_range, confidence=0.9))
            q10 = list(pg.locateAllOnScreen("./img_web/r_1p.png", region=prtsc_range, confidence=0.9))
            q11 = list(pg.locateAllOnScreen("./img_web/r_2p.png", region=prtsc_range, confidence=0.9))
            q12 = list(pg.locateAllOnScreen("./img_web/r_3p.png", region=prtsc_range, confidence=0.9))
            q13 = list(pg.locateAllOnScreen("./img_web/r_4p.png", region=prtsc_range, confidence=0.9))
            q14a = list(pg.locateAllOnScreen("./img_web/r_5p.png", region=prtsc_range, confidence=0.9))
            q14b = list(pg.locateAllOnScreen("./img_web/r_5pr.png", region=prtsc_range, confidence=0.9))
            q14 = q14a + q14b
            q15 = list(pg.locateAllOnScreen("./img_web/r_6p.png", region=prtsc_range, confidence=0.9))
            q16 = list(pg.locateAllOnScreen("./img_web/r_7p.png", region=prtsc_range, confidence=0.9))
            q17 = list(pg.locateAllOnScreen("./img_web/r_8p.png", region=prtsc_range, confidence=0.9))
            q18 = list(pg.locateAllOnScreen("./img_web/r_9p.png", region=prtsc_range, confidence=0.9))
            q19 = list(pg.locateAllOnScreen("./img_web/r_1s.png", region=prtsc_range, confidence=0.9))
            q20 = list(pg.locateAllOnScreen("./img_web/r_2s.png", region=prtsc_range, confidence=0.9))
            q21 = list(pg.locateAllOnScreen("./img_web/r_3s.png", region=prtsc_range, confidence=0.9))
            q22 = list(pg.locateAllOnScreen("./img_web/r_4s.png", region=prtsc_range, confidence=0.9))
            q23a = list(pg.locateAllOnScreen("./img_web/r_5s.png", region=prtsc_range, confidence=0.9))
            q23b = list(pg.locateAllOnScreen("./img_web/r_5sr.png", region=prtsc_range, confidence=0.9))
            q23 = q23a + q23b
            q24 = list(pg.locateAllOnScreen("./img_web/r_6s.png", region=prtsc_range, confidence=0.9))
            q25 = list(pg.locateAllOnScreen("./img_web/r_7s.png", region=prtsc_range, confidence=0.9))
            q26 = list(pg.locateAllOnScreen("./img_web/r_8s.png", region=prtsc_range, confidence=0.9))
            q27 = list(pg.locateAllOnScreen("./img_web/r_9s.png", region=prtsc_range, confidence=0.9))
            q28 = list(pg.locateAllOnScreen("./img_web/r_E.png", region=prtsc_range, confidence=0.9))
            q29 = list(pg.locateAllOnScreen("./img_web/r_S.png", region=prtsc_range, confidence=0.9))
            q30 = list(pg.locateAllOnScreen("./img_web/r_We.png", region=prtsc_range, confidence=0.9))
            q31 = list(pg.locateAllOnScreen("./img_web/r_N.png", region=prtsc_range, confidence=0.9))
            q32 = list(pg.locateAllOnScreen("./img_web/r_Wh.png", region=prtsc_range, confidence=0.9))
            q33 = list(pg.locateAllOnScreen("./img_web/r_G.png", region=prtsc_range, confidence=0.9))
            q34 = list(pg.locateAllOnScreen("./img_web/r_R.png", region=prtsc_range, confidence=0.9))
            # q35 = list(pg.locateAllOnScreen("./img_web/r_5mr.png", region=prtsc_range, confidence=0.90))
            # q36 = list(pg.locateAllOnScreen("./img_web/r_5pr.png", region=prtsc_range, confidence=0.90))
            # q37 = list(pg.locateAllOnScreen("./img_web/r_5sr.png", region=prtsc_range, confidence=0.95))
            MySet = [q1,  q2,  q3,  q4,  q5,  q6,  q7,  q8,  q9, 
                q10, q11, q12, q13, q14, q15, q16, q17, q18, 
                q19, q20, q21, q22, q23, q24, q25, q26, q27, 
                q28, q29, q30, q31, q32, q33, q34]
            for i in range(34):
                if BoxValue_D(MySet[i]) != None:
                    for _ in range(len(BoxValue_D(MySet[i]))):
                        if self.Name[i] not in ['9m', '9p', '9s', 'N', 'Wh', 'R']:
                            Dora.append(self.Name[i+1])
                        if self.Name[i] == '9m':
                            Dora.append('1m')
                        if self.Name[i] == '9p':
                            Dora.append('1p')
                        if self.Name[i] == '9s':
                            Dora.append('1s')
                        if self.Name[i] == 'N':
                            Dora.append('E')
                        if self.Name[i] == 'R':
                            Dora.append('Wh')
                        if self.Name[i] == 'Wh' and Dora == []:
                            Dora.append('G')

        # 対面前の山のドラサーチ
        if Dora == []:
            q100 = pg.locateOnScreen("./img_web/c_DoraYama.png", region=(128, 135, 798, 102), confidence=0.7)
            # print('path2')
            if q100 != None:
                prtsc_range = (128, 135, 798, 72)
                q101 = list(pg.locateAllOnScreen("./img_web/c_1m.png", region=prtsc_range, confidence=0.9))
                q102 = list(pg.locateAllOnScreen("./img_web/c_2m.png", region=prtsc_range, confidence=0.9))
                q103 = list(pg.locateAllOnScreen("./img_web/c_3m.png", region=prtsc_range, confidence=0.9))
                q104 = list(pg.locateAllOnScreen("./img_web/c_4m.png", region=prtsc_range, confidence=0.9))
                q105a = list(pg.locateAllOnScreen("./img_web/c_5m.png", region=prtsc_range, confidence=0.9))
                q105b = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.9))
                q105 = q105a + q105b
                q106 = list(pg.locateAllOnScreen("./img_web/c_6m.png", region=prtsc_range, confidence=0.9))
                q107 = list(pg.locateAllOnScreen("./img_web/c_7m.png", region=prtsc_range, confidence=0.9))
                q108 = list(pg.locateAllOnScreen("./img_web/c_8m.png", region=prtsc_range, confidence=0.9))
                q109 = list(pg.locateAllOnScreen("./img_web/c_9m.png", region=prtsc_range, confidence=0.9))
                q110 = list(pg.locateAllOnScreen("./img_web/c_1p.png", region=prtsc_range, confidence=0.9))
                q111 = list(pg.locateAllOnScreen("./img_web/c_2p.png", region=prtsc_range, confidence=0.9))
                q112 = list(pg.locateAllOnScreen("./img_web/c_3p.png", region=prtsc_range, confidence=0.9))
                q113 = list(pg.locateAllOnScreen("./img_web/c_4p.png", region=prtsc_range, confidence=0.9))
                q114a = list(pg.locateAllOnScreen("./img_web/c_5p.png", region=prtsc_range, confidence=0.9))
                q114b = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.9))
                q114 = q114a + q114b
                q115 = list(pg.locateAllOnScreen("./img_web/c_6p.png", region=prtsc_range, confidence=0.9))
                q116 = list(pg.locateAllOnScreen("./img_web/c_7p.png", region=prtsc_range, confidence=0.9))
                q117 = list(pg.locateAllOnScreen("./img_web/c_8p.png", region=prtsc_range, confidence=0.9))
                q118 = list(pg.locateAllOnScreen("./img_web/c_9p.png", region=prtsc_range, confidence=0.9))
                q119 = list(pg.locateAllOnScreen("./img_web/c_1s.png", region=prtsc_range, confidence=0.9))
                q120 = list(pg.locateAllOnScreen("./img_web/c_2s.png", region=prtsc_range, confidence=0.9))
                q121 = list(pg.locateAllOnScreen("./img_web/c_3s.png", region=prtsc_range, confidence=0.9))
                q122 = list(pg.locateAllOnScreen("./img_web/c_4s.png", region=prtsc_range, confidence=0.9))
                q123a = list(pg.locateAllOnScreen("./img_web/c_5s.png", region=prtsc_range, confidence=0.9))
                q123b = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.9))
                q123 = q123a + q123b
                q124 = list(pg.locateAllOnScreen("./img_web/c_6s.png", region=prtsc_range, confidence=0.9))
                q125 = list(pg.locateAllOnScreen("./img_web/c_7s.png", region=prtsc_range, confidence=0.9))
                q126 = list(pg.locateAllOnScreen("./img_web/c_8s.png", region=prtsc_range, confidence=0.9))
                q127 = list(pg.locateAllOnScreen("./img_web/c_9s.png", region=prtsc_range, confidence=0.9))
                q128 = list(pg.locateAllOnScreen("./img_web/c_E.png", region=prtsc_range, confidence=0.9))
                q129 = list(pg.locateAllOnScreen("./img_web/c_S.png", region=prtsc_range, confidence=0.9))
                q130 = list(pg.locateAllOnScreen("./img_web/c_We.png", region=prtsc_range, confidence=0.9))
                q131 = list(pg.locateAllOnScreen("./img_web/c_N.png", region=prtsc_range, confidence=0.9))
                q132 = list(pg.locateAllOnScreen("./img_web/c_Wh.png", region=prtsc_range, confidence=0.9))
                q133 = list(pg.locateAllOnScreen("./img_web/c_G.png", region=prtsc_range, confidence=0.9))
                q134 = list(pg.locateAllOnScreen("./img_web/c_R.png", region=prtsc_range, confidence=0.9))
                # q135 = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.90))
                # q136 = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.90))
                # q137 = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.95))
                MySet = [q101,  q102,  q103,  q104,  q105,  q106,  q107,  q108,  q109, 
                    q110, q111, q112, q113, q114, q115, q116, q117, q118, 
                    q119, q120, q121, q122, q123, q124, q125, q126, q127, 
                    q128, q129, q130, q131, q132, q133, q134]
                for i in range(34):
                    if BoxValue_D(MySet[i]) != None:
                        for _ in range(len(BoxValue_D(MySet[i]))):
                            if self.Name[i] not in ['9m', '9p', '9s', 'N', 'Wh', 'R']:
                                Dora.append(self.Name[i+1])
                            if self.Name[i] == '9m':
                                Dora.append('1m')
                            if self.Name[i] == '9p':
                                Dora.append('1p')
                            if self.Name[i] == '9s':
                                Dora.append('1s')
                            if self.Name[i] == 'N':
                                Dora.append('E')
                            if self.Name[i] == 'R':
                                Dora.append('Wh')
                            if self.Name[i] == 'Wh' and Dora == []:
                                Dora.append('G')

        # 上家前の山のドラサーチ
        if Dora == []:
            prtsc_range = (134, 177, 116, 688)
            q200 = pg.locateOnScreen("./img_web/l_DoraYama.png", region=prtsc_range, confidence=0.7)
            # print('path3')
            if q200 != None:
                q201 = list(pg.locateAllOnScreen("./img_web/l_1m.png", region=prtsc_range, confidence=0.9))
                q202 = list(pg.locateAllOnScreen("./img_web/l_2m.png", region=prtsc_range, confidence=0.9))
                q203 = list(pg.locateAllOnScreen("./img_web/l_3m.png", region=prtsc_range, confidence=0.9))
                q204 = list(pg.locateAllOnScreen("./img_web/l_4m.png", region=prtsc_range, confidence=0.9))
                q205a = list(pg.locateAllOnScreen("./img_web/l_5m.png", region=prtsc_range, confidence=0.9))
                q205b = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.9))
                q205 = q205a + q205b
                q206 = list(pg.locateAllOnScreen("./img_web/l_6m.png", region=prtsc_range, confidence=0.9))
                q207 = list(pg.locateAllOnScreen("./img_web/l_7m.png", region=prtsc_range, confidence=0.9))
                q208 = list(pg.locateAllOnScreen("./img_web/l_8m.png", region=prtsc_range, confidence=0.9))
                q209 = list(pg.locateAllOnScreen("./img_web/l_9m.png", region=prtsc_range, confidence=0.9))
                q210 = list(pg.locateAllOnScreen("./img_web/l_1p.png", region=prtsc_range, confidence=0.9))
                q211 = list(pg.locateAllOnScreen("./img_web/l_2p.png", region=prtsc_range, confidence=0.9))
                q212 = list(pg.locateAllOnScreen("./img_web/l_3p.png", region=prtsc_range, confidence=0.9))
                q213 = list(pg.locateAllOnScreen("./img_web/l_4p.png", region=prtsc_range, confidence=0.9))
                q214a = list(pg.locateAllOnScreen("./img_web/l_5p.png", region=prtsc_range, confidence=0.9))
                q214b = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.9))
                q214 = q214a + q214b
                q215 = list(pg.locateAllOnScreen("./img_web/l_6p.png", region=prtsc_range, confidence=0.9))
                q216 = list(pg.locateAllOnScreen("./img_web/l_7p.png", region=prtsc_range, confidence=0.9))
                q217 = list(pg.locateAllOnScreen("./img_web/l_8p.png", region=prtsc_range, confidence=0.9))
                q218 = list(pg.locateAllOnScreen("./img_web/l_9p.png", region=prtsc_range, confidence=0.9))
                q219 = list(pg.locateAllOnScreen("./img_web/l_1s.png", region=prtsc_range, confidence=0.9))
                q220 = list(pg.locateAllOnScreen("./img_web/l_2s.png", region=prtsc_range, confidence=0.9))
                q221 = list(pg.locateAllOnScreen("./img_web/l_3s.png", region=prtsc_range, confidence=0.9))
                q222 = list(pg.locateAllOnScreen("./img_web/l_4s.png", region=prtsc_range, confidence=0.9))
                q223a = list(pg.locateAllOnScreen("./img_web/l_5s.png", region=prtsc_range, confidence=0.9))
                q223b = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.9))
                q223 = q223a + q223b
                q224 = list(pg.locateAllOnScreen("./img_web/l_6s.png", region=prtsc_range, confidence=0.9))
                q225 = list(pg.locateAllOnScreen("./img_web/l_7s.png", region=prtsc_range, confidence=0.9))
                q226 = list(pg.locateAllOnScreen("./img_web/l_8s.png", region=prtsc_range, confidence=0.9))
                q227 = list(pg.locateAllOnScreen("./img_web/l_9s.png", region=prtsc_range, confidence=0.9))
                q228 = list(pg.locateAllOnScreen("./img_web/l_E.png", region=prtsc_range, confidence=0.9))
                q229 = list(pg.locateAllOnScreen("./img_web/l_S.png", region=prtsc_range, confidence=0.9))
                q230 = list(pg.locateAllOnScreen("./img_web/l_We.png", region=prtsc_range, confidence=0.9))
                q231 = list(pg.locateAllOnScreen("./img_web/l_N.png", region=prtsc_range, confidence=0.9))
                q232 = list(pg.locateAllOnScreen("./img_web/l_Wh.png", region=prtsc_range, confidence=0.9))
                q233 = list(pg.locateAllOnScreen("./img_web/l_G.png", region=prtsc_range, confidence=0.9))
                q234 = list(pg.locateAllOnScreen("./img_web/l_R.png", region=prtsc_range, confidence=0.9))
                # q235 = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.90))
                # q236 = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.90))
                # q237 = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.95))
                MySet = [q201,  q202,  q203,  q204,  q205,  q206,  q207,  q208,  q209, 
                    q210, q211, q212, q213, q214, q215, q216, q217, q218, 
                    q219, q220, q221, q222, q223, q224, q225, q226, q227, 
                    q228, q229, q230, q231, q232, q233, q234]
                for i in range(34):
                    if BoxValue_D(MySet[i]) != None:
                        for _ in range(len(BoxValue_D(MySet[i]))):
                            if self.Name[i] not in ['9m', '9p', '9s', 'N', 'Wh', 'R']:
                                Dora.append(self.Name[i+1])
                            if self.Name[i] == '9m':
                                Dora.append('1m')
                            if self.Name[i] == '9p':
                                Dora.append('1p')
                            if self.Name[i] == '9s':
                                Dora.append('1s')
                            if self.Name[i] == 'N':
                                Dora.append('E')
                            if self.Name[i] == 'R':
                                Dora.append('Wh')
                            if self.Name[i] == 'Wh' and Dora == []:
                                Dora.append('G')

        # 自分の山のドラサーチ
        if Dora == []:
            # print('path4')
            prtsc_range = (202, 767, 788, 68)
            q301 = list(pg.locateAllOnScreen("./img_web/f_1m.png", region=prtsc_range, confidence=0.9))
            q302 = list(pg.locateAllOnScreen("./img_web/f_2m.png", region=prtsc_range, confidence=0.9))
            q303 = list(pg.locateAllOnScreen("./img_web/f_3m.png", region=prtsc_range, confidence=0.9))
            q304 = list(pg.locateAllOnScreen("./img_web/f_4m.png", region=prtsc_range, confidence=0.9))
            q305a = list(pg.locateAllOnScreen("./img_web/f_5m.png", region=prtsc_range, confidence=0.9))
            q305b = list(pg.locateAllOnScreen("./img_web/f_5mr.png", region=prtsc_range, confidence=0.9))
            q305 = q305a + q305b
            q306 = list(pg.locateAllOnScreen("./img_web/f_6m.png", region=prtsc_range, confidence=0.9))
            q307 = list(pg.locateAllOnScreen("./img_web/f_7m.png", region=prtsc_range, confidence=0.9))
            q308 = list(pg.locateAllOnScreen("./img_web/f_8m.png", region=prtsc_range, confidence=0.9))
            q309 = list(pg.locateAllOnScreen("./img_web/f_9m.png", region=prtsc_range, confidence=0.9))
            q310 = list(pg.locateAllOnScreen("./img_web/f_1p.png", region=prtsc_range, confidence=0.9))
            q311 = list(pg.locateAllOnScreen("./img_web/f_2p.png", region=prtsc_range, confidence=0.9))
            q312 = list(pg.locateAllOnScreen("./img_web/f_3p.png", region=prtsc_range, confidence=0.9))
            q313 = list(pg.locateAllOnScreen("./img_web/f_4p.png", region=prtsc_range, confidence=0.9))
            q314a = list(pg.locateAllOnScreen("./img_web/f_5p.png", region=prtsc_range, confidence=0.9))
            q314b = list(pg.locateAllOnScreen("./img_web/f_5pr.png", region=prtsc_range, confidence=0.9))
            q314 = q314a + q314b
            q315 = list(pg.locateAllOnScreen("./img_web/f_6p.png", region=prtsc_range, confidence=0.9))
            q316 = list(pg.locateAllOnScreen("./img_web/f_7p.png", region=prtsc_range, confidence=0.9))
            q317 = list(pg.locateAllOnScreen("./img_web/f_8p.png", region=prtsc_range, confidence=0.9))
            q318 = list(pg.locateAllOnScreen("./img_web/f_9p.png", region=prtsc_range, confidence=0.9))
            q319 = list(pg.locateAllOnScreen("./img_web/f_1s.png", region=prtsc_range, confidence=0.9))
            q320 = list(pg.locateAllOnScreen("./img_web/f_2s.png", region=prtsc_range, confidence=0.9))
            q321 = list(pg.locateAllOnScreen("./img_web/f_3s.png", region=prtsc_range, confidence=0.9))
            q322 = list(pg.locateAllOnScreen("./img_web/f_4s.png", region=prtsc_range, confidence=0.9))
            q323a = list(pg.locateAllOnScreen("./img_web/f_5s.png", region=prtsc_range, confidence=0.9))
            q323b = list(pg.locateAllOnScreen("./img_web/f_5sr.png", region=prtsc_range, confidence=0.9))
            q323 = q323a + q323b
            q324 = list(pg.locateAllOnScreen("./img_web/f_6s.png", region=prtsc_range, confidence=0.9))
            q325 = list(pg.locateAllOnScreen("./img_web/f_7s.png", region=prtsc_range, confidence=0.9))
            q326 = list(pg.locateAllOnScreen("./img_web/f_8s.png", region=prtsc_range, confidence=0.9))
            q327 = list(pg.locateAllOnScreen("./img_web/f_9s.png", region=prtsc_range, confidence=0.9))
            q328 = list(pg.locateAllOnScreen("./img_web/f_E.png", region=prtsc_range, confidence=0.9))
            q329 = list(pg.locateAllOnScreen("./img_web/f_S.png", region=prtsc_range, confidence=0.9))
            q330 = list(pg.locateAllOnScreen("./img_web/f_We.png", region=prtsc_range, confidence=0.9))
            q331 = list(pg.locateAllOnScreen("./img_web/f_N.png", region=prtsc_range, confidence=0.9))
            q332 = list(pg.locateAllOnScreen("./img_web/f_Wh.png", region=prtsc_range, confidence=0.9))
            q333 = list(pg.locateAllOnScreen("./img_web/f_G.png", region=prtsc_range, confidence=0.9))
            q334 = list(pg.locateAllOnScreen("./img_web/f_R.png", region=prtsc_range, confidence=0.9))
            # q335 = list(pg.locateAllOnScreen("./img_web/f_5mr.png", region=prtsc_range, confidence=0.90))
            # q336 = list(pg.locateAllOnScreen("./img_web/f_5pr.png", region=prtsc_range, confidence=0.90))
            # q337 = list(pg.locateAllOnScreen("./img_web/f_5sr.png", region=prtsc_range, confidence=0.95))
            MySet = [q301,  q302,  q303,  q304,  q305,  q306,  q307,  q308,  q309, 
                q310, q311, q312, q313, q314, q315, q316, q317, q318, 
                q319, q320, q321, q322, q323, q324, q325, q326, q327, 
                q328, q329, q330, q331, q332, q333, q334]
            for i in range(34):
                if BoxValue_D(MySet[i]) != None:
                    for _ in range(len(BoxValue_D(MySet[i]))):
                        if self.Name[i] not in ['9m', '9p', '9s', 'N', 'Wh', 'R']:
                            Dora.append(self.Name[i+1])
                        if self.Name[i] == '9m':
                            Dora.append('1m')
                        if self.Name[i] == '9p':
                            Dora.append('1p')
                        if self.Name[i] == '9s':
                            Dora.append('1s')
                        if self.Name[i] == 'N':
                            Dora.append('E')
                        if self.Name[i] == 'R':
                            Dora.append('Wh')
                        if self.Name[i] == 'Wh' and Dora == []:
                            Dora.append('G')
        
        print('Dora: ', Dora)
        print('time.time()-t1 ', time.time()-t1)
        return Dora

    # 局の移り変わりの処理
    def GameChange(self, Dora, MyArrangement):
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
        if p3 != None:
            pg.moveTo(935, 785)
            pg.click()
            pg.moveTo(935, 790)
        p4 = pg.locateOnScreen("./img_web/AutoAgari.png", confidence=0.9)
        if p4 != None:
            pg.moveTo(651, 1011)
            pg.click()
            pg.moveTo(935, 790)

        r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
        # r2 = pg.locateOnScreen("./img_web/GameEND.png", confidence=0.9)
        # if r1 != None and r2 == None:
        if r1 != None:
            print('OK をチェックした。これからおよそ 10 秒後に配牌チェック')
            # ScreenShot()
            t1=time.time()
            # while r1 != None and r2 == None:
            while r1 != None:    
                r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
                # r2 = pg.locateOnScreen("./img_web/GameEND.png", confidence=0.9)
            print('time.time()-t1 ', time.time()-t1)
            MyArrangement = []
            time.sleep(2.5)
            self.Name = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                        '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                        '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                        'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
                        # '5mr', '5pr', '5sr']
            self.ReachState = []
            self.Member = 0
            self.Hou = []
            self.ReachBox = []
            self.CareBox = []
            self.Alert = []
            Dora = []
            self.Turn = []
            self.Escape = []
            self.UpdateRight = []
            self.UpdateCenter = []
            self.UpdateLeft = []
            self.r_attack = []
            self.c_attack = []
            self.l_attack = []
            self.r_ReachPiece = []
            self.c_ReachPiece = []
            self.l_ReachPiece = []
        
        return MyArrangement, self.ReachState, self.Member, self.Hou, self.ReachBox, self.CareBox, self.Alert, Dora, self.Turn, self.Escape, \
                self.UpdateRight, self.UpdateCenter, self.UpdateLeft, self.r_attack, self.c_attack, self.l_attack, self.r_ReachPiece, self.c_ReachPiece, self.l_ReachPiece

    # ツモ牌を手牌へ加えて、牌を捨てる関数・・・・時間のチェック用として仮作成
    def AutoButton2(self):
        # 巡目表示
        TmpTurn = len(self.Turn) + 1
        print(' ==================================================== ')
        print(TmpTurn, ' 巡目')

        # 手牌リスト作成（MyArrangement1) のチェック
        print('手牌', self.MyArrangement, '数',  len(self.MyArrangement))

        r = 0
        progress = 0
        print('ツモ待ち') 
        while r == 0:
            self.MyArrangement, self.ReachState, self.Member, self.Hou, self.ReachBox, self.CareBox, self.Alert, self.Dora, self.Turn, self.Escape, \
            self.UpdateRight, self.UpdateCenter, self.UpdateLeft, self.r_attack, self.c_attack, self.l_attack, self.r_ReachPiece, self.c_ReachPiece, self.l_ReachPiece = D.GameChange(self.Dora, self.MyArrangement)
            progress += 1
            if self.ReachState == []:
                print("\r" + ">> "*progress, end="")

            if self.Turn == [] and self.MyArrangement == []:
                self.MyArrangement = D.MyArrangement1(12, 892, 982, 106)
                print('配牌: ', self.MyArrangement, '数',  len(self.MyArrangement))

            q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
            if q == None and self.ReachState == []:
                if self.ReachBox == []:
                    # 積もったらまず、他家のリーチ状況を確認する。これは最優先で外せない。
                    self.s_r = pg.locateOnScreen("./img_web/Reach_Right.png", region=(695, 359, 256, 306), confidence=0.95)
                    self.s_c = pg.locateOnScreen("./img_web/Reach_Center.png", region=(388, 175, 340, 222), confidence=0.95)
                    self.s_l = pg.locateOnScreen("./img_web/Reach_Left.png", region=(233, 356, 210, 288), confidence=0.95)
                    # 他家から同順リーチが来た時は、下家－対面－上家の順で、一つだけに絞る。時間の関係上で。本当は全部処理したいが。。。
                    # また、今回の web 版でのリーチ認識では、牌が続いていくと見た目が変わるので、リーチ後最初の一巡しか認識チャンスが無いので注意。

                    if self.s_r != None:
                        print('下家-リーチ')
                        print(self.s_r)
                        self.ReachBox.extend(self.UpdateRight)
                        self.Alert.append(1)
                        self.r_ReachPiece = D.r_ReachPieceCheck()
                        print('宣言牌　', self.r_ReachPiece)
                        self.Escape.append(1)
                        self.UpdateCenter = D.Center(388, 175, 340, 222)
                        self.UpdateLeft = D.Left(186, 357, 264, 282)
                        if self.r_ReachPiece != []:
                            self.ReachBox.append(self.r_ReachPiece[0])
                    if self.s_c != None and self.s_r == None:
                        print('対面-リーチ')
                        self.ReachBox.extend(self.UpdateCenter)
                        self.Alert.append(1)
                        self.c_ReachPiece = D.c_ReachPieceCheck()
                        print('宣言牌　', self.c_ReachPiece)
                        self.Escape.append(1)
                        self.UpdateLeft = D.Left(186, 357, 264, 282)
                        self.UpdateRight = D.Right(688, 359, 256, 306)
                        if self.c_ReachPiece != []:
                            self.ReachBox.append(self.c_ReachPiece[0])
                    if self.s_l != None and self.s_r == None and self.s_c == None:
                        print('上家-リーチ')
                        self.ReachBox.extend(self.UpdateLeft)
                        self.Alert.append(1)
                        self.l_ReachPiece = D.l_ReachPieceCheck()
                        print('宣言牌　', self.l_ReachPiece)
                        self.Escape.append(1)
                        self.UpdateCenter = D.Center(388, 175, 340, 222)
                        self.UpdateRight = D.Right(688, 359, 256, 306)
                        if self.l_ReachPiece != []:
                            self.ReachBox.append(self.l_ReachPiece[0])

                self.r_attack, self.c_attack, self.l_attack = D.SituationCheck(0.85)

                if self.r_attack != [] and self.Alert == []:
                    print('下家-聴牌気配')
                    # self.UpdateRight = D.Right(688, 359, 256, 306)
                    self.CareBox.extend(self.UpdateRight)
                    self.CareBox = list(dict.fromkeys(self.CareBox))
                    if self.Escape == []:
                        self.Escape.append(1)
                if self.c_attack != [] and self.Alert == []:
                    print('対面-聴牌気配')
                    # self.UpdateCenter = D.Center(388, 175, 340, 222)
                    self.CareBox.extend(self.UpdateCenter)
                    self.CareBox = list(dict.fromkeys(self.CareBox))
                    if self.Escape == []:
                        self.Escape.append(1)
                if self.l_attack != [] and self.Alert == []:
                    print('上家-聴牌気配')
                    # self.UpdateLeft = D.Left(186, 357, 264, 282)
                    self.CareBox.extend(self.UpdateLeft)
                    self.CareBox = list(dict.fromkeys(self.CareBox))
                    if self.Escape == []:
                        self.Escape.append(1)
                if self.CareBox != [] and self.Alert == []:
                    print('2鳴き以上の他家の捨て牌: ', self.CareBox)
                if self.Alert != []:
                    print('リーチ以降の他家捨て牌:  ', self.ReachBox)
                r = 1
                break
        
        # リーチして積もった時
        if r == 1 and self.ReachState != []:
            return

        # # ツモってから、牌を選択して捨てる
        if r == 1 and self.ReachState == []:
            print('  ')
            pg.moveTo(447, 790)
            
            # ツモ牌を認識する。
            New = O.MyArrangement2(975, 896, 100, 108)
            print('ツモ牌', New)
            if New == None:
                New = ['Wh']
                print('ツモ牌認識エラー')
                print(' ')
            
            # # 手牌リストへ追加する。
            self.MyArrangement.append(New[0])
            
            print('手牌 切る前: ', self.MyArrangement, '数',  len(self.MyArrangement))
            print(' ')

            # 切る牌を選択する
            # print('self.Escape Before: ', self.Escape)

            Point, RedSign, self.Escape = O.SelectionExe(self.MyArrangement, self.Escape, self.ReachBox, self.CareBox, self.Dora)

            print('ツモ牌', New)
            print('捨てた牌', Point[0])
            print(' ')
            print('降りるかどうか: ', self.Escape)
            if self.Escape == [0]:
                print('[0] ⇒ 手作りを進める')
            if self.Escape == [1]:
                print('[1] ⇒ 降りる')

            Order = self.MyArrangement.index(Point[0])
            Positions = [(61, 946), (137, 946), (209, 946), (287, 946), (355, 946), (429, 946), (509, 946), 
                         (577, 946), (655, 946), (731, 946), (809, 946), (875, 946), (947, 946), (1029, 946)]
            
            
            # 自分の順番でリーチアイコンが出ているか
            s = pg.locateOnScreen("./img_web/Reach.png", confidence=0.9)
            # リーチアイコンのクリック（降りない時）
            if s != None and self.Escape != [1]:
                pg.moveTo(447, 790)
                pg.click()
                self.ReachState.append(1)

            print(' ')
            # 赤牌考慮は暫定。認識できるのを確認してから再考する。
            if RedSign == 0:
                print('切る牌の場所: ', Order)
                pg.moveTo(Positions[Order])
            if RedSign == 1 and New[0] not in ['5m', '5p', '5s']:
                print('切る牌の場所: ', Order+1)
                pg.moveTo(Positions[Order+1])
            time.sleep(0.1)
            pg.click()
            pg.moveTo(935, 790)

        # 手牌更新を追加する。ソートで。
        if self.ReachState == []:
            MyArrangementTmp = sorted(self.MyArrangement, key = self.Name.index)
            MyArrangementTmp.remove(Point[0])
            self.MyArrangement = MyArrangementTmp
            # print('手牌 切った後: ', self.MyArrangement, '数',  len(self.MyArrangement))
            self.Hou.append(Point[0])
            print('河: ', self.Hou)

        # if TmpTurn == 4 or TmpTurn == 10 or TmpTurn == 18:
        #     ScreenShot()
    
        time.sleep(1)
        if self.ReachState == []:
            # 手牌更新は極力やりたい。やらない弊害の方が多い。
            # q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
            # # r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
            # if q != None:
            # self.MyArrangement = D.MyArrangement1(10, 890, 990, 106)
            print('手牌', self.MyArrangement, '数',  len(self.MyArrangement))
        
        if self.Turn == [] and self.ReachState == []:
            self.Dora = D.DoraCheck(self.Dora, TmpTurn)
        print('ドラ牌: ', self.Dora)

        # リーチを受けた場合のチェックとして
        # print('リーチを受けた場合のチェックとして')
        # print('self.UpdateRight', self.UpdateRight)
        # print('self.UpdateCenter', self.UpdateCenter)
        # print('self.UpdateLeft', self.UpdateLeft)

        if len(self.Turn) > 1 and self.ReachState == []:
            self.UpdateRight, self.UpdateCenter, self.UpdateLeft, self.ReachBox = D.OtherPlayersSearch(self.s_r, self.s_c, self.s_l, self.Alert, self.r_attack, self.c_attack, self.l_attack, \
                                                                                                        self.UpdateRight, self.UpdateCenter, self.UpdateLeft)
        
        # 巡目更新
        self.Turn.append(1)

    # 手配リストを作成する関数（ツモ牌は除く）
    def MyArrangement1(self, left, top, width, depth):
        prtsc_range = (left, top, width, depth)
        t1 = time.time()
        q1 = list(pg.locateAllOnScreen("./img_web/1m.png", region=prtsc_range, confidence=0.9))
        q2 = list(pg.locateAllOnScreen("./img_web/2m.png", region=prtsc_range, confidence=0.9))
        q3 = list(pg.locateAllOnScreen("./img_web/3m.png", region=prtsc_range, confidence=0.9))
        q4 = list(pg.locateAllOnScreen("./img_web/4m.png", region=prtsc_range, confidence=0.9))
        q5a = list(pg.locateAllOnScreen("./img_web/5m.png", region=prtsc_range, confidence=0.9))
        q5b = list(pg.locateAllOnScreen("./img_web/5mr.png", region=prtsc_range, confidence=0.9))
        q5 = q5a + q5b
        q6 = list(pg.locateAllOnScreen("./img_web/6m.png", region=prtsc_range, confidence=0.9))
        q7 = list(pg.locateAllOnScreen("./img_web/7m.png", region=prtsc_range, confidence=0.9))
        q8 = list(pg.locateAllOnScreen("./img_web/8m.png", region=prtsc_range, confidence=0.9))
        q9 = list(pg.locateAllOnScreen("./img_web/9m.png", region=prtsc_range, confidence=0.9))
        q10 = list(pg.locateAllOnScreen("./img_web/1p.png", region=prtsc_range, confidence=0.9))
        q11 = list(pg.locateAllOnScreen("./img_web/2p.png", region=prtsc_range, confidence=0.9))
        q12 = list(pg.locateAllOnScreen("./img_web/3p.png", region=prtsc_range, confidence=0.9))
        q13 = list(pg.locateAllOnScreen("./img_web/4p.png", region=prtsc_range, confidence=0.9))
        q14a = list(pg.locateAllOnScreen("./img_web/5p.png", region=prtsc_range, confidence=0.9))
        q14b = list(pg.locateAllOnScreen("./img_web/5pr.png", region=prtsc_range, confidence=0.9))
        q14 = q14a + q14b
        q15 = list(pg.locateAllOnScreen("./img_web/6p.png", region=prtsc_range, confidence=0.9))
        q16 = list(pg.locateAllOnScreen("./img_web/7p.png", region=prtsc_range, confidence=0.9))
        q17 = list(pg.locateAllOnScreen("./img_web/8p.png", region=prtsc_range, confidence=0.9))
        q18 = list(pg.locateAllOnScreen("./img_web/9p.png", region=prtsc_range, confidence=0.9))
        q19 = list(pg.locateAllOnScreen("./img_web/1s.png", region=prtsc_range, confidence=0.9))
        q20 = list(pg.locateAllOnScreen("./img_web/2s.png", region=prtsc_range, confidence=0.9))
        q21 = list(pg.locateAllOnScreen("./img_web/3s.png", region=prtsc_range, confidence=0.9))
        q22 = list(pg.locateAllOnScreen("./img_web/4s.png", region=prtsc_range, confidence=0.9))
        q23a = list(pg.locateAllOnScreen("./img_web/5s.png", region=prtsc_range, confidence=0.9))
        q23b = list(pg.locateAllOnScreen("./img_web/5sr.png", region=prtsc_range, confidence=0.9))
        q23 = q23a + q23b
        q24 = list(pg.locateAllOnScreen("./img_web/6s.png", region=prtsc_range, confidence=0.9))
        q25 = list(pg.locateAllOnScreen("./img_web/7s.png", region=prtsc_range, confidence=0.9))
        q26 = list(pg.locateAllOnScreen("./img_web/8s.png", region=prtsc_range, confidence=0.9))
        q27 = list(pg.locateAllOnScreen("./img_web/9s.png", region=prtsc_range, confidence=0.9))
        q28 = list(pg.locateAllOnScreen("./img_web/E.png", region=prtsc_range, confidence=0.9))
        q29 = list(pg.locateAllOnScreen("./img_web/S.png", region=prtsc_range, confidence=0.9))
        q30 = list(pg.locateAllOnScreen("./img_web/We.png", region=prtsc_range, confidence=0.9))
        q31 = list(pg.locateAllOnScreen("./img_web/N.png", region=prtsc_range, confidence=0.9))
        q32 = list(pg.locateAllOnScreen("./img_web/Wh.png", region=prtsc_range, confidence=0.9))
        q33 = list(pg.locateAllOnScreen("./img_web/G.png", region=prtsc_range, confidence=0.9))
        q34 = list(pg.locateAllOnScreen("./img_web/R.png", region=prtsc_range, confidence=0.9))
        q35 = list(pg.locateAllOnScreen("./img_web/5mr.png", region=prtsc_range, confidence=0.90))
        q36 = list(pg.locateAllOnScreen("./img_web/5pr.png", region=prtsc_range, confidence=0.90))
        q37 = list(pg.locateAllOnScreen("./img_web/5sr.png", region=prtsc_range, confidence=0.95))
        t2 = time.time()
        MySet = [q1,  q2,  q3,  q4,  q5,  q6,  q7,  q8,  q9, 
                q10, q11, q12, q13, q14, q15, q16, q17, q18, 
                q19, q20, q21, q22, q23, q24, q25, q26, q27, 
                q28, q29, q30, q31, q32, q33, q34, 
                q35, q36, q37]
        self.MyArrangement = []
        for i in range(34):
            if BoxValue(MySet[i]) != None:
                for _ in range(len(BoxValue(MySet[i]))):
                    self.MyArrangement.append(self.Name[i])
        
        # Web 版は順番替えはない模様
        # NameCheck_m = 0
        # NameCheck_p = 0
        # NameCheck_s = 0
        # for j in range(len(self.MyArrangement)):
        #     if self.MyArrangement[j] in ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m'] and NameCheck_m != 1:
        #         NameCheck_m = 1
        #     if self.MyArrangement[j] in ['1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p'] and NameCheck_p != 1:
        #         NameCheck_p = 1
        #     if self.MyArrangement[j] in ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s'] and NameCheck_s != 1:
        #         NameCheck_s = 1
        # if [NameCheck_m, NameCheck_p, NameCheck_s] == [1, 0, 1]:
        #     self.Name = self.Name2
        #     print('self.Name Change to: ', self.Name2)
        # if [NameCheck_m, NameCheck_p, NameCheck_s] == [0, 1, 0]:
        #     self.Name = self.Name3
        #     print('self.Name Change to: ', self.Name3)
        # if [NameCheck_m, NameCheck_p, NameCheck_s] == [0, 1, 1]:
        #     self.Name = self.Name4
        #     print('self.Name Change to: ', self.Name4)
        # if [NameCheck_m, NameCheck_p, NameCheck_s] == [0, 0, 1]:
        #     self.Name = self.Name5
        #     print('self.Name Change to: ', self.Name5)
        # if [NameCheck_m, NameCheck_p, NameCheck_s] == [0, 1, 1] and self.Name == self.Name5 :
        #     self.Name = self.Name6
        #     print('self.Name Change to: ', self.Name6)

        # Wh は2枚以上続くと認識しないので、補正する。
        # print('Wh 補正前：', self.MyArrangement)
        if len(self.MyArrangement) <= 12:
            self.MyArrangement.append('Wh')
            self.MyArrangement = sorted(self.MyArrangement, key = self.Name.index)

        print('Time of MyArrangement1: ', t2-t1)
        return self.MyArrangement

    def Right(self, left, top, width, depth):
        prtsc_range = (left, top, width, depth)
        q1 = list(pg.locateAllOnScreen("./img_web/r_1m.png", region=prtsc_range, confidence=0.9))
        q2 = list(pg.locateAllOnScreen("./img_web/r_2m.png", region=prtsc_range, confidence=0.9))
        q3 = list(pg.locateAllOnScreen("./img_web/r_3m.png", region=prtsc_range, confidence=0.9))
        q4 = list(pg.locateAllOnScreen("./img_web/r_4m.png", region=prtsc_range, confidence=0.9))
        q5a = list(pg.locateAllOnScreen("./img_web/r_5m.png", region=prtsc_range, confidence=0.9))
        q5b = list(pg.locateAllOnScreen("./img_web/r_5mr.png", region=prtsc_range, confidence=0.9))
        q5 = q5a + q5b
        q6 = list(pg.locateAllOnScreen("./img_web/r_6m.png", region=prtsc_range, confidence=0.9))
        q7 = list(pg.locateAllOnScreen("./img_web/r_7m.png", region=prtsc_range, confidence=0.9))
        q8 = list(pg.locateAllOnScreen("./img_web/r_8m.png", region=prtsc_range, confidence=0.9))
        q9 = list(pg.locateAllOnScreen("./img_web/r_9m.png", region=prtsc_range, confidence=0.9))
        q10 = list(pg.locateAllOnScreen("./img_web/r_1p.png", region=prtsc_range, confidence=0.9))
        q11 = list(pg.locateAllOnScreen("./img_web/r_2p.png", region=prtsc_range, confidence=0.9))
        q12 = list(pg.locateAllOnScreen("./img_web/r_3p.png", region=prtsc_range, confidence=0.9))
        q13 = list(pg.locateAllOnScreen("./img_web/r_4p.png", region=prtsc_range, confidence=0.9))
        q14a = list(pg.locateAllOnScreen("./img_web/r_5p.png", region=prtsc_range, confidence=0.9))
        q14b = list(pg.locateAllOnScreen("./img_web/r_5pr.png", region=prtsc_range, confidence=0.9))
        q14 = q14a + q14b
        q15 = list(pg.locateAllOnScreen("./img_web/r_6p.png", region=prtsc_range, confidence=0.9))
        q16 = list(pg.locateAllOnScreen("./img_web/r_7p.png", region=prtsc_range, confidence=0.9))
        q17 = list(pg.locateAllOnScreen("./img_web/r_8p.png", region=prtsc_range, confidence=0.9))
        q18 = list(pg.locateAllOnScreen("./img_web/r_9p.png", region=prtsc_range, confidence=0.9))
        q19 = list(pg.locateAllOnScreen("./img_web/r_1s.png", region=prtsc_range, confidence=0.9))
        q20 = list(pg.locateAllOnScreen("./img_web/r_2s.png", region=prtsc_range, confidence=0.9))
        q21 = list(pg.locateAllOnScreen("./img_web/r_3s.png", region=prtsc_range, confidence=0.9))
        q22 = list(pg.locateAllOnScreen("./img_web/r_4s.png", region=prtsc_range, confidence=0.9))
        q23a = list(pg.locateAllOnScreen("./img_web/r_5s.png", region=prtsc_range, confidence=0.9))
        q23b = list(pg.locateAllOnScreen("./img_web/r_5sr.png", region=prtsc_range, confidence=0.9))
        q23 = q23a + q23b
        q24 = list(pg.locateAllOnScreen("./img_web/r_6s.png", region=prtsc_range, confidence=0.9))
        q25 = list(pg.locateAllOnScreen("./img_web/r_7s.png", region=prtsc_range, confidence=0.9))
        q26 = list(pg.locateAllOnScreen("./img_web/r_8s.png", region=prtsc_range, confidence=0.9))
        q27 = list(pg.locateAllOnScreen("./img_web/r_9s.png", region=prtsc_range, confidence=0.9))
        q28 = list(pg.locateAllOnScreen("./img_web/r_E.png", region=prtsc_range, confidence=0.9))
        q29 = list(pg.locateAllOnScreen("./img_web/r_S.png", region=prtsc_range, confidence=0.9))
        q30 = list(pg.locateAllOnScreen("./img_web/r_We.png", region=prtsc_range, confidence=0.9))
        q31 = list(pg.locateAllOnScreen("./img_web/r_N.png", region=prtsc_range, confidence=0.9))
        q32 = list(pg.locateAllOnScreen("./img_web/r_Wh.png", region=prtsc_range, confidence=0.9))
        q33 = list(pg.locateAllOnScreen("./img_web/r_G.png", region=prtsc_range, confidence=0.9))
        q34 = list(pg.locateAllOnScreen("./img_web/r_R.png", region=prtsc_range, confidence=0.9))
        # q35 = list(pg.locateAllOnScreen("./img_web/r_5mr.png", region=prtsc_range, confidence=0.90))
        # q36 = list(pg.locateAllOnScreen("./img_web/r_5pr.png", region=prtsc_range, confidence=0.90))
        # q37 = list(pg.locateAllOnScreen("./img_web/r_5sr.png", region=prtsc_range, confidence=0.95))
        
        MySet = [q1,  q2,  q3,  q4,  q5,  q6,  q7,  q8,  q9, 
                q10, q11, q12, q13, q14, q15, q16, q17, q18, 
                q19, q20, q21, q22, q23, q24, q25, q26, q27, 
                q28, q29, q30, q31, q32, q33, q34]
                # q35, q36, q37]

        self.Name = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', 
                        '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
                        '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                        'E',  'S',  'We', 'N',  'Wh', 'G',  'R']
                        # '5mr', '5pr', '5sr']

        self.RightList = []
        for i in range(34):
            if BoxValue_D(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    self.RightList.append(self.Name[i])
        
        return self.RightList

    def Center(self, left, top, width, depth):
        prtsc_range = (left, top, width, depth)
        q1 = list(pg.locateAllOnScreen("./img_web/c_1m.png", region=prtsc_range, confidence=0.9))
        q2 = list(pg.locateAllOnScreen("./img_web/c_2m.png", region=prtsc_range, confidence=0.9))
        q3 = list(pg.locateAllOnScreen("./img_web/c_3m.png", region=prtsc_range, confidence=0.9))
        q4 = list(pg.locateAllOnScreen("./img_web/c_4m.png", region=prtsc_range, confidence=0.9))
        q5a = list(pg.locateAllOnScreen("./img_web/c_5m.png", region=prtsc_range, confidence=0.9))
        q5b = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.9))
        q5 = q5a + q5b
        q6 = list(pg.locateAllOnScreen("./img_web/c_6m.png", region=prtsc_range, confidence=0.9))
        q7 = list(pg.locateAllOnScreen("./img_web/c_7m.png", region=prtsc_range, confidence=0.9))
        q8 = list(pg.locateAllOnScreen("./img_web/c_8m.png", region=prtsc_range, confidence=0.9))
        q9 = list(pg.locateAllOnScreen("./img_web/c_9m.png", region=prtsc_range, confidence=0.9))
        q10 = list(pg.locateAllOnScreen("./img_web/c_1p.png", region=prtsc_range, confidence=0.9))
        q11 = list(pg.locateAllOnScreen("./img_web/c_2p.png", region=prtsc_range, confidence=0.9))
        q12 = list(pg.locateAllOnScreen("./img_web/c_3p.png", region=prtsc_range, confidence=0.9))
        q13 = list(pg.locateAllOnScreen("./img_web/c_4p.png", region=prtsc_range, confidence=0.9))
        q14a = list(pg.locateAllOnScreen("./img_web/c_5p.png", region=prtsc_range, confidence=0.9))
        q14b = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.9))
        q14 = q14a + q14b
        q15 = list(pg.locateAllOnScreen("./img_web/c_6p.png", region=prtsc_range, confidence=0.9))
        q16 = list(pg.locateAllOnScreen("./img_web/c_7p.png", region=prtsc_range, confidence=0.9))
        q17 = list(pg.locateAllOnScreen("./img_web/c_8p.png", region=prtsc_range, confidence=0.9))
        q18 = list(pg.locateAllOnScreen("./img_web/c_9p.png", region=prtsc_range, confidence=0.9))
        q19 = list(pg.locateAllOnScreen("./img_web/c_1s.png", region=prtsc_range, confidence=0.9))
        q20 = list(pg.locateAllOnScreen("./img_web/c_2s.png", region=prtsc_range, confidence=0.9))
        q21 = list(pg.locateAllOnScreen("./img_web/c_3s.png", region=prtsc_range, confidence=0.9))
        q22 = list(pg.locateAllOnScreen("./img_web/c_4s.png", region=prtsc_range, confidence=0.9))
        q23a = list(pg.locateAllOnScreen("./img_web/c_5s.png", region=prtsc_range, confidence=0.9))
        q23b = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.9))
        q23 = q23a + q23b
        q24 = list(pg.locateAllOnScreen("./img_web/c_6s.png", region=prtsc_range, confidence=0.9))
        q25 = list(pg.locateAllOnScreen("./img_web/c_7s.png", region=prtsc_range, confidence=0.9))
        q26 = list(pg.locateAllOnScreen("./img_web/c_8s.png", region=prtsc_range, confidence=0.9))
        q27 = list(pg.locateAllOnScreen("./img_web/c_9s.png", region=prtsc_range, confidence=0.9))
        q28 = list(pg.locateAllOnScreen("./img_web/c_E.png", region=prtsc_range, confidence=0.9))
        q29 = list(pg.locateAllOnScreen("./img_web/c_S.png", region=prtsc_range, confidence=0.9))
        q30 = list(pg.locateAllOnScreen("./img_web/c_We.png", region=prtsc_range, confidence=0.9))
        q31 = list(pg.locateAllOnScreen("./img_web/c_N.png", region=prtsc_range, confidence=0.9))
        q32 = list(pg.locateAllOnScreen("./img_web/c_Wh.png", region=prtsc_range, confidence=0.9))
        q33 = list(pg.locateAllOnScreen("./img_web/c_G.png", region=prtsc_range, confidence=0.9))
        q34 = list(pg.locateAllOnScreen("./img_web/c_R.png", region=prtsc_range, confidence=0.9))
        # q35 = list(pg.locateAllOnScreen("./img_web/c_5mr.png", region=prtsc_range, confidence=0.90))
        # q36 = list(pg.locateAllOnScreen("./img_web/c_5pr.png", region=prtsc_range, confidence=0.90))
        # q37 = list(pg.locateAllOnScreen("./img_web/c_5sr.png", region=prtsc_range, confidence=0.95))
        MySet = [q1,  q2,  q3,  q4,  q5,  q6,  q7,  q8,  q9, 
                q10, q11, q12, q13, q14, q15, q16, q17, q18, 
                q19, q20, q21, q22, q23, q24, q25, q26, q27, 
                q28, q29, q30, q31, q32, q33, q34]
        #         q35, q36, q37]
        self.CenterList = []
        for i in range(len(MySet)):
            if BoxValue(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    self.CenterList.append(self.Name[i])
        
        return self.CenterList
    
    def Left(self, left, top, width, depth):
        prtsc_range = (left, top, width, depth)
        q1 = list(pg.locateAllOnScreen("./img_web/l_1m.png", region=prtsc_range, confidence=0.9))
        q2 = list(pg.locateAllOnScreen("./img_web/l_2m.png", region=prtsc_range, confidence=0.9))
        q3 = list(pg.locateAllOnScreen("./img_web/l_3m.png", region=prtsc_range, confidence=0.9))
        q4 = list(pg.locateAllOnScreen("./img_web/l_4m.png", region=prtsc_range, confidence=0.9))
        q5a = list(pg.locateAllOnScreen("./img_web/l_5m.png", region=prtsc_range, confidence=0.9))
        q5b = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.9))
        q5 = q5a + q5b
        q6 = list(pg.locateAllOnScreen("./img_web/l_6m.png", region=prtsc_range, confidence=0.9))
        q7 = list(pg.locateAllOnScreen("./img_web/l_7m.png", region=prtsc_range, confidence=0.9))
        q8 = list(pg.locateAllOnScreen("./img_web/l_8m.png", region=prtsc_range, confidence=0.9))
        q9 = list(pg.locateAllOnScreen("./img_web/l_9m.png", region=prtsc_range, confidence=0.9))
        q10 = list(pg.locateAllOnScreen("./img_web/l_1p.png", region=prtsc_range, confidence=0.9))
        q11 = list(pg.locateAllOnScreen("./img_web/l_2p.png", region=prtsc_range, confidence=0.9))
        q12 = list(pg.locateAllOnScreen("./img_web/l_3p.png", region=prtsc_range, confidence=0.9))
        q13 = list(pg.locateAllOnScreen("./img_web/l_4p.png", region=prtsc_range, confidence=0.9))
        q14a = list(pg.locateAllOnScreen("./img_web/l_5p.png", region=prtsc_range, confidence=0.9))
        q14b = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.9))
        q14 = q14a + q14b
        q15 = list(pg.locateAllOnScreen("./img_web/l_6p.png", region=prtsc_range, confidence=0.9))
        q16 = list(pg.locateAllOnScreen("./img_web/l_7p.png", region=prtsc_range, confidence=0.9))
        q17 = list(pg.locateAllOnScreen("./img_web/l_8p.png", region=prtsc_range, confidence=0.9))
        q18 = list(pg.locateAllOnScreen("./img_web/l_9p.png", region=prtsc_range, confidence=0.9))
        q19 = list(pg.locateAllOnScreen("./img_web/l_1s.png", region=prtsc_range, confidence=0.9))
        q20 = list(pg.locateAllOnScreen("./img_web/l_2s.png", region=prtsc_range, confidence=0.9))
        q21 = list(pg.locateAllOnScreen("./img_web/l_3s.png", region=prtsc_range, confidence=0.9))
        q22 = list(pg.locateAllOnScreen("./img_web/l_4s.png", region=prtsc_range, confidence=0.9))
        q23a = list(pg.locateAllOnScreen("./img_web/l_5s.png", region=prtsc_range, confidence=0.9))
        q23b = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.9))
        q23 = q23a + q23b
        q24 = list(pg.locateAllOnScreen("./img_web/l_6s.png", region=prtsc_range, confidence=0.9))
        q25 = list(pg.locateAllOnScreen("./img_web/l_7s.png", region=prtsc_range, confidence=0.9))
        q26 = list(pg.locateAllOnScreen("./img_web/l_8s.png", region=prtsc_range, confidence=0.9))
        q27 = list(pg.locateAllOnScreen("./img_web/l_9s.png", region=prtsc_range, confidence=0.9))
        q28 = list(pg.locateAllOnScreen("./img_web/l_E.png", region=prtsc_range, confidence=0.9))
        q29 = list(pg.locateAllOnScreen("./img_web/l_S.png", region=prtsc_range, confidence=0.9))
        q30 = list(pg.locateAllOnScreen("./img_web/l_We.png", region=prtsc_range, confidence=0.9))
        q31 = list(pg.locateAllOnScreen("./img_web/l_N.png", region=prtsc_range, confidence=0.9))
        q32 = list(pg.locateAllOnScreen("./img_web/l_Wh.png", region=prtsc_range, confidence=0.9))
        q33 = list(pg.locateAllOnScreen("./img_web/l_G.png", region=prtsc_range, confidence=0.9))
        q34 = list(pg.locateAllOnScreen("./img_web/l_R.png", region=prtsc_range, confidence=0.9))
        # q35 = list(pg.locateAllOnScreen("./img_web/l_5mr.png", region=prtsc_range, confidence=0.90))
        # q36 = list(pg.locateAllOnScreen("./img_web/l_5pr.png", region=prtsc_range, confidence=0.90))
        # q37 = list(pg.locateAllOnScreen("./img_web/l_5sr.png", region=prtsc_range, confidence=0.95))
        MySet = [q1,  q2,  q3,  q4,  q5,  q6,  q7,  q8,  q9, 
                q10, q11, q12, q13, q14, q15, q16, q17, q18, 
                q19, q20, q21, q22, q23, q24, q25, q26, q27, 
                q28, q29, q30, q31, q32, q33, q34]
        #         q35, q36, q37]
        
        self.LeftList = []
        for i in range(len(MySet)):
            if BoxValue_D(MySet[i]) != None:
                for _ in range(len(BoxValue_D(MySet[i]))):
                    self.LeftList.append(self.Name[i])

        return self.LeftList

    def OtherPlayersSearch(self, s_r, s_c, s_l, Alert, r_attack, c_attack, l_attack, UpdateRight, UpdateCenter, UpdateLeft):
        num = random.randint(1, 9)
        # if num % 3 == 0 or Alert != [] or l_attack != []:
        if Alert != [] or l_attack != []:
            q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
            # r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
            if q != None:
                L = D.Left(186, 357, 264, 282)
                print(' ')
                if L != []:
                    Diff_L = list_difference(L, UpdateLeft)
                    if Diff_L != []:
                        # 一個一個繋げなくて、一気にくっつけていい。
                        UpdateLeft.extend(Diff_L)
                        # print('★Diff(Left)', Diff_L)

                        # ReachBox への付加。他家のいずれかにリーチがかかっていたら、毎回実行する。
                        if s_r != None or s_c != None or s_l != None :
                            self.ReachBox.extend(Diff_L)
                            print('上家-捨て牌-差分', Diff_L)
                            self.ReachBox = list(dict.fromkeys(self.ReachBox))
                            
                    print('上家-捨て牌', UpdateLeft)
                    print(' ')
    
        # if num % 3 == 1 or Alert != [] or c_attack != []:
        if Alert != [] or c_attack != []:
            q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
            # r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
            if q != None:
                C = D.Center(388, 175, 340, 222)
                print(' ')
                if C != []:
                    Diff_C = list_difference(C, UpdateCenter)
                    if Diff_C != []:
                        # 一個一個繋げなくて、一気にくっつけていい。
                        UpdateCenter.extend(Diff_C)
                        # print('★Diff(Center)', Diff_C)

                        # ReachBox への付加。他家のいずれかにリーチがかかっていたら、毎回実行する。
                        if s_r != None or s_c != None or s_l != None :
                            self.ReachBox.extend(Diff_C)
                            print('対面-捨て牌-差分', Diff_C)
                            self.ReachBox = list(dict.fromkeys(self.ReachBox))

                    print('対面-捨て牌', UpdateCenter)
                    print(' ')

        # if num % 3 == 2 or Alert != [] or r_attack != []:
        if Alert != [] or r_attack != []:
            q = pg.locateOnScreen("./img_web/TumoPosition.png", confidence=0.9)
            # r1 = pg.locateOnScreen("./img_web/ToNextOK.png", confidence=0.9)
            if q != None:
                R = D.Right(688, 359, 256, 306)
                print(' ')
                if R != []:
                    Diff_R = list_difference(R, UpdateRight)
                    if Diff_R != []:
                        # 一個一個繋げなくて、一気にくっつけていい。
                        UpdateRight.extend(Diff_R)
                        # print('★Diff(Right)', Diff_R)

                        # ReachBox への付加。他家のいずれかにリーチがかかっていたら、毎回実行する。
                        if s_r != None or s_c != None or s_l != None :
                            self.ReachBox.extend(Diff_R)
                            print('下家-捨て牌-差分', Diff_R)
                            self.ReachBox = list(dict.fromkeys(self.ReachBox))

                    print('上家-捨て牌', UpdateRight)
                    print(' ')
        
        return UpdateRight, UpdateCenter, UpdateLeft, self.ReachBox

    def SituationCheck(self, conf):
        # 他家の鳴き状況
        s_rC1 = pg.locateOnScreen("./img_web/r_Corner1.png", confidence=conf)
        s_rC2 = pg.locateOnScreen("./img_web/r_Corner2.png", region = (1016, 384, 102, 146), confidence=conf)
        s_cC1 = pg.locateOnScreen("./img_web/c_Corner1.png", confidence=0.99)
        s_cC2 = pg.locateOnScreen("./img_web/c_Corner2.png", region = (341, 50, 238, 106), confidence=conf)
        s_lC1 = pg.locateOnScreen("./img_web/l_Corner1.png", confidence=conf)
        s_lC2 = pg.locateOnScreen("./img_web/l_Corner2.png", region = (11, 450, 104, 132), confidence=conf)
        # if s_rC1 != None:
        #     print('下家-面前')
        if s_rC1 == None and s_rC2 != None:
            print('下家 1 鳴き')
        if s_rC1 == None and s_rC2 == None:
            print('下家 2 鳴き')
            self.r_attack.append(1)
        # if s_cC1 != None:
        #     print('対面-面前')
        if s_cC1 == None and s_cC2 != None:
            print('対面 1 鳴き')
        if s_cC1 == None and s_cC2 == None:
            print('対面 2 鳴き')
            self.c_attack.append(1)
        # if s_lC1 != None:
        #     print('上家-面前')
        if s_lC1 == None and s_lC2 != None:
            print('上家 1 鳴き')
        if s_lC1 == None and s_lC2 == None:
            print('上家 2 鳴き')
            self.l_attack.append(1)
        print(' ')
        return self.r_attack, self.c_attack, self.l_attack

D = D_Execusion()
O = O_Execusion()
