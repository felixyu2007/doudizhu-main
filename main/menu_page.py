from sign_page import * 

class Menu():
    def __init__(self,surf,userinfomation,money):
        self.userinfo_rect = pygame.Rect(10,10,300,100)
        self.surf = surf
    def draw_menu(self):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,200))
         
