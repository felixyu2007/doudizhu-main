from running_data import *
get_cards()
while running == True:  
    Main()
    clock.tick(FPS)
    pygame.display.flip()

