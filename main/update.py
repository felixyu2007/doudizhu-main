from menu_page import *

class Refresh_system():
    def __init__(self,surf):
        self.surf = surf
        self.round = 0
        self.movement_position = [900,200]
        self.sended = False
        self.userinfo_size = pygame.font.Font(None,80)
        self.ans = function_data.signin_and_login_system.get_userinfo()
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)

    def draw_refreshed(self):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))

    def draw_moving_card(self,startpoint=(int,int),endpoint=(int,int))->list:
        if startpoint[0] <= endpoint[0]:
            x_move_distance = endpoint[0]//startpoint[0]
            print(x_move_distance)
        elif endpoint[0] <= startpoint[0]:
            x_move_distance = startpoint[0]//endpoint[0]
            print(x_move_distance)
        if startpoint[1] <= endpoint[1]:
            y_move_distance = endpoint[1]//startpoint[1]
            print(y_move_distance)
        elif endpoint[1] <= startpoint[1]:
            y_move_distance = startpoint[1]//endpoint[1]
            print(y_move_distance)
        return x_move_distance,y_move_distance
