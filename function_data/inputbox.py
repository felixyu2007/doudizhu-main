import pygame
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
        self.timewait = 0
    def draw(self):
        #绘制输入框
        pygame.draw.rect(self.surf,(74,74,74),self.rect1,2)
        #渲染输入框题目
        inputbox_name = self.textsize1.render(self.inputbox_title,True,(74,74,74))
        self.surf.blit(inputbox_name,(self.inputbox_x_coordinate,self.inputbox_y_coordinate-30))
        #渲染输入了的文字
        input_text = self.textsize1.render(self.input_text_data,True,(74,74,74))
        self.surf.blit(input_text,(self.inputbox_x_coordinate + 5,self.inputbox_y_coordinate + 5))

        self.timewait += 1
        if self.focus == True and self.timewait == 60:
            self.cursor = not self.cursor
            self.timewait = 0

        if self.cursor == True and self.focus == True:
            input_text_last_letter_position = input_text.get_rect()
            coordinatex = self.rect1.x+5+input_text_last_letter_position.width
            pygame.draw.line(self.surf,(74,74,74),(coordinatex,self.inputbox_y_coordinate+5),(coordinatex,self.inputbox_y_coordinate+25),2)

    def interact(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect1.collidepoint(event.pos):
                self.focus = True
            else:
                self.focus = False
        elif self.focus == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.delete = True
                else:
                    self.input_text_data += event.unicode
        #删除方法
        if self.delete == True and self.input_text_data:
            #注释，虽然pop()定义是随机删除，但实际上是删除最后一个元素
            self.input_text_data = self.input_text_data[:-1]
            self.delete = False
        else:
            pass
        return self.input_text_data


