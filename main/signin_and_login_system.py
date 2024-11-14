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
    pass