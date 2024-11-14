from sign_page import * 
class Menu():
    def __init__(self,difficult_choosed: bool):
        self.difficult_choosed = difficult_choosed
    def difficult_choosen(self,event):
        print('in!!!')
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