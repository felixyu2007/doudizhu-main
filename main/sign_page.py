#import cache and refresh_system
from button import *
from inputbox import *
class Sign_page():
    def __init__(self,surf,signed,getin):
        self.signed = signed
        self.getin = getin
        self.surf = surf
        self.getinbtn = Button(self.surf,1200,550,'get in!')
        self.name = Intput_box(screen,600,500,'name')
        self.password = Intput_box(screen,600,600,'password')
    def sign_page(self,event,mouseevent):
        if self.signed == True: 
            self.surf.fill(black)
            pygame.draw.rect(screen,orange,points[15])
            pygame.draw.circle(screen,black,points[2],150)
            pygame.draw.circle(screen,black,points[3],150)
            pygame.draw.rect(screen,black,points[4])
            pygame.draw.circle(screen,green,points[5],130)
            pygame.draw.circle(screen,green,points[6],130)
            pygame.draw.rect(screen,green,points[7])
            self.surf.blit(bgtitle,points[1])
            self.surf.blit(title,points[0])

            self.name.draw()
            self.password.draw()
            self.name.interact(event)
            self.password.interact(event)
            self.getinbtn.drawbutton()
            self.getinbtn.clickbutton(mouseevent,event)
            if self.getinbtn.clickbutton(mouseevent,event) == True:
                print('1')
                self.getin = True
                return self.getin

            
        elif self.signed == False:
            self.surf.fill(orange)
            self.surf.blit(button_image07,points[13])
            self.surf.blit(button_image08,points[14])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < pygame.mouse.get_pos()[0] < 796 and 100 < pygame.mouse.get_pos()[1] < 455:
                    self.signed = True
                    login()
                if 900 < pygame.mouse.get_pos()[0] < 1596 and 100 < pygame.mouse.get_pos()[1] < 495:
                    self.signed = True


# class Button:
#     '''draw a button in a Surface'''
#     def __init__(self,
#                  text:str,
#                  rect:pygame.Rect,
#                  color:tuple = BUTTON_COLOR,
#                  touch_color:tuple = BUTTON_TOUCH_COLOR,
#                  flag  = 0):
#         """flag is button function,setting == -1 betting == 0,bet setting == 1"""
#         self.text  = text
#         self.rect  = rect
#         self.color = color
#         self.touch = touch_color
#         self.flag  = flag

#     def adjust_value(self,value):
#         # increase /decrese
#         if   self.text == kw.INCREASE: return  value
#         elif self.text == kw.DECREASE: return -value

#     def check(self, event:pygame.event):
#         """return True when the button release"""
#         # reset color in every loop
#         self.color = BUTTON_COLOR
#         self.touch = BUTTON_TOUCH_COLOR
#         if self.rect.collidepoint(pygame.mouse.get_pos()):
#             self.touch = BUTTON_ACTIVE_TOUCH_COLOR
#             # press
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 self.color = BUTTON_ACTIVE_COLOR
#             # release
#             elif event.type == pygame.MOUSEBUTTONUP:
#                 self.color = BUTTON_COLOR
#                 self.touch = BUTTON_TOUCH_COLOR
#                 return True
#         return False

#     def draw(self, invalid:bool,value = None):
#         """draw the button\n
#            value will render above the button text"""
#         pygame.draw.rect(screen,self.color, self.rect,0,25)
#         pygame.draw.rect(screen,self.touch, self.rect,10,25)
#         pygame.draw.rect(screen,self.color, self.rect,5,25)
#         text = BUTTON_FONT.render(self.text,True,BUTTON_FONT_COLOR)
#         screen.blit(text,((self.rect.x + self.rect.width/2) - text.get_width()/2,(self.rect.y + self.rect.height/2) - text.get_height()/2))
#         if value:
#             value = BETTING_SIZE_FONT.render(str(value),True,BUTTON_FONT_COLOR)
#             screen.blit(value,(self.rect.x + (self.rect.width - value.get_width())/2,(self.rect.y + self.rect.height/2) - text.get_height() - 5))
#         if invalid:
#             invalid_layer = pygame.Surface((self.rect.width,self.rect.height),pygame.SRCALPHA)
#             pygame.draw.rect(invalid_layer,(0,0,0,128),invalid_layer.get_rect(),0,25)
#             screen.blit(invalid_layer,self.rect)
#         pygame.display.flip()
