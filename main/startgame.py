from refresh_system import *
import pygame
import function_data.bgdata

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')

sp = Sign_page(screen,signed,login_mode)
m = Menu(screen)
rs = Refresh_system(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            function_data.bgdata.ask_quetion('quit','do you want to quit right now?')
        if started == False:
            if getin == False:
                ans = sp.sign_page(event,pygame.mouse.get_pos())
            if ans == True or getin == True:
                getin = True
                started = m.draw_menu(event)
        else:
            if card_sended == False:
                rs.draw_refreshed()
                send_coordinate = (900,200)
                distance = rs.draw_moving_card(send_coordinate,(1100,600))
                send_coordinate[0] += distance[0]
                send_coordinate[1] += distance[1]
                screen.blit(cardback,send_coordinate)
                round += 1
    pygame.display.flip()
    

