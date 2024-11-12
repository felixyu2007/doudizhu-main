#import cache
from cache import *
difficult_choosed = False
difficult_rect1 = (550,600,50,20)
difficult_rect2 = (1050,600,50,20)
difficult_rect3 = (1550,600,50,20)
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
        global signed,interact1,interact2,usertextname,usertextpassword
        #the main part of the game,it is a cycle to refresh the graphic interface
        while running == True:
            for event in pygame.event.get():#这句程序是用来获取你的行为的
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main.ask_quetion('quit','wuld you want to quit the game?')
                if ined == False:
                    if signed == True:  
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if rect1.collidepoint(event.pos):
                                interact1 = True
                            else:
                                interact1 = False
                            if rect2.collidepoint(event.pos):
                                interact2 = True
                            else:
                                interact2 = False
                            if usertextname != '' and usertextpassword != '':
                                if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217:
                                    Main.sign_up(usertextname,usertextpassword)
                                else:
                                    pass

                        if event.type == pygame.KEYDOWN:
                            if interact1 == True:
                                if len(usertextname) > 30:
                                    usertextname = usertextname[:-1]
                                if event.key == pygame.K_BACKSPACE:
                                    usertextname = usertextname[:-1]
                                else:
                                    usertextname += event.unicode

                            if interact2 == True:
                                if len(usertextpassword) > 30:
                                    usertextpassword = usertextpassword[:-1]
                                if event.key == pygame.K_BACKSPACE:
                                    usertextpassword = usertextpassword[:-1]
                                else:
                                    usertextpassword += event.unicode
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
                        rect1.w=max(100,userinputname.get_width() + 5)
                        rect2.w=max(100,userinputpassword.get_width() + 5)
                        screen.blit(cardback,points[12])
                    elif signed == False:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                                signed = True
                                Main.login()
                            if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                                signed = True
                        screen.fill(orange)
                        screen.blit(button_image07,points[13])
                        screen.blit(button_image08,points[14])
                else:
                    if difficult_choosed == False:
                        screen.fill(green)
                        pygame.draw.rect(screen,black,difficult_rect1)
                        pygame.draw.rect(screen,black,difficult_rect2)
                        pygame.draw.rect(screen,black,difficult_rect3)

            pygame.display.update()


