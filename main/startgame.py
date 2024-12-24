from refresh_system import *
import pygame
import function_data.bgdata

clock = pygame.time.Clock()
clock.tick(FPS)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')

sp = Sign_page(screen,signed,login_mode)
m = Menu(screen)
rs = Refresh_system(screen)

start_coordinate = [900,200]
end_coordinate = [1100,600]
last_coordinate = [0,0]
distance = rs.draw_moving_card(start_coordinate,end_coordinate)

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
                if start_coordinate[0] <= end_coordinate[0] or start_coordinate[1] <= end_coordinate[1]:
                    start_coordinate[0] += distance[0]*2
                    start_coordinate[1] += distance[1]*2
                    screen.blit(cardback,(start_coordinate[0],start_coordinate[1]))
                else:
                    keep_show.append('i')
                    last_coordinate[0] = start_coordinate[0]
                    last_coordinate[1] = start_coordinate[1]
                    start_coordinate = [900,200]
                    end_coordinate = [1100,600]
                    round += 1
                if round != 0:
                    screen.blit(cardback,(last_coordinate[0],last_coordinate[1]))
                
    pygame.display.flip()
    

