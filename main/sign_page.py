#import cache and refresh_system
from button import *
from inputbox import *
class Sign_page():
    def __init__(self):
        pygame.display.set_caption('歡樂鬥地主')
    global signed,difficult_rect1,ined
    global difficult_rect2,difficult_rect3,start_rect,menu_rect,round,started
    user_input_name = Intput_box(screen,600,500,'name')
    user_input_password = Intput_box(screen,600,600,'password')
    def sign_page(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                ask_quetion('quit','do you want to quit the game?')
            if ined == False:
                if signed == True: 
                    screen.fill(black)
                    pygame.draw.rect(screen,orange,points[15])
                    pygame.draw.circle(screen,black,points[2],150)
                    pygame.draw.circle(screen,black,points[3],150)
                    pygame.draw.rect(screen,black,points[4])
                    pygame.draw.circle(screen,green,points[5],130)
                    pygame.draw.circle(screen,green,points[6],130)
                    pygame.draw.rect(screen,green,points[7])
                    screen.blit(bgtitle,points[1])
                    screen.blit(title,points[0])
                    screen.blit(cardback,points[12]) 
                    user_input_name.draw()
                    user_input_password.draw()
                    name = user_input_name.interact(event)
                    password = user_input_password.interact(event)
                    #登入条件
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217 and len(name and password) != 0:
                            sign_up(name,password)
                            ined == True
                        else:
                            pass
                elif signed == False:
                    screen.fill(orange)
                    screen.blit(button_image07,points[13])
                    screen.blit(button_image08,points[14])
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                            signed = True
                            login()
                        if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                            signed = True
        clock.tick(FPS)
        pygame.display.update()
