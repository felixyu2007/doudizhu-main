import function_data.bgdata as bgdata
#define a method button
class Button():
    def __init__(self,surf,coordinatex,coordinatey,text: str):
        self.coordinatex = coordinatex
        self.coordinatey = coordinatey
        self.surf = surf
        self.button_rect1 = bgdata.pygame.Rect(coordinatex,coordinatey,200,50)
        self.button_rect2 = bgdata.pygame.Rect(coordinatex-5,coordinatey-4,210,60)
        self.button_text_size = bgdata.pygame.font.Font(None,50)
        self.button_text = self.button_text_size.render(text,True,(74,74,74))
        
    def clickbutton(self,mouseevent,event):
        bgdata.pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
        bgdata.pygame.draw.rect(self.surf,(49,174,91),self.button_rect1)
        self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
        if self.button_rect2.collidepoint(mouseevent):
            if event.type == bgdata.pygame.MOUSEBUTTONDOWN:
                bgdata.pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
                bgdata.pygame.draw.rect(self.surf,(37,96,57),self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
            if event.type == bgdata.pygame.MOUSEBUTTONUP:
                bgdata.pygame.draw.rect(self.surf,(74,74,74),self.button_rect2)
                bgdata.pygame.draw.rect(self.surf,(49,174,91),self.button_rect1)
                self.surf.blit(self.button_text,(self.coordinatex,self.coordinatey))
                return True
        