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
        userinfo = json.loads(opr).decode('utf-8')
        print(userinfo)
    if usertextname not in userinfo or usertextpassword not in userinfo:
        ask_quetion('sign error','name or password not correct')
        return False
    else:
        return True
def get_userinfo():
    pass

        