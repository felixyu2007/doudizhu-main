#import cache
from cache import *

#quit or other method function messagebox
class Main():
    def ask_quetion(input_title,input_message):
        global ined
        ans = messagebox.askquestion(title=input_title,message=input_message)
        if ans == 'yes' and input_title == 'quit':
            pygame.quit()
            quit()
        if ans == 'yes' and input_title == 'login?':
            ined = True
    def get_cards():
        for p in imgs:
            poker_data.append(p)

    def save_system(name,password):
        opw = os.open('txt_data\player_data',os.O_RDWR)
        os.write(opw,name)
        os.write(opw,password)
        os.close(opw)
        Main.ask_quetion('login?','do you want to login now?')
    def sign_up(usertextname,usertextpassword):
        usn = os.fsencode(usertextname)
        usp = os.fsencode(usertextpassword)
        Main.save_system(usn,usp)     
        
    def login():
        pass

    pygame.display.set_caption('歡樂鬥地主')
    def game_main():
        global signed,interact1,interact2,usertextname,usertextpassword,difficult_choosed,difficult_rect1,difficult_rect2,difficult_rect3,rect1,rect2,start_rect
        #the main part of the game,it is a cycle to refresh the graphic interface
        while running == True:
            for event in pygame.event.get():#这句程序是用来获取你的行为的
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main.ask_quetion('quit','wuld you want to quit the game?')
                if ined == False:
                    if signed == True: 
                        screen.fill(black)
                        pygame.draw.rect(screen,orange,points[15])
                        userinputname = textsize1.render(usertextname,True,black)
                        userinputpassword = textsize1.render(usertextpassword,True,black)
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
                        screen.blit(userinputname,points[8])
                        screen.blit(userinputpassword,points[9])
                        screen.blit(cardback,points[12]) 

                        
                        if 600 < pygame.mouse.get_pos()[0] < 1200 and 500 < pygame.mouse.get_pos()[1] < 530:
                            interact1 = True
                            interact2 = False
                            
                        if 600 < pygame.mouse.get_pos()[0] < 1200 and 600 < pygame.mouse.get_pos()[1] < 630:
                            interact2 = True
                            interact1 = False
                            
                        if usertextname != '' and usertextpassword != '':
                            if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217:
                                Main.sign_up(usertextname,usertextpassword)
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
                                Main.login()
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
                        pass
                        # screen.blit(background_image,(0,0))
                        # pygame.draw.rect(screen,green,start_rect)
            pygame.display.update()


