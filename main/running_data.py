#import cache
from cache import *
difficult_rect1 = ()
difficult_rect2 = ()
difficult_rect3 = ()
#quit or other method function messagebox
class Main():
    def ask_quetion(input_title,input_message):
        ans = messagebox.askquestion(title=input_title,message=input_message)
        if ans == 'yes' and input_title == 'quit':
            pygame.quit()
            quit()
        if ans == 'yes' and input_title == 'signin?':
            pass
        if ans == 'yes' and input_title == 'login?':
            
            Main.game_main()
    def poker():
        for p in imgs:
            poker_data.append(p)

    pygame.display.set_caption('歡樂鬥地主')
    def game_main():
        global round
        #the main part of the game,it is a cycle to refresh the graphic interface
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main.ask_quetion('quit','wuld you want to quit the game?')
                pygame.draw.rect()
            #     if round == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            #         if 685 < pygame.mouse.get_pos()[0] < 835 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             round += 1
            #         if 885 < pygame.mouse.get_pos()[0] < 1035 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             None
            #         if 1085 < pygame.mouse.get_pos()[0] < 1235 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             None
            #     else:
            #         if 685 < pygame.mouse.get_pos()[0] < 835 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             None
            #         if 885 < pygame.mouse.get_pos()[0] < 1035 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             None
            #         if 1085 < pygame.mouse.get_pos()[0] < 1235 and 1000 < pygame.mouse.get_pos()[1] < 1042:
            #             None
            pygame.display.update()


