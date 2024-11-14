from data import *
#define a method button

class Button():
    def __init__(self,coordinatex,coordinatey,text: str):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.button_rect1 = pygame.Rect(coordinatex,coordinatey,200,50)
        self.button_rect2 = pygame.Rect(coordinatex-5,coordinatey-4,210,60)
        self.button_text_size = pygame.font.Font(None,50)
        self.button_text = self.button_text_size.render(text,True,black)
    def drawbutton(self,surf):
        pygame.draw.rect(screen,black,self.button_rect2)
        pygame.draw.rect(screen,green,self.button_rect1)
        surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
    def clickbutton(self,event,command: bool):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect2.collidepoint(event.pos):#pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
                not command
                return command
        