from refresh_system import *
get_cards()
sp = Sign_page(screen,signed,getin)
m = Menu(screen,'''wait to drop''','''wait to drop''')
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ask_quetion('quit','do you want to quit right now?')
        if started == False:
            if getin == False:
                sp.sign_page(event,pygame.mouse.get_pos())
            elif getin == True:
                m.draw_menu()
    pygame.display.flip()

