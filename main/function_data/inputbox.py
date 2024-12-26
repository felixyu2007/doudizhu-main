import bgdata
import pygame
pygame.init()
pygame.font.init()
#登入界面输入位置
class Intput_box():
    def __init__(self,surf,inputbox_x_coordinate,inputbox_y_coordinate,inputbox_title: str):
        self.surf = surf
        self.inputbox_x_coordinate = inputbox_x_coordinate
        self.inputbox_y_coordinate = inputbox_y_coordinate
        self.rect1 = pygame.Rect(self.inputbox_x_coordinate,self.inputbox_y_coordinate,500,30)
        self.inputbox_title = inputbox_title
        self.input_text_data = ''
        self.focus = False
        self.cursor = False
        self.typing = False
        self.delete = False
        self.textsize1 = pygame.font.Font(None,35)
        self.input_text = self.textsize1.render(self.input_text_data,True,(74,74,74))
        self.inputbox_name = self.textsize1.render(self.inputbox_title,True,(74,74,74))
        self.input_text_last_letter_position = self.input_text.get_rect()
        self.coordinatex = self.rect1.x+5+self.input_text_last_letter_position.width

    def draw(self):
        #绘制输入框
        pygame.draw.rect(self.surf,(74,74,74),self.rect1,2)
        #渲染输入框题目
        self.surf.blit(self.inputbox_name,(self.inputbox_x_coordinate,self.inputbox_y_coordinate-30))
        #渲染输入了的文字
        self.surf.blit(self.input_text,(self.inputbox_x_coordinate + 5,self.inputbox_y_coordinate + 5))

    def interact(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect1.collidepoint(pygame.mouse.get_pos()):
                self.focus = True
            else:
                self.focus = False
        else:
            pass
        if self.focus == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.delete = True
                else:
                    self.input_text_data += event.unicode

        if self.focus == True:
            self.cursor = not self.cursor
        if self.focus == True and self.cursor == True:
            pygame.draw.line(self.surf,(74,74,74),(self.coordinatex,self.inputbox_y_coordinate+5),(self.coordinatex,self.inputbox_y_coordinate+25),2)
        
        #删除方法
        if self.delete == True and self.input_text_data:
            #注释，虽然pop()定义是随机删除，但实际上是删除最后一个元素
            self.input_text_data = self.input_text_data[:-1]
            self.delete = False
        else:
            pass
        return self.input_text_data

if __name__ == '__main__':
    FPS = 60
    black = (74,74,74)
    screen_width = 1920
    screen_height = 1080
    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('歡樂鬥地主')
    name = Intput_box(screen,600,500,'name')
    password = Intput_box(screen,600,600,'password')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                bgdata.ask_quetion('quit','do you want to quit right now?')
        screen.fill(black)
        name.draw()
        password.draw()
        name.interact(event)
        password.interact(event)
        pygame.display.update()
