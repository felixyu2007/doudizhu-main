from data import *
def sign_up(usertextname,usertextpassword):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    json.dump(usinfo,open('main\player_info.json','w'),indent=4)

def login():
    pass
def get_userinfo():
    pass

        