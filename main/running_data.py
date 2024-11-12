#import cache
from front import *
difficult_choosed = False
difficult_rect1 = (550,600,50,20)
difficult_rect2 = (1050,600,50,20)
difficult_rect3 = (1550,600,50,20)
#quit or other method function messagebox
class Main():
    def ask_quetion(input_title,input_message):
        ans = messagebox.askquestion(title=input_title,message=input_message)
        if ans == 'yes' and input_title == 'quit':
            pygame.quit()
            quit()
        if ans == 'yes' and input_title == 'signin?':
            pass
    def get_cards():
        for p in imgs:
            poker_data.append(p)

    pygame.display.set_caption('歡樂鬥地主')
    def game_main():
        #the main part of the game,it is a cycle to refresh the graphic interface
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main.ask_quetion('quit','wuld you want to quit the game?')
                if ined == False:
                    Signin_and_login_system.signup_system()
                else:
                    if difficult_choosed == False:
                        pygame.draw.rect(screen,black,difficult_rect1)
                        pygame.draw.rect(screen,black,difficult_rect2)
                        pygame.draw.rect(screen,black,difficult_rect3)

            pygame.display.update()


