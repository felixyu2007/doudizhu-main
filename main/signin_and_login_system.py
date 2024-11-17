from data import *
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    with open('main\player_info.json',O_WRONLY) as opw:
        json.dump(usinfo,opw)

def login():
    pass

def get_userinfo():
    pass

        