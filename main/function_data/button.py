import pygame
#define a method button
class Button():
    def __init__(self,surf,coordinatex,coordinatey,text: str,color=(int,int,int)):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.surf = surf
        self.color = color
        self.button_rect1 = pygame.Rect(coordinatex,coordinatey,200,50)
        self.button_rect2 = pygame.Rect(coordinatex-5,coordinatey-4,210,60)
        self.button_text_size = pygame.font.Font(None,50)
        self.button_text = self.button_text_size.render(text,True,(74,74,74))
        self.clicked = False
        
    def clickbutton(self,mouseevent,event):
        pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
        pygame.draw.rect(self.surf,self.color,self.button_rect1)
        self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
        if self.button_rect2.collidepoint(mouseevent):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
                pygame.draw.rect(self.surf,(37,96,57),self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
                self.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
                pygame.draw.rect(self.surf,self.color,self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
                if self.clicked == False:
                    return False
                else:
                    self.clicked = False
                    return True
                
        