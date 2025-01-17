import function_data.bgdata
import json
class Signin_and_login_method():
    def __init__(self):
        self.path = 'player_infomation\player_info.json'

    def sign_up(self,usertextname: str,usertextpassword: str):
        usn = usertextname
        usp = usertextpassword
        usm = 10000
        usinfo = {'username':usn,'userpassword':usp,'userfunding':usm}
        bill_gate = {"ai_username": "Bill Gate", "userpassword": "", "userfunding": 4000000}
        elon_musk = {"ai_username": "Elon_Musk", "userpassword": "", "userfunding": 5000000}
        all_player_info = {usinfo,bill_gate,elon_musk}
        with open(self.path,mode='w',encoding='utf-8') as opw:
            json.dump(all_player_info,opw)
            print(usinfo,opw)

    def login(self,usertextname: str,usertextpassword: str):
        with open(self.path,mode='r',encoding='utf-8') as opr:
            userinfo = json.load(opr)
            print(userinfo)
        if usertextname != userinfo['username'] or usertextpassword != userinfo['userpassword']:
            function_data.bgdata.ask_quetion('sign error','name or password not correct')
            return False
        else:return True
        
    def del_account(delete_target):
        with open('player_infomation\player_info.json',mode='r',encoding='utf-8') as get:
            userinfo = json.load(get)
            ans = userinfo[delete_target]
            return ans
        
    def get_userinfo():
        with open('player_infomation\player_info.json',mode='r',encoding='utf-8') as get:
            userinfo = json.load(get)
            ans = [userinfo['username'],userinfo['userfunding']]
            return ans
            