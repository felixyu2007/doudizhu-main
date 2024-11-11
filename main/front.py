#引入和创建必要的函数和文件路径
from running_data import *
#背景颜色
orange = (204,115,63)
green = (49,174,91)
red = (219,81,81)
black = (74,74,74)
#背景图片与图形渲染的固定位置
points = [(420,200),(425,205),(400,240),(1520,240),(400,90,1100,300)
          ,(400,239),(1520,239),(410,110,1100,260),(600,500,300,30)
          ,(600,600,300,30),(600,480),(600,580),(1100,480),(900,100)
          ,(100,100),(50,50,1820,980)]
#背景图片与图形渲染的可活动位置
movingpoint1 = [0,0,1920,1080]
#设定渲染文字的字形与内容
titletext1 = pygame.font.Font(None,140)
titletext2 = pygame.font.Font(None,140)
textsize1 = pygame.font.Font(None,35)
title = titletext1.render('Fighting The Landlord',True,red)
bgtitle = titletext2.render('Fighting The Landlord',True,black)
nametext = textsize1.render('NAME',True,black)
passwordtext = textsize1.render('PASSWORD',True,black)

usertextname = ''
usertextpassword = ''
#登入界面输入位置
rect1 = pygame.Rect(600,500,300,30)
rect2 = pygame.Rect(600,600,300,30)
#是否已互动预设
running = True
signed = False
interact1 = False
interact2 = False
#以下是登入部分的主要程序
class Signin_and_login_system():      
    def save_system(name,password):
        opw = os.open('txt_data\player_data',os.O_RDWR)
        os.write(opw,name)
        os.write(opw,password)
        os.close(opw)
        Main.ask_quetion('login?','go to login?')

    def sign_up(usertextname,usertextpassword):
        usn = os.fsencode(usertextname)
        usp = os.fsencode(usertextpassword)
        Signin_and_login_system.save_system(usn,usp)     

    def log_in():
        pass

#以下使用pygame module去渲染登入界面
while running == True:
    for event in pygame.event.get():#这句程序是用来获取你的行为的
        #通过下面这一句程序实现离开方法
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            Main.ask_quetion('quit','wuld you want to quit the game')
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
            
