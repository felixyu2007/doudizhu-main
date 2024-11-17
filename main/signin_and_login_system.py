from data import *

def save_system(name,password):
    with open('txt_data\player_data',O_RDWR) as opw:
        os.write(opw,name)
        os.write(opw,password)
        os.close(opw)
    ask_quetion('login?','do you want to login now?')
    return
def sign_up(usertextname,usertextpassword):
    usn = os.fsencode(usertextname)
    usp = os.fsencode(usertextpassword)
    save_system(usn,usp)     
    return
def login():
    pass
def get_userinfo():
    with open('txt_data\player_data',os.O_RDONLY) as opr:
        userinformaton = opr.read()

        