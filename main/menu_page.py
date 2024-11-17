from sign_page import * 

class Menu():
    def __init__(self,surf,userinfomation,money):
        self.userinfo_rect = pygame.Rect(10,10,300,100)
        self.rule_rect = pygame.Rect(800,440,320,100)
        self.rule_slogan_size = pygame.font.Font(None,80)
        self.rule_slogan = self.rule_slogan_size.render('RULE',True,black)
        self.surf = surf
    def draw_menu(self):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,self.userinfo_rect)
        pygaem.draw.rect(self.surf,green,self.rule_rect)
        
         
