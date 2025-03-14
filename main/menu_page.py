#import cache and refresh_system
from bgdata import *
from button import *
from inputbox import *
from signin_and_login_system import *
from data import *

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
        self.del_account_mode = False
        self.userid = ''
        self.sign = Signin_and_login_method()
        self.getinbtn = Button(self.surf,1200,650,'Enter',green)
        self.signinbtn = Button(self.surf,400,700,'sign in',orange2)
        self.loginbtn = Button(self.surf,800,700,'log in',orange2)
        self.delaccbtn = Button(self.surf,1200,700,'del account',orange2)
        self.user_id = Intput_box(self.surf,600,500,'user id (must be integer and 8 letters)')
        self.name = Intput_box(self.surf,600,600,'name (must be longer than 7 letters)')
        self.password = Intput_box(self.surf,600,700,'password (must be longer than 7 letters)')
        self.del_account = Intput_box(self.surf,600,400,'Enter the account id you want to delete')
        self.back = Button(self.surf,1200,500,'back',orange2)

    def sign_page(self,event,mouseevent):
        global getin

        if self.signed == False and self.del_account_mode == True:
            self.surf.fill(black)
            pygame.draw.rect(self.surf,orange,points[15])
            pygame.draw.polygon(self.surf,orange2,draw_points1,0)
            pygame.draw.polygon(self.surf,red2,draw_points2,0)
            pygame.draw.polygon(self.surf,orange2,draw_points3,0)
            pygame.draw.polygon(self.surf,red2,draw_points4,0)
            pygame.draw.polygon(self.surf,orange2,draw_points5,0)

            self.del_account.draw()
            self.userid = self.del_account.interact(event)
            ans2 = self.back.clickbutton(mouseevent,event)
            getinbutton = self.getinbtn.clickbutton(mouseevent,event)
            if self.userid != '' and len(self.userid) == 8 and getinbutton == True:
                ans = self.sign.delete_account(self.userid)
                if ans:
                    ask_quetion('sign_error','account deleted')
                    self.del_account_mode == False
                else:pass
            if ans2 == True:
                self.signed = False
                self.del_account_mode = False
            else:pass

        elif self.signed == True and self.login_mode == True: 
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
            self.user_id.draw()
            self.userid = self.user_id.interact(event)
            name = self.name.interact(event)
            password = self.password.interact(event)
            ans2 = self.back.clickbutton(mouseevent,event)
            getinbutton = self.getinbtn.clickbutton(mouseevent,event)
            if (self.userid != '' and name != '' and password != '') and (len(self.userid) == 8 and len(name) >= 8 and len(password) >= 8):
                if getinbutton == True:
                    ans = self.sign.login(self.userid,name,password)
                    return ans
            if ans2 == True:
                self.signed = False
                self.del_account_mode = False
            else:pass
        elif self.signed == True and self.login_mode == False:
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
            self.user_id.draw()
            self.userid = self.user_id.interact(event)
            name = self.name.interact(event)
            password = self.password.interact(event)
            ans2 = self.back.clickbutton(mouseevent,event)
            getinbutton = self.getinbtn.clickbutton(mouseevent,event)
            if (self.userid != '' and name != '' and password != '') and (len(self.userid) == 8 and len(name) >= 8 and len(password) >= 8):
                if getinbutton == True:
                    self.sign.create_account(self.userid,name,password)
                    self.signed = False
                    self.login_mode = False
                    self.del_account_mode = False
            if ans2 == True:
                self.signed = False
                self.del_account_mode = False
            else:pass
        if self.signed == False and self.del_account_mode == False:
            self.surf.fill(black)
            pygame.draw.rect(self.surf,orange,points[15])
            pygame.draw.polygon(self.surf,orange2,draw_points1,0)
            pygame.draw.polygon(self.surf,red2,draw_points2,0)
            pygame.draw.polygon(self.surf,orange2,draw_points3,0)
            pygame.draw.polygon(self.surf,red2,draw_points4,0)
            pygame.draw.polygon(self.surf,orange2,draw_points5,0)

            a = self.signinbtn.clickbutton(mouseevent,event)
            b = self.loginbtn.clickbutton(mouseevent,event)
            c = self.delaccbtn.clickbutton(mouseevent,event)
            if a:
                self.signed = True
            elif b:
                self.signed = True
                self.login_mode = True
            elif c:
                self.signed = False
                self.del_account_mode = True

    def sendback(self):
        return self.userid

class Menu():
    def __init__(self,surf):
        self.rule_rect = pygame.Rect(800,440,320,100)
        self.start_rect = pygame.Rect(800,640,320,100)
        self.rule_slogan_size = pygame.font.Font(None,120)
        self.userinfo_size = pygame.font.Font(None,80)
        self.surf = surf
        self.rule_slogan = self.rule_slogan_size.render('RULE',True,black)
        self.start_slogan = self.rule_slogan_size.render('START',True,black)
        self.sign = Signin_and_login_method()
    def draw_menu(self,event,target):
        self.target = target
        self.ans = self.sign.get_userinfo(self.target)
        self.name = self.userinfo_size.render(self.ans[0],True,black)
        self.fund = self.userinfo_size.render(str(self.ans[1]),True,green)
        self.surf.blit(background_image,(0,0))
        pygame.draw.rect(self.surf,black,(0,0,1920,100))
        pygame.draw.rect(self.surf,orange,(10,10,300,80))
        pygame.draw.rect(self.surf,green,self.rule_rect)
        pygame.draw.rect(self.surf,green,self.start_rect)
        self.surf.blit(self.rule_slogan,(850,450))
        self.surf.blit(self.name,(20,20))
        self.surf.blit(self.fund,(1600,20))
        self.surf.blit(self.start_slogan,(830,650))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rule_rect.collidepoint(event.pos):
                self.surf.blit(button_image09,(700,350))
            if self.start_rect.collidepoint(event.pos):
                return True
        return False