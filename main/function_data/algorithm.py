from function_data.bgdata import *
import random
import os
from function_data.button import *

class Game_algorithm():
    def __init__(self,screen):
        self.surf = screen
        poker_image_path = r'PNG-cards-1.3'
        imgs = os.listdir(poker_image_path)
        self.poker = []
        self.choosed_dizhu_poker = []
        self.choosed_poker01 = []
        self.choosed_poker02 = []
        self.user_choosed_poker = []
        self.round = 0
        self.price = 0
        self.increase_btn = Button(self.surf,1200,650,'increase')
        self.decrease_btn = Button(self.surf,1200,750,'decrease')
        self.bet_button = Button(self.surf,1450,750,'bet')
        self.pricetext = pygame.font.Font(None,100)
        self.priceshow = self.pricetext.render(''.join(str(self.price)),True,(255,255,255))
        self.suit = ['a','b','c','d']
        self.rank = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

        for p in imgs:
            baba = os.path.dirname(os.path.abspath(p))
            haha = os.path.join(baba,poker_image_path+'\\'+p)
            self.image_path = pygame.image.load(haha)
            self.poker.append(self.image_path)
            print(p)
        for x in range(4):
            for y in range(13):
                self.cards = {self.suit[x]+self.rank[y]:self.image_path}
                

        for a in range(3):
            dizhupai = random.choice(self.poker)
            self.choosed_dizhu_poker.append(dizhupai)
            self.poker.remove(dizhupai)
            
        for b in range(17):
            player1 = random.choice(self.poker)
            self.choosed_poker01.append(player1)
            self.poker.remove(player1)
            player2 = random.choice(self.poker)
            self.choosed_poker02.append(player2)
            self.poker.remove(player2)
            player3 = random.choice(self.poker)
            self.user_choosed_poker.append(player3)
            self.poker.remove(player3)
            
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
            p1 = self.surf.blit(self.user_choosed_poker[0],(450,700))
            p2 = self.surf.blit(self.user_choosed_poker[1],(500,700))
            p3 = self.surf.blit(self.user_choosed_poker[2],(550,700))
            p4 = self.surf.blit(self.user_choosed_poker[3],(600,700))
            p5 = self.surf.blit(self.user_choosed_poker[4],(650,700))
            p6 = self.surf.blit(self.user_choosed_poker[5],(700,700))
            p7 = self.surf.blit(self.user_choosed_poker[6],(750,700))
            p8 = self.surf.blit(self.user_choosed_poker[7],(800,700))
            p9 = self.surf.blit(self.user_choosed_poker[8],(850,700))
            p10 = self.surf.blit(self.user_choosed_poker[9],(900,700))
            p11 = self.surf.blit(self.user_choosed_poker[10],(950,700))
            p12 = self.surf.blit(self.user_choosed_poker[11],(1000,700))
            p13 = self.surf.blit(self.user_choosed_poker[12],(1050,700))
            p14 = self.surf.blit(self.user_choosed_poker[13],(1100,700))
            p15 = self.surf.blit(self.user_choosed_poker[14],(1150,700))
            p16 = self.surf.blit(self.user_choosed_poker[15],(1200,700))
            p17 = self.surf.blit(self.user_choosed_poker[16],(1250,700))

    def check_card_choose():
        None