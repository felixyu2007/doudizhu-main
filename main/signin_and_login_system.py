import json
from data import *
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    with open('main\player_info.json',mode='w') as opw:
        json.dump(usinfo,opw)

def login(usertextname: str,usertextpassword: str):
    with open('main\player_info.json',mode='r') as opr:
        userinfo = json.load(opr)
        print(userinfo)
    if usertextname != userinfo['username'] or usertextpassword != userinfo['userpassword']:
        ask_quetion('sign error','name or password not correct')
        return False
    else:
        return True
    
def get_userinfo():
    with open('main\player_info.json',mode='r') as get:
        userinfo = json.load(get)
        ans = [userinfo['username'],userinfo['userfunding']]
        return ans

        