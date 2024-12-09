from menu_page import *
class Refresh_system():
    def __init__(self,surf,userinfo,money,round):
        self.surf = surf
        self.userinfo = userinfo
        self.money = money
        self.round = 0
        self.movement_position = (900,200)
    def draw_refreshed(self):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        if self.round == 0 and :
            self.surf.blit(cardback,self.movement_position)
            self.movement_position[0] += 2
            self.movement_position[1] += 1
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