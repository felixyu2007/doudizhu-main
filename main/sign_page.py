#import cache and refresh_system
from button import *
from inputbox import *
class Sign_page():
    def __init__(self,surf,signed,started):
        self.surf = surf
        self.signed = signed
        self.started = started
        self.name = Intput_box(screen,600,500,'name')
        self.password = Intput_box(screen,600,600,'password')
    def sign_page(self,event):
        if self.signed == True: 
            self.surf.fill(black)
            pygame.draw.rect(screen,orange,points[15])
            pygame.draw.circle(screen,black,points[2],150)
            pygame.draw.circle(screen,black,points[3],150)
            pygame.draw.rect(screen,black,points[4])
            pygame.draw.circle(screen,green,points[5],130)
            pygame.draw.circle(screen,green,points[6],130)
            pygame.draw.rect(screen,green,points[7])
            self.surf.blit(bgtitle,points[1])
            self.surf.blit(title,points[0])
            self.surf.blit(cardback,points[12]) 
            self.name.draw()
            self.password.draw()
            self.name.interact
            self.password.interact
        elif self.signed == False:
            self.surf.fill(orange)
            self.surf.blit(button_image07,points[13])
            self.surf.blit(button_image08,points[14])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                    self.signed = True
                    login()
                if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                    self.signed = True
