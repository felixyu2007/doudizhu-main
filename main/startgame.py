from refresh_system import *
import pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')

def get_cards():
    for p in imgs:
        poker_data.append(p)

get_cards()

sp = Sign_page(screen,signed,login_mode)
m = Menu(screen)
rs = Refresh_system(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ask_quetion('quit','do you want to quit right now?')
        if started == False:
            if getin == False:
                ans = sp.sign_page(event,pygame.mouse.get_pos())
            if ans == True or getin == True:
                getin = True
                started = m.draw_menu(event)
        else:
            if card_sended == False:
                rs.draw_refreshed()
                rs.draw_moving_card()
                round += 1
    pygame.display.flip()
    

