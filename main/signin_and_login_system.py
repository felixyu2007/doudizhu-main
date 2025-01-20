import bgdata
import json
import random
class Signin_and_login_method():
    def __init__(self):
        self.path = 'player_infomation\player_info.json'
        self.cache1 = {}
        self.cache2 = {}
        self.ai_list = ["bernard","elon","jeff","mark","larry","warren","bill"]
        self.key_list = [0,1,2,3,4,5,6]
        self.ais = []
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
            else:
                bgdata.ask_quetion('sign_error','uid or name or password incorrect')
        except:
            try:
                if username != self.data['user'][0][user_id] or password != self.data['user'][1][user_id]:
                    bgdata.ask_quetion('sign_error','uid or name or password incorrect')
                    return False
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
            
    def spended_fund(self,num,target):
        with open(self.path,mode='w') as opww:
            fund = self.data['user'][2][target]
            self.cache3 = {target:fund + num}
            self.data['user'][2].update(self.cache3)
            json.dump(self.data,opww,indent=4)

    def get_userinfo(self,userid):
        with open(self.path,mode='r',encoding='utf-8') as opr:
            self.data = json.load(opr)
        cache = [self.data['user'][0][userid],self.data['user'][2][userid]]
        return cache
    
    def get_aiinfo(self):
        ans = random.choice(self.key_list)
        self.ais.append(self.ai_list[ans])
        print(self.ai_list)
        print(self.key_list)
        print(ans)
        del self.key_list[ans]
        ans2 = random.choice(self.key_list)
        print(self.ai_list)
        print(self.key_list)
        print(ans2)
        self.ais.append(self.ai_list[ans2])
        ai_name = self.data[self.ais[0]][0]['username']
        ai_fund = self.data[self.ais[0]][1]['fund']
        ai_name2 = self.data[self.ais[1]][0]['username']
        ai_fund2 = self.data[self.ais[1]][1]['fund']
        print(ai_name,ai_fund,ai_name2,ai_fund2)
        return [ai_name,ai_fund,ai_name2,ai_fund2]
            