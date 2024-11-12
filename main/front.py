#引入和创建必要的函数和文件路径
from cache import *
#以下是登入部分的主要程序
class Signin_and_login_system():      
    def save_system(name,password):
        opw = os.open('txt_data\player_data',os.O_RDWR)
        os.write(opw,name)
        os.write(opw,password)
        os.close(opw)
        
    def sign_up(usertextname,usertextpassword):
        usn = os.fsencode(usertextname)
        usp = os.fsencode(usertextpassword)
        Signin_and_login_system.save_system(usn,usp)     

    def log_in():
        pass

    #以下使用pygame module去渲染登入界面
    def signup_system():
        for event in pygame.event.get():
            #如果已登入signed=true，反之=false
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
                            Signin_and_login_system.sign_up(usertextname,usertextpassword)
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
                                        #以下是渲染部分
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
                pygame.display.update()
                clock.tick(FPS)
            elif signed == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                        signed = True
                        Signin_and_login_system.log_in()
                    if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                        signed = True
                #以下是渲染部分
                screen.fill(orange)
                screen.blit(button_image07,points[13])
                screen.blit(button_image08,points[14])
                pygame.display.update()
                clock.tick(FPS)

