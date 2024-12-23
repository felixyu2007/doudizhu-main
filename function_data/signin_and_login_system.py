import function_data.bgdata as bgdata
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    with open('main\player_info.bgdata.json',mode='w') as opw:
        bgdata.json.dump(usinfo,opw)

def login(usertextname: str,usertextpassword: str):
    with open('main\player_info.bgdata.json',mode='r') as opr:
        userinfo = bgdata.json.load(opr)
        print(userinfo)
    if usertextname != userinfo['username'] or usertextpassword != userinfo['userpassword']:
        bgdata.ask_quetion('sign error','name or password not correct')
        return False
    else:
        return True
    
def get_userinfo():
    with open('main\player_info.bgdata.json',mode='r') as get:
        userinfo = bgdata.json.load(get)
        ans = [userinfo['username'],userinfo['userfunding']]
        return ans

        