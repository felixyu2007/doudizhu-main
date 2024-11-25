from sign_page import * 

class Menu():
    def __init__(self,surf,userinfomation,money):
        self.userinfo_rect = pygame.Rect(10,10,300,80)
        self.rule_rect = pygame.Rect(800,440,320,100)
        self.start_rect = pygame.Rect(800,640,320,100)
        self.rule_slogan_size = pygame.font.Font(None,120)
        self.rule_slogan = self.rule_slogan_size.render('RULE',True,black)
        self.surf = surf
    def draw_menu(self,event):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,self.userinfo_rect)
        pygame.draw.rect(self.surf,green,self.rule_rect)
        pygame.draw.rect(self.surf,green,self.start_rect)
        self.surf.blit(self.rule_slogan,(850,445))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rule_rect.collidepoint(event.pos):
                self.surf.blit(button_image09,(700,350))
            if self.start_rect.collidepoint(event.pos):
                return True

         
