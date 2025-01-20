from menu_page import *
from algorithm import *

class Refresh_system():
    def __init__(self,surf):
        self.sign = Signin_and_login_method()
        self.surf = surf
        self.ga = Game_algorithm(self.surf)
        self.count = 0
        self.movement_position = [900,200]
        self.sended = False
        self.userinfo_size = pygame.font.Font(None,80)
        self.ai_info_size =  pygame.font.Font(None,40)
        self.sign = Signin_and_login_method()
        self.distance = [1,3]
        self.start_coordinate = [900,200]
        self.end_coordinate = [1100,600]
        self.last_coordinate = [0,0]
        self.keep_show = ['','','','','','','','','','','','','','','','','']
        self.card_sended = False
        self.notice_size = pygame.font.Font(None,300)
        self.winpage = self.notice_size.render('YOU WIN',True,red)
        self.losepage = self.notice_size.render('YOU lose',True,red)
        self.ai_ans = self.sign.get_aiinfo()

    def draw_refreshed(self,event,mouseevent,target):
        self.target = target
        self.ans = self.sign.get_userinfo(self.target)
        self.ai_name1 = self.ai_info_size.render(self.ai_ans[0],True,white2)
        self.ai_fund1 = self.ai_info_size.render(str(self.ai_ans[1]),True,white2)
        self.ai_name2 = self.ai_info_size.render(self.ai_ans[2],True,white2)
        self.ai_fund2 = self.ai_info_size.render(str(self.ai_ans[3]),True,white2)
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,orange,(0,200,300,100))
        pygame.draw.rect(self.surf,orange,(1620,200,300,100))
        pygame.draw.rect(self.surf,black,(0,200,300,50))
        pygame.draw.rect(self.surf,black,(1620,200,300,50))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))
        self.surf.blit(self.ai_name1,(10,210))
        self.surf.blit(self.ai_fund1,(10,250))
        self.surf.blit(self.ai_name2,(1630,210))
        self.surf.blit(self.ai_fund2,(1630,250))
        
        if self.card_sended == False:
            if self.start_coordinate[0] <= self.end_coordinate[0] or self.start_coordinate[1] <= self.end_coordinate[1]:
                self.surf.blit(cardback,(900,200))
                self.start_coordinate[0] += self.distance[0]*40
                self.start_coordinate[1] += self.distance[1]*40
                self.surf.blit(cardback,(self.start_coordinate[0],self.start_coordinate[1]))
            else:
                self.surf.blit(cardback,(900,200))
                self.last_coordinate[0] = self.start_coordinate[0]
                self.last_coordinate[1] = self.start_coordinate[1]
                self.start_coordinate = [900,200]
                self.end_coordinate = [1100,600]
                print(self.keep_show)
                if self.keep_show[15] == 'i':
                    self.card_sended = True
                    print(self.card_sended)
                    print('done')
                else:
                    self.keep_show[self.count] = 'i'
                    self.count += 1
            if self.count != 0:
                self.surf.blit(cardback,(self.last_coordinate[0],self.last_coordinate[1]))
        if self.card_sended == True:
            ans = self.ga.run(event,mouseevent)
            if ans == True:
                self.surf.blit(self.winpage,(400,500))
                spended = self.ga.return_spended_money()
                self.sign.spended_fund(spended,self.target)
                self.card_sended == False
                
            elif ans == False:
                self.surf.blit(self.losepage,(400,500))
                spended = self.ga.return_spended_money()
                self.sign.spended_fund(spended,self.target)
                self.card_sended == False

            
