from data import *
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    with open('player_info.json','w') as opw:
        opw = str(opw)
        json.dump(usinfo,opw)

def login():
    pass
def get_userinfo():
    pass

        