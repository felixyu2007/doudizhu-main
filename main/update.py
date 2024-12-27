from menu_page import *
from function_data.algorithm import *

class Refresh_system():
    def __init__(self,surf):
        self.surf = surf
        self.ga = Game_algorithm(self.surf)
        self.count = 0
        self.movement_position = [900,200]
        self.sended = False
        self.userinfo_size = pygame.font.Font(None,80)
        self.ans = function_data.signin_and_login_system.get_userinfo()
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)
        self.distance = [1,3]
        self.start_coordinate = [900,200]
        self.end_coordinate = [1100,600]
        self.last_coordinate = [0,0]
        self.keep_show = ['','','','','','','','','','','','','','','','','']
        self.count = 0
        self.round = 0
        self.card_sended = False

    def draw_refreshed(self,event,mouseevent):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))
        if self.card_sended == False:
            if self.start_coordinate[0] <= self.end_coordinate[0] or self.start_coordinate[1] <= self.end_coordinate[1]:
                self.surf.blit(cardback,(900,200))
                self.start_coordinate[0] += self.distance[0]*10
                self.start_coordinate[1] += self.distance[1]*10
                self.surf.blit(cardback,(self.start_coordinate[0],self.start_coordinate[1]))
            else:
                self.surf.blit(cardback,(900,200))
                self.last_coordinate[0] = self.start_coordinate[0]
                self.last_coordinate[1] = self.start_coordinate[1]
                self.start_coordinate = [900,200]
                self.end_coordinate = [1100,600]
                print(self.keep_show)
                if self.keep_show[16] == 'i':
                    self.card_sended = True
                    print(self.card_sended)
                    print('done')
                else:
                    self.keep_show[self.count] = 'i'
                    self.count += 1
            if self.count != 0:
                self.surf.blit(cardback,(self.last_coordinate[0],self.last_coordinate[1]))
        else:
            if self.card_sended == True:
                if self.round == 0:
                    self.ga.run(event,mouseevent)
