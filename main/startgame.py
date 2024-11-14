from refresh_system import *
get_cards()
sp = Sign_page(screen,signed,started)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ask_quetion('quit','do you want to quit right now?')
        
        sp.sign_page(event)
        
    pygame.display.flip()

