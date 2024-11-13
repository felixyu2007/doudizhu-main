#import cache and refresh_system
from refresh_system import *
from button import *
from signin_and_login_system import *
#quit or other method function messagebox
class Main():
    pygame.display.set_caption('歡樂鬥地主')
    def game_main():
        global signed,interact1,interact2,usertextname,usertextpassword,difficult_choosed,difficult_rect1
        global difficult_rect2,difficult_rect3,rect1,rect2,start_rect,menu_rect,round,started
        #the main part of the game,it is a cycle to refresh the graphic interface
        while running == True:
            for event in pygame.event.get():#这句程序是用来获取你的行为的
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ask_quetion('quit','wuld you want to quit the game?')
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
                        screen.blit(nametext,points[10])
                        screen.blit(passwordtext,points[11])
                        pygame.draw.rect(screen,black,rect1,2)
                        pygame.draw.rect(screen,black,rect2,2)
                        
                        screen.blit(cardback,points[12]) 
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 600 < pygame.mouse.get_pos()[0] < 1200 and 500 < pygame.mouse.get_pos()[1] < 530:
                                interact1 = True
                                interact2 = False
                                
                            if 600 < pygame.mouse.get_pos()[0] < 1200 and 600 < pygame.mouse.get_pos()[1] < 630:
                                interact2 = True
                                interact1 = False
                            
                            if usertextname != '' and usertextpassword != '':
                                if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217:
                                    sign_up(usertextname,usertextpassword)
                                else:
                                    pass
                        
                        if event.type == pygame.KEYDOWN:
                            if interact1 == True:
                                if len(usertextname) > 30:
                                    usertextname = usertextname[:-1]
                                elif event.key == pygame.K_BACKSPACE:
                                    usertextname = usertextname[:-1]
                                else:
                                    usertextname += event.unicode

                            if interact2 == True:
                                if len(usertextpassword) > 30:
                                    usertextpassword = usertextpassword[:-1]
                                elif event.key == pygame.K_BACKSPACE:
                                    usertextpassword = usertextpassword[:-1]
                                else:
                                    usertextpassword += event.unicode
                        
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
                        
                else:
                    if difficult_choosed == False:
                        screen.fill(green)
                        pygame.draw.rect(screen,black,difficult_rect1)
                        pygame.draw.rect(screen,black,difficult_rect2)
                        pygame.draw.rect(screen,black,difficult_rect3)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 550 < pygame.mouse.get_pos()[0] < 650 and 600 < pygame.mouse.get_pos()[1] < 640:
                                difficult_choosed = True
                            if 1050 < pygame.mouse.get_pos()[0] < 1150 and 600 < pygame.mouse.get_pos()[1] < 640:
                                difficult_choosed = True
                            if 1550 < pygame.mouse.get_pos()[0] < 1650 and 600 < pygame.mouse.get_pos()[1] < 640:
                                difficult_choosed = True
                    else:
                        #
                        while menu_rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) and menu_rect.w < 400:
                            menu_rect.w += 1
                        else:
                            pass
                        while not(menu_rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])) and menu_rect.w > 100:
                            menu_rect.w -= 1
                        else:
                            pass
                        #
                        if started == False:
                            button(1050,800,text='start')
                            if command == True:
                                started == True
                        else:
                            screen.fill(black)
            pygame.display.update()


