import bgdata
import random
import os
import button

poker_image_path = r'PNG-cards-1.3'
imgs = os.listdir(poker_image_path)
poker = []
choosed_dizhu_poker = []
choosed_poker01 = []
choosed_poker02 = []
choosed_poker03 = []
round = 0

class Game_algorithm():
    def __init__(self,screen):
        self.surf = screen
        for p in imgs:
            poker.append(p)
        print(poker)
        for a in range(3):
            dizhupai = random.choice(poker)
            choosed_dizhu_poker.append(dizhupai)
            poker.remove(dizhupai)
        for b in range(17):
            player1 = random.choice(poker)
            choosed_poker01.append(player1)
            poker.remove(player1)
            player2 = random.choice(poker)
            choosed_poker02.append(player2)
            poker.remove(player2)
            player3 = random.choice(poker)
            choosed_poker03.append(player3)
            poker.remove(player3)

    def run(self):
        global round,poker,choosed_dizhu_poker,choosed_poker01,choosed_poker02,choosed_poker03
        if round == 0:
            pass
if __name__ == '__main__':
    Game_algorithm()
    print('====================================================')
    print(choosed_dizhu_poker)
    print('====================================================')
    print(choosed_poker01)
    print('====================================================')
    print(choosed_poker02)
    print('====================================================')
    print(choosed_poker03)
    print('====================================================')
    print(poker)
    print('=======================end==========================')
