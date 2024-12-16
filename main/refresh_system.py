from menu_page import *
class Refresh_system():
    def __init__(self,surf,userinfo,money):
        self.surf = surf
        self.userinfo = userinfo
        self.money = money
        self.round = 0
        self.movement_position = [900,200]
        self.sended = False
    def draw_refreshed(self):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
    def draw_moving_card(self):
        global keep_show
        if self.round <= 13 and self.sended == False:
            self.surf.blit(cardback,(900,200))
            self.surf.blit(cardback,self.movement_position)
            self.movement_position[0] += 8
            self.movement_position[1] += 16
            if self.movement_position[0] == 1100 or self.movement_position[1] == 600:
                keep_show.append('i')
                self.movement_position[0] = 900
                self.movement_position[1] = 200
                self.round += 1
            if self.round >= 1:
                self.surf.blit(cardback,(1100,600))
        

    def refresh(self,round):
        if round == 0:
            for i in range(0,54):
                choosed_poker = random.choice(poker_data)
                if choosed_poker not in choosed_poker_data:
                    choosed_poker_data.append(choosed_poker)
                else:
                    pass
                return choosed_poker_data
        else:
            pass