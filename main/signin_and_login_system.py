import bgdata
import json
class Signin_and_login_method():
    def __init__(self):
        self.path = 'player_infomation\player_info.json'
        self.cache1 = {}
        self.cache2 = {}
        with open(self.path,mode='r',encoding='utf-8') as opr:
            self.data = json.load(opr)

    def create_account(self,user_id,username,password):
        if user_id in self.data['user'][0]:
            bgdata.ask_quetion('sign_error','account existed')
            return False
        if user_id not in self.data['user'][0]:
            Signin_and_login_method.save_account(self,user_id,username,password)
            bgdata.ask_quetion('login?','account created')
            return True

    def login(self,user_id,username,password):
        try:
            if username == self.data['user'][0][user_id] and password == self.data['user'][1][user_id]:
                return True
        except:
            bgdata.ask_quetion('sign_error','uid or name or password incorrect')
            return False

    def save_account(self,user_id,username,password):
        with open(self.path,mode='w') as opw:
            self.cache1 = {user_id:username}
            self.cache2 = {user_id:password}
            self.cache3 = {user_id:10000000}
            self.data['user'][0].update(self.cache1)
            self.data['user'][1].update(self.cache2)
            self.data['user'][2].update(self.cache3)
            json.dump(self.data,opw,indent=4)

    def delete_account(self,target):
        with open(self.path,mode='w',encoding='utf-8') as opw:
            if target in self.data['user'][0]:
                del self.data['user'][0][target]
                del self.data['user'][1][target]
                del self.data['user'][2][target]
                json.dump(self.data,opw,indent=4)
                return True
            if target not in self.data['user'][0]:
                json.dump(self.data,opw,indent=4)
                bgdata.ask_quetion('sign_error','account not existed')
                return False
            
    def get_userinfo(self,userid):
        cache = [self.data['user'][0][userid],self.data['user'][2][userid]]
        return cache
    def get_aiinfo(self):
        pass
            