from data import *
#define a method button

class Button():
    def __init__(self,coordinatex,coordinatey,text: str,command: bool):
        self.command = command
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.button_rect = pygame.Rect(coordinatex,coordinatey,300,30)
        self.button_text_size = pygame.font.Font(None,28)
        self.button_text = self.button_text_size.render(text,True,black)
    def button(self,event):
        pygame.draw.rect(screen,green,self.button_rect)
        screen.blit(self.button_text,(self.coordinatex,self.coordinatey))
        if self.button_rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
        