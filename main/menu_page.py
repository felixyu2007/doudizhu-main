from sign_page import * 

class Menu():
    def __init__(self,surf):
        self.rule_rect = pygame.Rect(800,440,320,100)
        self.start_rect = pygame.Rect(800,640,320,100)
        self.rule_slogan_size = pygame.font.Font(None,120)
        self.userinfo_size = pygame.font.Font(None,80)
        self.surf = surf
        self.ans = get_userinfo()
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)
        self.rule_slogan = self.rule_slogan_size.render('RULE',True,black)

    def draw_menu(self,event):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        pygame.draw.rect(self.surf,green,self.rule_rect)
        pygame.draw.rect(self.surf,green,self.start_rect)
        self.surf.blit(self.rule_slogan,(850,445))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rule_rect.collidepoint(event.pos):
                self.surf.blit(button_image09,(700,350))
            if self.start_rect.collidepoint(event.pos):
                return True
        return False
         
