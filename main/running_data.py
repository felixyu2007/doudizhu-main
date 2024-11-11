#import cache
from cache import *
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
    def show1():
        screen.blit(background_image,[0,0])
        screen.blit(roundtext,[885,400])
        screen.blit(cardback,[885,100])
        screen.blit(button_image01,[685,1000])
        screen.blit(button_image05,[885,1000])
        screen.blit(button_image06,[1085,1000])
    def show2():
        screen.blit(background_image,[0,0])
        screen.blit(cardback,[885,100])
        screen.blit(button_image04,[685,1000])
        screen.blit(button_image02,[885,1000])
        screen.blit(button_image03,[1085,1000])
    #set the game screen size

    pygame.display.set_caption('歡樂鬥地主')
    def game_main():
        global round
        #the main part of the game,it is a cycle to refresh the graphic interface
        while True:
            clock.tick(FPS)
            Main.show1()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        Main.ask_quetion('quit','wuld you want to quit the game?')
                    if round == 0 and event.type == pygame.MOUSEBUTTONDOWN:
                        if 685 < pygame.mouse.get_pos()[0] < 835 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            round += 1
                        if 885 < pygame.mouse.get_pos()[0] < 1035 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            None
                        if 1085 < pygame.mouse.get_pos()[0] < 1235 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            None
                    else:
                        if 685 < pygame.mouse.get_pos()[0] < 835 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            None
                        if 885 < pygame.mouse.get_pos()[0] < 1035 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            None
                        if 1085 < pygame.mouse.get_pos()[0] < 1235 and 1000 < pygame.mouse.get_pos()[1] < 1042:
                            None
            pygame.display.update()


