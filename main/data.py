#import all the module need to use
from random import *
import pygame
import time
from os import *
import os.path
import sys
import tkinter
from tkinter import messagebox
pygame.init()
pygame.font.init()
#basic function
FPS = 60
clock = pygame.time.Clock()
screen_width = 1920
screen_height = 1080
round = 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('歡樂鬥地主')
#背景颜色
orange = (204,115,63)
green = (49,174,91)
dark_green = (37,96,57)
red = (219,81,81)
black = (74,74,74)
#背景图片与图形渲染的固定位置
points = [(420,200),(425,205),(400,240),(1520,240),(400,90,1100,300)
          ,(400,239),(1520,239),(410,110,1100,260),(600,500,300,30)
          ,(600,600,300,30),(600,480),(600,580),(1100,480),(900,100)
          ,(100,100),(50,50,1820,980)]
cards_points = [(300,800),(300,810),(300,820),(300,830),(300,840),(300,850)]
#背景图片与图形渲染的可活动位置
movingpoint1 = [0,0,1920,1080]
#设定渲染文字的字形与内容
titletext1 = pygame.font.Font(None,140)
titletext2 = pygame.font.Font(None,140)
textsize2 = pygame.font.Font(None,60)
title = titletext1.render('Fighting The Landlord',True,red)
bgtitle = titletext2.render('Fighting The Landlord',True,black)
starttitle = textsize2.render('start',True,black)

#是否已互动预设
running = True
signed = False
ined = False
started = False
getin = False


#四边形
difficult_rect1 = pygame.Rect(550,600,100,40)
difficult_rect2 = pygame.Rect(1050,600,100,40)
difficult_rect3 = pygame.Rect(1550,600,100,40)
start_rect = pygame.Rect(1050,600,100,40)
menu_rect = pygame.Rect(0,0,100,1080)
#background and cardback and button image
background_image = pygame.image.load(r'button_image\background.png')
cardback = pygame.image.load('button_image\card_back.png')
button_image01 = pygame.image.load(r'button_image\background.png')
button_image02 = pygame.image.load(r'button_image\button01.jpg')
button_image03 = pygame.image.load(r'button_image\button02.jpg')
button_image04 = pygame.image.load(r'button_image\button(1).png')
button_image05 = pygame.image.load(r'button_image\button01(1).png')
button_image06 = pygame.image.load(r'button_image\button02(1).png')
button_image07 = pygame.image.load('button_image\SIGNIN.png')
button_image08 = pygame.image.load('button_image\png.png')
textfont = pygame.font.SysFont('Raleway_Bold',50)
roundtext = textfont.render('第1回合',True,'white')
yifapaitext = textfont.render('已经发牌了哦~~~',True,'white')
#poker image
poker_image_path = r'PNG-cards-1.3'
imgs = listdir(poker_image_path)
poker_data = []
choosed_poker_data = []

def ask_quetion(input_title,input_message):
    global ined
    ans = messagebox.askquestion(title=input_title,message=input_message)
    if ans == 'yes' and input_title == 'quit':
        pygame.quit()
        quit()
    if ans == 'yes' and input_title == 'login?':
        ined = True
def get_cards():
    for p in imgs:
        poker_data.append(p)

