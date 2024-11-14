from cache import *
def save_system(name,password):
    opw = os.open('txt_data\player_data',os.O_RDWR)
    os.write(opw,name)
    os.write(opw,password)
    os.close(opw)
    ask_quetion('login?','do you want to login now?')
def sign_up(usertextname,usertextpassword):
    usn = os.fsencode(usertextname)
    usp = os.fsencode(usertextpassword)
    save_system(usn,usp)     
    
def login():
    if input_text_data != '':
        if 1100 < pygame.mouse.get_pos()[0] < 1100+150 and 480 < pygame.mouse.get_pos()[1] < 480+217:
            sign_up(input_text_data)
        else:
            pass