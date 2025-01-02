from function_data.bgdata import *
import random
import os
from function_data.button import *

class Game_algorithm():
    def __init__(self,screen):
        self.surf = screen
        self.round = 0
        self.price = 0
        self.prevous_card = {}
        self.current_card = {}
        #创建各种牌组和字典（地主牌3张，3个玩家各17张）
        poker_image_path = r'PNG-cards-1.3'
        imgs = os.listdir(poker_image_path)
        self.poker = {}
        self.choosed_dizhu_poker = {}
        self.choosed_poker01 = {}
        self.choosed_poker02 = {}
        self.user_choosed_poker = {}
        self.choosed_poker_cache = {}
        self.choose_poker = []
        #调用先前写好的按钮函数
        self.increase_btn = Button(self.surf,1200,650,'increase')
        self.decrease_btn = Button(self.surf,1200,750,'decrease')
        self.bet_button = Button(self.surf,1450,750,'bet')
        self.grab_button = Button(self.surf,1450,850,'be the landlord')
        self.unrob_button = Button(self.surf,1450,900,'be the people')
        self.pass_btn = Button(self.surf,1200,650,'pass')
        self.play_btn = Button(self.surf,1200,650,'pass')
        #要把下注的金额绘制出来
        self.pricetext = pygame.font.Font(None,100)
        self.priceshow = self.pricetext.render(''.join(str(self.price)),True,(255,255,255))
        self.card_start_point = [450,750]
        self.position = 0
        self.card_blit_point = {}
        self.choosen = False
        #往牌组里随机抽出牌然后分别放入（地主牌，3个玩家各17张）
        for p in imgs:
            baba = os.path.dirname(os.path.abspath(p))
            self.haha = os.path.join(baba,poker_image_path+'\\'+p)
            self.image_surface = pygame.image.load(self.haha)
            poker_dict = {p:self.image_surface}
            self.poker.update(poker_dict)
            print(p,)
        #地主牌的
        for a in range(3):
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_dizhu_poker.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
        #3个玩家的
        for b in range(17):
            #ai的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker01.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
            #ai的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker02.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
            #玩家的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.user_choosed_poker.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
        
        
    def run(self,event,mouseevent):
        #创建第零回合，询问是否抢地主
        if self.round == 0:
            grab = self.grab_button.clickbutton(mouseevent,event)
            ungrab = self.unrob_button.clickbutton(mouseevent,event)
            if grab == True:
                self.round += 1
                self.choosen = True
            if ungrab == True:
                self.round += 1
                self.choosen == False
        #第一回合需要下注与创建玩家所持的卡的字典，其中是{卡的surface：【卡绘制的位置x，卡绘制的位置y】}
        elif self.round == 1:
            high = self.increase_btn.clickbutton(mouseevent,event)
            low = self.decrease_btn.clickbutton(mouseevent,event)
            bet = self.bet_button.clickbutton(mouseevent,event)
            pygame.draw.rect(self.surf,(74,74,74),(1450,650,200,60))
            self.surf.blit(self.priceshow,(1450,650))
            if high == True:
                self.price += 100
                if self.price >= 10000:
                    self.price = 10000
                self.priceshow = self.pricetext.render(''.join(str(self.price)),True,(255,255,255))
            if low == True:
                self.price -= 100
                if self.price <= 0:
                    self.price = 0
                self.priceshow = self.pricetext.render(''.join(str(self.price)),True,(255,255,255))
            if bet == True and self.price != 0 and self.choosen == False:#判断是否抢地主
                for d in self.user_choosed_poker.values():
                    self.cache = {d:[self.card_start_point[0]+self.position,self.card_start_point[1]]}
                    self.card_blit_point.update(self.cache)
                    self.position += 50
                self.round += 1
                print(self.card_blit_point)
            if bet == True and self.price != 0 and self.choosen == True:#判断是否抢地主
                self.user_choosed_poker.update(self.choosed_dizhu_poker)#抢了地主会额外拿到3张牌
                for d in self.user_choosed_poker.values():
                    self.cache = {d:[self.card_start_point[0]+self.position,self.card_start_point[1]]}
                    self.card_blit_point.update(self.cache)
                    self.position += 50
                self.round += 1
                print(self.card_blit_point)
        else:
            Game_algorithm.draw_cards(self,event,mouseevent)
            passround = self.pass_btn.clickbutton(mouseevent,event)
            if passround:
                self.round += 1
                #here the ai algorithm
                Game_algorithm.ai_alorithm(self)
            ans = Game_algorithm.check_hand(self)
            if ans:
                play = self.play_btn.clickbutton(mouseevent,event)
                if play:
                    Game_algorithm.ai_alorithm(self)
            else:
                pass
    def draw_cards(self,event,mouseevent):
        for c in self.user_choosed_poker.values():
            self.image_scale = pygame.Rect(self.card_blit_point[c][0],self.card_blit_point[c][1],49,145)
            self.surf.blit(c,self.card_blit_point[c])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.image_scale.collidepoint(mouseevent):
                    if self.card_blit_point[c][1] == 750:
                        self.card_blit_point[c] = {c:[self.card_blit_point[c][0],700]}
                    if self.card_blit_point[c][1] == 700:
                        self.card_blit_point[c] = {c:[self.card_blit_point[c][0],750]}

    def ai_alorithm(self):
        None
    def check_hand(self):
        for e in self.user_choosed_poker.keys():
            if self.card_blit_point[self.user_choosed_poker[e]][1] == 700:
                self.choosed_poker_cache = {e:self.user_choosed_poker[e]}
                self.current_card.update(self.choosed_poker_cache)
                print(self.current_card)