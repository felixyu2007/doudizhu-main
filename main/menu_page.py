#import cache and refresh_system
import function_data.button
import function_data.inputbox
from data import *
import function_data.signin_and_login_system
class Sign_page():
    def __init__(self,surf,signed,login_mode):
        #设定渲染文字的字形与内容
        self.titletext1 = pygame.font.Font(None,140)
        self.titletext2 = pygame.font.Font(None,140)
        self.textsize2 = pygame.font.Font(None,60)
        self.title = self.titletext1.render('Fighting The Landlord',True,red)
        self.bgtitle = self.titletext2.render('Fighting The Landlord',True,black)
        self.starttitle = self.textsize2.render('start',True,black)
        self.signed = signed
        self.surf = surf
        self.login_mode = login_mode
        self.getinbtn = function_data.button.Button(self.surf,1200,550,'get in!')
        self.name = function_data.inputbox.Intput_box(self.surf,600,500,'name')
        self.password = function_data.inputbox.Intput_box(self.surf,600,600,'password')

    def sign_page(self,event,mouseevent):
        global getin
        if self.signed == True and self.login_mode == False: 
            self.surf.fill(black)
            pygame.draw.rect(self.surf,orange,points[15])
            pygame.draw.polygon(self.surf,orange2,draw_points1,0)
            pygame.draw.polygon(self.surf,red2,draw_points2,0)
            pygame.draw.polygon(self.surf,orange2,draw_points3,0)
            pygame.draw.polygon(self.surf,red2,draw_points4,0)
            pygame.draw.polygon(self.surf,orange2,draw_points5,0)
            pygame.draw.polygon(self.surf,green2,draw_points6,0)
            pygame.draw.polygon(self.surf,white2,draw_points7,0)
            pygame.draw.circle(self.surf,black,points[2],150)
            pygame.draw.circle(self.surf,black,points[3],150)
            pygame.draw.rect(self.surf,black,points[4])
            pygame.draw.circle(self.surf,green,points[5],130)
            pygame.draw.circle(self.surf,green,points[6],130)
            pygame.draw.rect(self.surf,green,points[7])
            self.surf.blit(self.bgtitle,points[1])
            self.surf.blit(self.title,points[0])

            self.name.draw()
            self.password.draw()
            aname = self.name.interact(event)
            apassword = self.password.interact(event)

            getinbutton = self.getinbtn.clickbutton(mouseevent,event)
            if aname != '' and apassword != '':
                if getinbutton == True and getinbutton not in disable_button:
                    disable_button.append(getinbutton)
                    function_data.signin_and_login_system.sign_up(aname,apassword)
                    print(disable_button)
                    getin = True
                    return getin
        if self.signed == True and self.login_mode == True:
            self.surf.fill(black)
            pygame.draw.rect(self.surf,orange,points[15])
            pygame.draw.polygon(self.surf,orange2,draw_points1,0)
            pygame.draw.polygon(self.surf,red2,draw_points2,0)
            pygame.draw.polygon(self.surf,orange2,draw_points3,0)
            pygame.draw.polygon(self.surf,red2,draw_points4,0)
            pygame.draw.polygon(self.surf,orange2,draw_points5,0)
            pygame.draw.polygon(self.surf,green2,draw_points6,0)
            pygame.draw.polygon(self.surf,white2,draw_points7,0)
            pygame.draw.circle(self.surf,black,points[2],150)
            pygame.draw.circle(self.surf,black,points[3],150)
            pygame.draw.rect(self.surf,black,points[4])
            pygame.draw.circle(self.surf,green,points[5],130)
            pygame.draw.circle(self.surf,green,points[6],130)
            pygame.draw.rect(self.surf,green,points[7])
            self.surf.blit(self.bgtitle,points[1])
            self.surf.blit(self.title,points[0])

            self.name.draw()
            self.password.draw()
            name = self.name.interact(event)
            password = self.password.interact(event)

            getinbutton = self.getinbtn.clickbutton(mouseevent,event)
            if name != '' and password != '':
                if getinbutton == True and getinbutton not in disable_button:
                    ans = function_data.signin_and_login_system.login(name,password)
                    if ans == True:
                        disable_button.append(getinbutton)
                        print(disable_button)
                        return getinbutton
                    else:
                        return False
                    
        elif self.signed == False:
            self.surf.fill(orange)
            self.surf.blit(button_image07,points[13])
            self.surf.blit(button_image08,points[14])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                    self.signed = True
                    self.login_mode = True
                if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                    self.signed = True

class Menu():
    def __init__(self,surf):
        self.rule_rect = pygame.Rect(800,440,320,100)
        self.start_rect = pygame.Rect(800,640,320,100)
        self.rule_slogan_size = pygame.font.Font(None,120)
        self.userinfo_size = pygame.font.Font(None,80)
        self.surf = surf
        self.ans = function_data.signin_and_login_system.get_userinfo()
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)
        self.rule_slogan = self.rule_slogan_size.render('RULE',True,black)

    def draw_menu(self,event):
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        pygame.draw.rect(self.surf,green,self.rule_rect)
        pygame.draw.rect(self.surf,green,self.start_rect)
        self.surf.blit(self.rule_slogan,(850,445))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rule_rect.collidepoint(event.pos):
                self.surf.blit(button_image09,(700,350))
            if self.start_rect.collidepoint(event.pos):
                return True
        return False