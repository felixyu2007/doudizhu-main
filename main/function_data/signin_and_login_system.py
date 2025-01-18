import function_data.bgdata
import json
class Signin_and_login_method():
    def __init__(self):
        self.path = 'player_infomation\player_info.json'
        self.data = ''
    def create_account(self,username,password):
        with open(self.path,mode='r') as opr:
            self.data = json.load(opr)
            if username in self.data:
                function_data.bgdata.ask_quetion('sign_error','account existed')
                return False
            if username not in self.data:
                Signin_and_login_method.save_account(self,username,password)
                function_data.bgdata.ask_quetion('login?','account created')
                return True

    def login(self):
        pass
    def save_account(self,username,password):
        with open(self.path,mode='w+') as opw:
            cache = {username:password}
            json.dump(cache,opw)
    def delete_account(self,target):
        with open(self.path,mode='r+') as opr:
            self.data = json.load(opr)
            if target in self.data:
                return True
            if target not in self.data:
                function_data.bgdata.ask_quetion('sign_error','account not existed')
                return False
    def get_userinfo(self):
        with open(self.path,mode='r') as opr:
            self.data = json.load(opr)
            
            