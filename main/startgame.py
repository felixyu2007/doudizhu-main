from refresh_system import *
get_cards()
sp = Sign_page(screen,signed)
m = Menu(screen,'''wait to drop''')
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ask_quetion('quit','do you want to quit right now?')
        if getin == False:
            sp.sign_page(event)
        if sp.sign_page(event):
            getin = True
            screen.fill(black)
    pygame.display.flip()

