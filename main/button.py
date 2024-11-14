from main.data import *
#define a method button
command = False
def button(coordinatex,coordinatey,text: str):
    global command
    button_rect = pygame.Rect(coordinatex,coordinatey,300,30)
    button_text_size = pygame.font.Font(None,28)
    button_text = button_text_size.render(text,True,black)
    pygame.draw.rect(screen,green,button_rect)
    screen.blit(button_text,(coordinatex,coordinatey))
    if button_rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
        command = True
        return command