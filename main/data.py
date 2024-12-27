import pygame
pygame.init()
pygame.font.init()
#basic function
FPS = 240
screen_width = 1920
screen_height = 1080

#背景颜色
orange = (204,115,63)
green = (49,174,91)
dark_green = (37,96,57)
red = (219,81,81)
black = (74,74,74)

white2 = (255,255,255)
orange2 = (255,127,39)
green2 = (0,222,63)
red2 = (236,28,36)
blue2 = (0,168,243)
draw_points1 = [(50,1030),(50,500),(200,450),(600,500),(700,500),(1000,550),(1200,400),(1500,380),(1820,500),(1870,1030)]
draw_points2 = [(50,1030),(50,600),(300,550),(560,580),(680,500),(1020,500),(1240,560),(1540,480),(1870,620),(1870,1030)]
draw_points3 = [(50,1030),(50,550),(400,640),(660,680),(750,600),(1030,560),(1210,660),(1570,580),(1840,750),(1870,1030)]
draw_points4 = [(50,1030),(50,700),(300,680),(630,800),(730,700),(1080,670),(1260,680),(1520,680),(1870,730),(1870,1030)]
draw_points5 = [(50,1030),(50,850),(350,850),(610,800),(790,800),(1050,850),(1230,680),(1590,750),(1870,900),(1870,1030)]
draw_points6 = [(50,540),(50,730),(400,1030),(620,1030)]
draw_points7 = [(1200,1030),(1200,900),(1300,900),(1300,850),(1400,850),(1400,950),(1500,950),(1500,1030)]

#背景图片与图形渲染的固定位置
points = [(420,200),(425,205),(400,240),(1520,240),(400,90,1100,300)
          ,(400,239),(1520,239),(410,110,1100,260),(600,500,300,30)
          ,(600,600,300,30),(600,480),(600,580),(1100,480),(900,100)
          ,(100,100),(50,50,1820,980)]
cards_points = [(300,800),(300,810),(300,820),(300,830),(300,840),(300,850)]
#
disable_button = []

#背景图片与图形渲染的可活动位置
movingpoint1 = [0,0,1920,1080]

#是否已互动预设
running = True
signed = False
started = False
getin = False
money = 10000
login_mode = False

#background and cardback and button image
background_image = pygame.image.load(r'button_image\background.png')
cardback = pygame.image.load('button_image\card_back.png')
# button_image01 = pygame.image.load(r'button_image\background.png')
# button_image02 = pygame.image.load(r'button_image\button01.jpg')
# button_image03 = pygame.image.load(r'button_image\button02.jpg')
# button_image04 = pygame.image.load(r'button_image\button(1).png')
# button_image05 = pygame.image.load(r'button_image\button01(1).png')
# button_image06 = pygame.image.load(r'button_image\button02(1).png')
button_image07 = pygame.image.load('button_image\SIGNIN.png')
button_image08 = pygame.image.load('button_image\png.png')
button_image09 = pygame.image.load(r'button_image\rule.png')
# textfont = pygame.font.SysFont('Raleway_Bold',50)
# roundtext = textfont.render('第1回合',True,'white')
# yifapaitext = textfont.render('已经发牌了哦~~~',True,'white')
#poker image