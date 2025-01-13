import function_data.bgdata
import json
def sign_up(usertextname: str,usertextpassword: str):
    usn = usertextname
    usp = usertextpassword
    usm = 10000
    usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
    with open('player_infomation\player_info.json',mode='w',encoding='utf-8') as opw:
        json.dump(usinfo,opw)
        print(usinfo,opw)

def login(usertextname: str,usertextpassword: str):
    with open('player_infomation\player_info.json',mode='r',encoding='utf-8') as opr:
        userinfo = json.load(opr)
        print(userinfo)
    if usertextname != userinfo['username'] or usertextpassword != userinfo['userpassword']:
        function_data.bgdata.ask_quetion('sign error','name or password not correct')
        return False
    else:
        return True
    
def get_userinfo():
    with open('player_infomation\player_info.json',mode='r',encoding='utf-8') as get:
        userinfo = json.load(get)
        ans = [userinfo['username'],userinfo['userfunding']]
        return ans

        