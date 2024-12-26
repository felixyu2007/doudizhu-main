import json
import pygame
pygame.init()
pygame.font.init()
from tkinter import messagebox
def ask_quetion(input_title,input_message):
    global ined
    ans = messagebox.askquestion(title=input_title,message=input_message)
    if ans == 'yes' and input_title == 'quit':
        quit()
    if ans == 'yes' and input_title == 'login?':
        ined = True
    if ans == 'yes' and input_title == 'sign error':
        return False
