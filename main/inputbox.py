from signin_and_login_system import *

def inputbox():
    global usertextname,usertextpassword
    while running == True:
        screen.fill(green)
        pygame.draw.rect(screen,black,rect1,2)
        pygame.draw.rect(screen,black,rect2,2)
        userinputname = textsize1.render(usertextname,True,black)
        userinputpassword = textsize1.render(usertextpassword,True,black)
        screen.blit(userinputname,points[8])
        screen.blit(userinputpassword,points[9])
        screen.blit(nametext,points[10])
        screen.blit(passwordtext,points[11])
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 600 < pygame.mouse.get_pos()[0] < 1200 and 500 < pygame.mouse.get_pos()[1] < 530:
                    interact1 = True
                    interact2 = False
                    
                if 600 < pygame.mouse.get_pos()[0] < 1200 and 600 < pygame.mouse.get_pos()[1] < 630:
                    interact2 = True
                    interact1 = False
                
                if usertextname != '' and usertextpassword != '':
                    if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217:
                        sign_up(usertextname,usertextpassword)
                    else:
                        pass

            if event.type == pygame.KEYDOWN:
                if interact1 == True:
                    if len(usertextname) > 30:
                        usertextname = usertextname[:-1]
                    elif event.key == pygame.K_BACKSPACE:
                        usertextname = usertextname[:-1]
                    else:
                        usertextname += event.unicode

                if interact2 == True:
                    if len(usertextpassword) > 30:
                        usertextpassword = usertextpassword[:-1]
                    elif event.key == pygame.K_BACKSPACE:
                        usertextpassword = usertextpassword[:-1]
                    else:
                        usertextpassword += event.unicode
        pygame.display.update()
inputbox()