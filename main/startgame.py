from main.update import *
import function_data.bgdata

clock = pygame.time.Clock()
clock.tick(FPS)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')

sp = Sign_page(screen,signed,login_mode)
m = Menu(screen)
rs = Refresh_system(screen)
ga = function_data.bgdata.Game_algorithm()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            function_data.bgdata.ask_quetion('quit','do you want to quit right now?')
        if started == False:
            if getin == False:
                ans = sp.sign_page(event,pygame.mouse.get_pos())
            # ?????????????????????????error????????????????????????
            if ans == True or getin == True:
                getin = True
                started = m.draw_menu(event)
    if started == True:
        rs.draw_refreshed()
    pygame.display.update()
    

