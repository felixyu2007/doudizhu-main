from signin_and_login_system import *
#登入界面输入位置

def inputbox(inputbox_x_coordinate,inputbox_y_coordinate,inputbox_title: str):
    global input_text_data
    interact = False
    while running == True:
        screen.fill(green)
        rect1 = pygame.Rect(inputbox_x_coordinate,inputbox_y_coordinate,600,30)
        inputbox_name = textsize1.render(inputbox_title,True,black)
        screen.blit(inputbox_name,(inputbox_x_coordinate,inputbox_y_coordinate-20))
        pygame.draw.rect(screen,black,rect1,2)
        input_text = textsize1.render(input_text_data,True,black)
        screen.blit(input_text,(inputbox_x_coordinate,inputbox_y_coordinate))
        
        for event in pygame.event.get():
            if rect1.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                interact = True

            if event.type == pygame.KEYDOWN:
                if interact == True:
                    if len(input_text_data) > 30:
                        input_text_data = input_text_data[:-1]
                    elif event.key == pygame.K_BACKSPACE:
                        input_text_data = input_text_data[:-1]
                    else:
                        input_text_data += event.unicode
        pygame.display.update()

inputbox(200,300,'hi')