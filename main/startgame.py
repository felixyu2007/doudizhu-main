print('==========================python_running_log=====================================')
from update import *
from bgdata import *

clock = pygame.time.Clock()
clock.tick(FPS)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')

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
            if ans == True:
                ans2 = sp.sendback()
                getin = True
                started = m.draw_menu(event,ans2)
    if started == True: 
        rs.draw_refreshed(event,pygame.mouse.get_pos(),ans2)
    pygame.display.flip()
    
