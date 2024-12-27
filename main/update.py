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
        self.start_coordinate = [900,200]
        self.end_coordinate = [1100,600]
        self.last_coordinate = [0,0]
        self.distance = Refresh_system.draw_moving_card(self.start_coordinate,self.end_coordinate)
        self.keep_show = []
        self.round = 0

    def draw_refreshed(self):
        if self.round == 0:
            self.surf.blit(background_image,(0,0))
            pygame.draw.rect(self.surf,black,(0,0,1920,100))
            pygame.draw.rect(self.surf,orange,(10,10,300,80))
            self.surf.blit(self.name,(20,20))
            self.surf.blit(self.fund,(1600,20))
        
            if self.start_coordinate[0] <= end_coordinate[0] or self.start_coordinate[1] <= end_coordinate[1]:
                self.surf.blit(cardback,(900,200))
                self.start_coordinate[0] += self.distance[0]*10
                self.start_coordinate[1] += self.distance[1]*10
                self.surf.blit(cardback,(self.start_coordinate[0],self.start_coordinate[1]))
            else:
                self.surf.blit(cardback,(900,200))
                self.keep_show.append('i')
                self.last_coordinate[0] = self.start_coordinate[0]
                self.last_coordinate[1] = self.start_coordinate[1]
                start_coordinate = [900,200]
                end_coordinate = [1100,600]
                round += 1
                if self.keep_show[17] == 'i':
                    quit
            if round != 0:
                self.surf.blit(cardback,(self.last_coordinate[0],self.last_coordinate[1]))

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
