from data import *
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    json.dump(usinfo,'player_info.json',indent=4)

def login():
    pass
def get_userinfo():
    pass

        