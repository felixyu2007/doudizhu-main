from data import *
#define a method button

class Button():
    def __init__(self,surf,coordinatex,coordinatey,text: str):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.surf = surf
        self.button_rect1 = pygame.Rect(coordinatex,coordinatey,200,50)
        self.button_rect2 = pygame.Rect(coordinatex-5,coordinatey-4,210,60)
        self.button_text_size = pygame.font.Font(None,50)
        self.button_text = self.button_text_size.render(text,True,black)
    def drawbutton(self):
        pygame.draw.rect(screen,black,self.button_rect2)
        pygame.draw.rect(screen,green,self.button_rect1)
        self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
    def clickbutton(self,mouseevent,event):
        if self.button_rect2.collidepoint(mouseevent):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen,black,self.button_rect2)
                pygame.draw.rect(screen,dark_green,self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(screen,black,self.button_rect2)
                pygame.draw.rect(screen,green,self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
                return True
        