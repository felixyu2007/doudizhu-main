from refresh_system import *
get_cards()
while True:
    sp = Sign_page(screen,signed,started)
    sp.sign_page()
    
    pygame.display.flip()

