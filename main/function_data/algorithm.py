from function_data.bgdata import *
import random
import os
from function_data.button import *

class Game_algorithm():
    def __init__(self,screen):
        self.surf = screen
        poker_image_path = r'PNG-cards-1.3'
        imgs = os.listdir(poker_image_path)
        self.poker = {}
        self.choosed_dizhu_poker = {}
        self.choosed_poker01 = {}
        self.choosed_poker02 = {}
        self.user_choosed_poker = {}
        self.choosed_poker_cache = {}
        self.choose_poker = []
        self.round = 0
        self.price = 0
        self.increase_btn = Button(self.surf,1200,650,'increase')
        self.decrease_btn = Button(self.surf,1200,750,'decrease')
        self.bet_button = Button(self.surf,1450,750,'bet')
        self.pricetext = pygame.font.Font(None,100)
        self.priceshow = self.pricetext.render(''.join(str(self.price)),True,(255,255,255))
        self.card_start_point = [450,750]
        for p in imgs:
            baba = os.path.dirname(os.path.abspath(p))
            self.haha = os.path.join(baba,poker_image_path+'\\'+p)
            self.image_path = pygame.image.load(self.haha)
            poker_dict = {p:self.image_path}
            self.poker.update(poker_dict)

        for self.a in range(3):
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_dizhu_poker.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
        
        for b in range(17):
            
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker01.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]

            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker02.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]

            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.user_choosed_poker.update(self.choosed_poker_cache)
            del self.poker[self.choose_poker]
        
        self.count = list(self.user_choosed_poker.values())

    def run(self,event,mouseevent):
        if self.round == 0:
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
            if bet == True and self.price != 0:
                self.round += 1
        else:
            Game_algorithm.draw_cards(self)
            Game_algorithm.collided_cards(self,event,mouseevent)
    def draw_cards(self):
        for c in self.user_choosed_poker.values():
            self.ans = self.surf.blit(c,self.card_start_point)
            self.card_start_point[0] += 50
            if self.card_start_point[0] >= 1300:
                self.card_start_point[0] = 450
        
        for d in self.user_choosed_poker.values():
            pass
    def collided_cards(self,event,mouseevent):
        self.card_hitbox = pygame.Rect(self.card_start_point[0],self.card_start_point[1],49,145)
        pygame.draw.rect(self.surf,(255,255,255),self.card_hitbox)
        if self.card_hitbox.collidepoint(mouseevent):
            self.card_start_point[1] = 700
        else:
            self.card_start_point[1] = 750
    def alorithm(self):
        None
    def check_card(self):
        None