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
        self.increase_btn = Button(self.surf,1200,550,'increase')
        self.decrease_btn = Button(self.surf,1200,750,'decrease')

        for p in imgs:
            self.poker.append(p)
        print(self.poker)
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
            self.increase_btn.clickbutton(mouseevent,event)
            self.decrease_btn.clickbutton(mouseevent,event)

