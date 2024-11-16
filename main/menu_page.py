from sign_page import * 

class Menu():
    def __init__(self,userinfomation,money):
        self.userinfo_rect = pygame.Rect(10,10,300,100)
        
    def draw_menu(self,surf):
        surf.blit(background_image,(0,0))
        pygame.draw.rect(surf,black,(0,0,1920,200))
         
