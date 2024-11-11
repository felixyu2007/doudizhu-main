#import all the module need to use
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
FPS = 240
clock = pygame.time.Clock()
screen_width = 1920
screen_height = 1080
timer = time.sleep(1)
round = 0
screen = pygame.display.set_mode((screen_width, screen_height))
#background and cardback and button image
background_image = pygame.image.load(r'button_image\background.png')
cardback = pygame.image.load('PNG-cards-1.3\card_back.png')
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
