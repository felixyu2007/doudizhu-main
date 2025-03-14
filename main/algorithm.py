from bgdata import *
import random
import os
from button import *
from data import *
from signin_and_login_system import * 

class Game_algorithm():
    def __init__(self,screen):
        self.surf = screen
        self.sign = Signin_and_login_method()
        self.round = 0
        self.price = 0
        self.straight = 0
        self.prevous_card = {}
        self.ai_prevous_card1 = {}
        self.ai_prevous_card2 = {}
        self.current_card = {}
        self.free_hand = False
        self.ai_free_hand1 = False
        self.ai_free_hand2 = False
        self.cursor = False
        self.winner = False
        self.feedback1 = False
        self.feedback2 = False
        self.passround = False
        #创建各种牌组和字典（地主牌3张，3个玩家各17张）
        self.poker_image_path = r'PNG-cards-1.3'
        self.imgs = os.listdir(self.poker_image_path)
        self.poker = {}
        self.choosed_dizhu_poker = {}
        self.choosed_poker01 = {}
        self.choosed_poker02 = {}
        self.user_choosed_poker = {}
        self.choosed_poker_cache = {}
        self.card_blit_point = {}
        self.card_play_point = {}
        self.prevous_card_point = {}
        self.ai_prevous_card_point1 = {}
        self.ai_prevous_card_point2 = {}
        self.choose_poker = []
        self.sort_cache = []
        self.sort_cache_dict = {}
        self.key_dict = {}
        self.key_dict2 = {}
        #调用先前写好的按钮函数
        self.increase_btn = Button(self.surf,1200,650,'increase',green)
        self.decrease_btn = Button(self.surf,1200,750,'decrease',green)
        self.bet_button = Button(self.surf,1450,750,'bet',green)
        self.grab_button = Button(self.surf,1450,850,'landlord',green)
        self.unrob_button = Button(self.surf,1450,950,'people',green)
        self.pass_btn = Button(self.surf,1200,650,'pass',green)
        self.play_btn = Button(self.surf,1500,650,'play',green)
        #要把下注的金额绘制出来
        self.text = pygame.font.Font(None,100)
        self.priceshow = self.text.render(''.join(str(self.price)),True,(255,255,255))
        self.card_start_point = [450,750]
        self.position = 0
        self.choosen = False
        
    def get_poker(self):
        self.choosed_dizhu_poker.clear()
        self.choosed_poker01.clear()
        self.choosed_poker02.clear()
        self.user_choosed_poker.clear()
        self.poker.clear()
        self.sort_cache.clear()
        self.sort_cache.clear()
        self.card_blit_point.clear()
        self.choosen = False

######################################################################################################################################################################
        
        #往牌组里随机抽出牌然后分别放入（地主牌，3个玩家各17张）
        for p in self.imgs:
            baba = os.path.dirname(os.path.abspath(p))
            self.haha = os.path.join(baba,self.poker_image_path+'\\'+p)
            self.image_surface = pygame.image.load(self.haha)
            poker_dict = {p:self.image_surface}
            self.poker.update(poker_dict)#为{path:surface}

######################################################################################################################################################################
        
        #地主牌的
        for a in range(3):
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_dizhu_poker.update(self.choosed_poker_cache)#为{path:surface}
            del self.poker[self.choose_poker]
            
        self.sort_cache = list(self.choosed_dizhu_poker.keys())
        self.sort_cache.sort(reverse=False)
        line()
        print(self.sort_cache)
        for a in self.sort_cache:
            self.choosed_poker_cache = {a:self.choosed_dizhu_poker[a]}
            self.sort_cache_dict.update(self.choosed_poker_cache)
        self.choosed_dizhu_poker.clear()
        self.choosed_dizhu_poker.update(self.sort_cache_dict)
        self.sort_cache_dict.clear()
        line()
        print(self.choosed_dizhu_poker)

######################################################################################################################################################################
        
        #3个玩家的
        for b in range(17):
            #ai的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker01.update(self.choosed_poker_cache)#为{path:surface}
            del self.poker[self.choose_poker]
            #ai的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.choosed_poker02.update(self.choosed_poker_cache)#为{path:surface}
            del self.poker[self.choose_poker]
            #玩家的
            self.choose_poker = random.choice(list(self.poker.keys()))
            self.choosed_poker_cache = {self.choose_poker:self.poker[self.choose_poker]}
            self.user_choosed_poker.update(self.choosed_poker_cache)#为{path:surface}
            del self.poker[self.choose_poker]

######################################################################################################################################################################
        
        #ai的  
        self.sort_cache = list(self.choosed_poker01.keys())
        self.sort_cache.sort(reverse=False)
        line()
        print(self.sort_cache)
        for b in self.sort_cache:
            self.choosed_poker_cache = {b:self.choosed_poker01[b]}
            self.sort_cache_dict.update(self.choosed_poker_cache)
        self.choosed_poker01.clear()
        self.choosed_poker01.update(self.sort_cache_dict)
        self.sort_cache_dict.clear()
        line()
        print(self.choosed_poker01)
        
        #ai的
        self.sort_cache = list(self.choosed_poker02.keys())
        self.sort_cache.sort(reverse=False)
        line()
        print(self.sort_cache)
        for b in self.sort_cache:
            self.choosed_poker_cache = {b:self.choosed_poker02[b]}
            self.sort_cache_dict.update(self.choosed_poker_cache)
        self.choosed_poker02.clear()
        self.choosed_poker02.update(self.sort_cache_dict)
        self.sort_cache_dict.clear()
        line()
        print(self.choosed_poker02)

        #玩家的
        self.sort_cache = list(self.user_choosed_poker.keys())
        self.sort_cache.sort(reverse=False)
        line()
        print(self.sort_cache)
        for b in self.sort_cache:
            self.choosed_poker_cache = {b:self.user_choosed_poker[b]}
            self.sort_cache_dict.update(self.choosed_poker_cache)
        self.user_choosed_poker.clear()
        self.user_choosed_poker.update(self.sort_cache_dict)
        self.sort_cache_dict.clear()
        line()
        print(self.user_choosed_poker)
        line()

######################################################################################################################################################################

    def run(self,event,mouseevent):
        #创建第零回合，询问是否抢地主
        if self.round == 0:
            grab = self.grab_button.clickbutton(mouseevent,event)
            ungrab = self.unrob_button.clickbutton(mouseevent,event)
            if grab == True:
                self.round += 1
                Game_algorithm.get_poker(self)
                self.choosen = True
            if ungrab == True:
                self.round += 1
                Game_algorithm.get_poker(self)
                self.choosen == False

######################################################################################################################################################################
    
        #第一回合需要下注与创建玩家所持的卡的字典，其中是{卡的surface：【卡绘制的位置x，卡绘制的位置y】}
        elif self.round == 1:
            high = self.increase_btn.clickbutton(mouseevent,event)
            low = self.decrease_btn.clickbutton(mouseevent,event)
            bet = self.bet_button.clickbutton(mouseevent,event)
            pygame.draw.rect(self.surf,(74,74,74),(1450,650,200,60))
            self.surf.blit(self.priceshow,(1450,650))
            if high == True:
                self.price += 10000
                if self.price >= 1000000:
                    self.price = 1000000
                self.priceshow = self.text.render(''.join(str(self.price)),True,(255,255,255))
            if low == True:
                self.price -= 10000
                if self.price <= 0:
                    self.price = 0
                self.priceshow = self.text.render(''.join(str(self.price)),True,(255,255,255))

######################################################################################################################################################################

            if bet == True and self.price != 0 and self.choosen == False:#判断是否抢地主
                for d in self.user_choosed_poker.keys():##为{path:surface}
                    self.cache = {d:[self.card_start_point[0]+self.position,self.card_start_point[1]]}
                    self.card_blit_point.update(self.cache)#为{path:position}
                    self.position += 50
                self.position = 0
                self.round += 1
                print(self.card_blit_point)
                dizhu = random.randint(0,1)
                if dizhu:
                    self.choosed_poker01.update(self.choosed_dizhu_poker)
                else:
                    self.choosed_poker02.update(self.choosed_dizhu_poker)
                #ai 一号的手牌
                print(self.choosed_poker01)
                #ai 二号的手牌
                print(self.choosed_poker02)

            if bet == True and self.price != 0 and self.choosen == True:#判断是否抢地主
                self.user_choosed_poker.update(self.choosed_dizhu_poker)#抢了地主会额外拿到3张牌
                self.free_hand = True
                self.sort_cache = list(self.user_choosed_poker.keys())
                self.sort_cache.sort(reverse=False)
                line()
                print(self.sort_cache)
                for d in self.sort_cache:
                    self.choosed_poker_cache = {d:self.user_choosed_poker[d]}
                    self.sort_cache_dict.update(self.choosed_poker_cache)
                self.user_choosed_poker.clear()
                self.user_choosed_poker.update(self.sort_cache_dict)
                self.sort_cache_dict.clear()
                line()
                print(self.user_choosed_poker)

                for d in self.user_choosed_poker.keys():#为{path:surface}
                    self.cache = {d:[self.card_start_point[0]+self.position,self.card_start_point[1]]}
                    self.card_blit_point.update(self.cache)#为{path:position}
                    self.position += 50
                self.position = 0
                self.round += 1
                line()
                print(self.card_blit_point)

############################################开始算法###################################################################################################################
        
        else:
            if self.choosen == False and self.round == 2:
                self.round += 1
                #自動pass,且決定地主
                #here the ai algorithm
                self.ai_free_hand1 = True
                Game_algorithm.ai_alorithm1(self)
                self.ai_free_hand2 = False
                Game_algorithm.ai_alorithm2(self)

            else:
                Game_algorithm.draw_cards(self,event,mouseevent)
                self.passround = self.pass_btn.clickbutton(mouseevent,event)
                ans = Game_algorithm.check_hand(self)#self.card_play_point.clear() and self.current_card.clear()
                
                if ans == True:
                    play = self.play_btn.clickbutton(mouseevent,event)
                    if play:
                        self.round += 1
                        self.position = 0
                        self.prevous_card_point.clear()
                        self.prevous_card.clear()
                        for d in self.current_card.keys():
                            self.cache = {d:[500+self.position,self.card_blit_point[d][1]-300]}
                            self.card_play_point.update(self.cache)#为{path:position}

                            self.cache = {d:[self.card_play_point[d][0],self.card_play_point[d][1]-50]}
                            self.prevous_card_point.update(self.cache)#为{path:position}

                            del self.card_blit_point[d]
                            del self.user_choosed_poker[d]

                            self.surf.blit(self.current_card[d],self.card_play_point[d])
                            self.position += 50
                        
                        self.prevous_card.update(self.current_card)#为{path:surface}
                        self.feedback1 = Game_algorithm.ai_alorithm1(self)
                        self.ai_free_hand2 = False
                        self.feedback2 = Game_algorithm.ai_alorithm2(self)
                        if self.feedback2 == False and self.feedback1 == False:
                            self.free_hand = True
                            print('free hand')
                        else:
                            self.free_hand = False
                            print('not free')
                    else:pass
                if self.passround == True:
                    self.round += 1
                    self.ai_free_hand1 = False
                    self.feedback1 = Game_algorithm.ai_alorithm1(self)
                    if self.feedback1 == False:
                        self.ai_free_hand2 = True
                    else:
                        self.ai_free_hand2 = False
                    self.feedback2 = Game_algorithm.ai_alorithm2(self)
                    if self.feedback2 == False and self.feedback1 == False:
                        self.free_hand = True
                        print('free hand')
                    else:
                        self.free_hand = False
                        print('not free')
                ans4 = Game_algorithm.check_winner(self)
                if ans4 == True:
                    self.ai_prevous_card1.clear()
                    self.ai_prevous_card2.clear()
                    self.prevous_card.clear()
                    self.ai_prevous_card_point1.clear()
                    self.ai_prevous_card_point2.clear()
                    self.round = 0
                else:pass
                return ans4

######################################################################################################################################################################

    def return_spended_money(self):
        return self.price

        
######################################################################################################################################################################

    def draw_cards(self,event,mouseevent):
        for c in self.card_blit_point.keys():#为{path:position}
            self.image_scale = pygame.Rect(self.card_blit_point[c][0],self.card_blit_point[c][1],49,145)
            self.surf.blit(self.user_choosed_poker[c],self.card_blit_point[c])

            if self.image_scale.collidepoint(mouseevent):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.card_blit_point[c][1] == 730:
                        self.card_blit_point[c][1] = 700
                    elif self.card_blit_point[c][1] == 700:
                        self.card_blit_point[c][1] = 730
                else:
                    if self.card_blit_point[c][1] == 750:
                        self.card_blit_point[c][1] = 730
            elif not self.image_scale.collidepoint(mouseevent) and self.card_blit_point[c][1] != 700:
                self.card_blit_point[c][1] = 750
                
        for d in self.ai_prevous_card1.keys():
            self.surf.blit(self.ai_prevous_card1[d],self.ai_prevous_card_point1[d])
        for d in self.ai_prevous_card2.keys():
            self.surf.blit(self.ai_prevous_card2[d],self.ai_prevous_card_point2[d])
        for d in self.prevous_card.keys():
            self.surf.blit(self.prevous_card[d],self.prevous_card_point[d])
        

######################################################################################################################################################################

    def ai_alorithm1(self):
        self.ai_prevous_card_point1.clear()
        self.key_dict.clear()
        self.key_dict2.clear()
        key_list = list(self.choosed_poker01.keys())#path
        if self.passround == True and len(self.ai_prevous_card2) != 0:
            target_key_list = list(self.ai_prevous_card2.keys())#path
            for kl in range(len(target_key_list)):
                self.cache = {kl:int(target_key_list[kl][0:2])}
                self.key_dict.update(self.cache)#path of previous_card with no (letter).png
        elif self.passround == True and len(self.ai_prevous_card2) == 0 or self.passround == True and self.feedback2 == False:
            self.ai_free_hand1 = True
            target_key_list = []
        else:
            target_key_list = list(self.prevous_card.keys())#path
            for kl in range(len(target_key_list)):
                self.cache = {kl:int(target_key_list[kl][0:2])}
                self.key_dict.update(self.cache)#path of previous_card with no (letter).png

        for g in range(len(key_list)):
            self.cache = {g:int(key_list[g][0:2])}
            self.key_dict2.update(self.cache)#path of choosed_poker01 with no (letter).png

        if self.round == 2 or self.ai_free_hand1 == True:
            self.ai_prevous_card1.clear()
            self.ai_prevous_card_point1.clear()
            ans = random.choice(list(self.choosed_poker01.keys()))
            self.cache = {ans:self.choosed_poker01[ans]}
            self.ai_prevous_card1.update(self.cache)#为{path:surface}
            del self.choosed_poker01[ans]

            self.cache = {ans:[self.position+1200,200]}
            self.ai_prevous_card_point1.update(self.cache)#为{path:position}

            self.ai_free_hand1 = False
            return True
        else: 
            for g in range(len(key_list)):
                self.position = 0
                self.ai_prevous_card1.clear()
                self.ai_prevous_card_point1.clear()
                if len(self.key_dict) == 1:
                    if self.key_dict2[g] > self.key_dict[0]:
                        self.cache = {key_list[g]:self.choosed_poker01[key_list[g]]}
                        self.ai_prevous_card1.update(self.cache)#为{path:surface}
                        self.cache = {key_list[g]:[self.position+1200,200]}
                        self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                        del self.choosed_poker01[key_list[g]]
                        line()
                        print(self.ai_prevous_card1)
                        return True
                    else:pass
     
                elif len(self.key_dict) == 2:
                    if g == len(key_list)-2:
                        return False
                    elif self.key_dict2[g] == self.key_dict2[g + 1]:
                        if self.key_dict2[g] > self.key_dict[0]:
                            self.cache = {key_list[g]:self.choosed_poker01[key_list[g]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker01[key_list[g+1]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}

                            self.cache = {key_list[g]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}

                            del self.choosed_poker01[key_list[g]]
                            del self.choosed_poker01[key_list[g+1]]
                            line()
                            print(self.ai_prevous_card1)
                            return True
                        else:pass
                    
                elif len(self.key_dict) == 4:
                    if g == len(key_list)-4:
                        return False
                    elif self.key_dict[0] == self.key_dict[3]:
                        if self.key_dict2[g] > self.key_dict[0]:
                            self.cache = {key_list[g]:self.choosed_poker01[key_list[g]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker01[key_list[g+1]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+2]:self.choosed_poker01[key_list[g+2]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+3]:self.choosed_poker01[key_list[g+3]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}

                            del self.choosed_poker01[key_list[g]]
                            del self.choosed_poker01[key_list[g+1]]
                            del self.choosed_poker01[key_list[g+2]]
                            del self.choosed_poker01[key_list[g+3]]

                            self.cache = {key_list[g]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}

                            line()
                            print(self.ai_prevous_card1)
                            return True
                        else:pass   

                            
                    elif self.key_dict[0] != self.key_dict[3]:
                        if self.key_dict2[g] == self.key_dict2[g+1] == self.key_dict2[g+2] and self.key_dict2[g+3] or self.key_dict2[g-1]:
                            self.cache = {key_list[g]:self.choosed_poker01[key_list[g]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker01[key_list[g+1]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+2]:self.choosed_poker01[key_list[g+2]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+3]:self.choosed_poker01[key_list[g+3]]}
                            self.ai_prevous_card1.update(self.cache)#为{path:surface}
                            del self.choosed_poker01[key_list[g]]
                            del self.choosed_poker01[key_list[g+1]]
                            del self.choosed_poker01[key_list[g+2]]
                            del self.choosed_poker01[key_list[g+3]]

                            self.cache = {key_list[g]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+3]:[self.position+1200,200]}
                            self.ai_prevous_card_point1.update(self.cache)#为{path:position}

                            line()
                            print(self.ai_prevous_card1)
                            return True
                        else:pass
                    
                elif len(self.key_dict) >= 5:
                    if self.key_dict[0]+1 == self.key_dict[1]:
                        self.straight = len(self.key_dict)
                        if self.straight > 5:
                            return False
                        else:
                            self.cursor = True
                    elif self.key_dict[0] == self.key_dict[1]:
                        self.cursor = False

                    if g == len(key_list)-5:
                        return False

                    if self.cursor == True:
                        if self.key_dict2[g]+4 == self.key_dict2[g+1]+3 == self.key_dict2[g+2]+2 == self.key_dict2[g+3]+1 == self.key_dict2[g+4]:
                            if self.key_dict2[g] > self.key_dict[0]:
                                self.cache = {key_list[g]:self.choosed_poker01[key_list[g]]}
                                self.ai_prevous_card1.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+1]:self.choosed_poker01[key_list[g+1]]}
                                self.ai_prevous_card1.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+2]:self.choosed_poker01[key_list[g+2]]}
                                self.ai_prevous_card1.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+3]:self.choosed_poker01[key_list[g+3]]}
                                self.ai_prevous_card1.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+4]:self.choosed_poker01[key_list[g+4]]}
                                self.ai_prevous_card1.update(self.cache)#为{path:surface}

                                del self.choosed_poker01[key_list[g]]
                                del self.choosed_poker01[key_list[g+1]]
                                del self.choosed_poker01[key_list[g+2]]
                                del self.choosed_poker01[key_list[g+3]]
                                del self.choosed_poker01[key_list[g+4]]

                                self.cache = {key_list[g]:[self.position+1200,200]}
                                self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+1]:[self.position+1200,200]}
                                self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+2]:[self.position+1200,200]}
                                self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+3]:[self.position+1200,200]}
                                self.ai_prevous_card_point1.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+4]:[self.position+1200,200]}
                                self.ai_prevous_card_point1.update(self.cache)#为{path:position}

                                line()
                                print(self.ai_prevous_card1)
                                return True
                            else:pass
                        else:pass
                    else:return False
                else:return False

######################################################################################################################################################################

    def ai_alorithm2(self):
        self.ai_prevous_card_point2.clear()
        self.key_dict.clear()
        self.key_dict2.clear()
        key_list = list(self.choosed_poker02.keys())#path
        if self.feedback1 == False and len(self.prevous_card) != 0:
            target_key_list = list(self.prevous_card.keys())#path
            for kl in range(len(target_key_list)):
                self.cache = {kl:int(target_key_list[kl][0:2])}
                self.key_dict.update(self.cache)#path of previous_card with no (letter).png
        elif self.feedback1 == False and len(self.prevous_card) == 0 or self.passround == True and self.feedback1 == False:
            self.ai_free_hand2 = True
            target_key_list = []
        else:
            target_key_list = list(self.ai_prevous_card1.keys())#path
            for kl in range(len(target_key_list)):
                self.cache = {kl:int(target_key_list[kl][0:2])}
                self.key_dict.update(self.cache)#path of previous_card with no (letter).png

        for g in range(len(key_list)):
            self.cache = {g:int(key_list[g][0:2])}
            self.key_dict2.update(self.cache)#path of choosed_pokchoosed_poker02er01 with no (letter).png

        if self.round == 2 or self.ai_free_hand2 == True:
            self.ai_prevous_card2.clear()
            self.ai_prevous_card_point2.clear()
            ans = random.choice(list(self.choosed_poker02.keys()))
            self.cache = {ans:self.choosed_poker02[ans]}
            self.ai_prevous_card2.update(self.cache)#为{path:surface}
            del self.choosed_poker02[ans]

            self.cache = {ans:[self.position+600,200]}
            self.ai_prevous_card_point2.update(self.cache)#为{path:position}

            self.ai_free_hand2 = False
            return True
        else: 
            for g in range(len(key_list)):
                self.position = 0
                self.ai_prevous_card2.clear()
                self.ai_prevous_card_point2.clear()
                if len(self.key_dict) == 1:
                    if self.key_dict2[g] > self.key_dict[0]:
                        self.cache = {key_list[g]:self.choosed_poker02[key_list[g]]}
                        self.ai_prevous_card2.update(self.cache)#为{path:surface}
                        self.cache = {key_list[g]:[self.position+600,200]}
                        self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                        del self.choosed_poker02[key_list[g]]
                        line()
                        print(self.ai_prevous_card2)
                        return True
                    else:pass
     
                elif len(self.key_dict) == 2:
                    if g == len(key_list)-2:
                        return False
                    elif self.key_dict2[g] == self.key_dict2[g + 1]:
                        if self.key_dict2[g] > self.key_dict[0]:
                            self.cache = {key_list[g]:self.choosed_poker02[key_list[g]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker02[key_list[g+1]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}

                            self.cache = {key_list[g]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}

                            del self.choosed_poker02[key_list[g]]
                            del self.choosed_poker02[key_list[g+1]]
                            line()
                            print(self.ai_prevous_card2)
                            return True
                        else:pass
                    
                elif len(self.key_dict) == 4:
                    if g == len(key_list)-4:
                        return False
                    elif self.key_dict[0] == self.key_dict[3]:
                        if self.key_dict2[g] > self.key_dict[0]:
                            self.cache = {key_list[g]:self.choosed_poker02[key_list[g]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker02[key_list[g+1]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+2]:self.choosed_poker02[key_list[g+2]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+3]:self.choosed_poker02[key_list[g+3]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}

                            del self.choosed_poker02[key_list[g]]
                            del self.choosed_poker02[key_list[g+1]]
                            del self.choosed_poker02[key_list[g+2]]
                            del self.choosed_poker02[key_list[g+3]]

                            self.cache = {key_list[g]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}

                            line()
                            print(self.ai_prevous_card2)
                            return True
                        else:pass   

                            
                    elif self.key_dict[0] != self.key_dict[3]:
                        if self.key_dict2[g] == self.key_dict2[g+1] == self.key_dict2[g+2] and self.key_dict2[g+3] or self.key_dict2[g-1]:
                            self.cache = {key_list[g]:self.choosed_poker02[key_list[g]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+1]:self.choosed_poker02[key_list[g+1]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+2]:self.choosed_poker02[key_list[g+2]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            self.cache = {key_list[g+3]:self.choosed_poker02[key_list[g+3]]}
                            self.ai_prevous_card2.update(self.cache)#为{path:surface}
                            del self.choosed_poker02[key_list[g]]
                            del self.choosed_poker02[key_list[g+1]]
                            del self.choosed_poker02[key_list[g+2]]
                            del self.choosed_poker02[key_list[g+3]]

                            self.cache = {key_list[g]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+1]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+2]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                            self.position += 50
                            self.cache = {key_list[g+3]:[self.position+600,200]}
                            self.ai_prevous_card_point2.update(self.cache)#为{path:position}

                            line()
                            print(self.ai_prevous_card2)
                            return True
                        else:pass
                    
                elif len(self.key_dict) >= 5:
                    if self.key_dict[0]+1 == self.key_dict[1]:
                        self.straight = len(self.key_dict)
                        if self.straight > 5:
                            return False
                        else:
                            self.cursor = True
                    elif self.key_dict[0] == self.key_dict[1]:
                        self.cursor = False

                    if g == len(key_list)-5:
                        return False

                    if self.cursor == True:
                        if self.key_dict2[g]+4 == self.key_dict2[g+1]+3 == self.key_dict2[g+2]+2 == self.key_dict2[g+3]+1 == self.key_dict2[g+4]:
                            if self.key_dict2[g] > self.key_dict[0]:
                                self.cache = {key_list[g]:self.choosed_poker02[key_list[g]]}
                                self.ai_prevous_card2.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+1]:self.choosed_poker02[key_list[g+1]]}
                                self.ai_prevous_card2.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+2]:self.choosed_poker02[key_list[g+2]]}
                                self.ai_prevous_card2.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+3]:self.choosed_poker02[key_list[g+3]]}
                                self.ai_prevous_card2.update(self.cache)#为{path:surface}
                                self.cache = {key_list[g+4]:self.choosed_poker02[key_list[g+4]]}
                                self.ai_prevous_card2.update(self.cache)#为{path:surface}

                                del self.choosed_poker02[key_list[g]]
                                del self.choosed_poker02[key_list[g+1]]
                                del self.choosed_poker02[key_list[g+2]]
                                del self.choosed_poker02[key_list[g+3]]
                                del self.choosed_poker02[key_list[g+4]]

                                self.cache = {key_list[g]:[self.position+600,200]}
                                self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+1]:[self.position+600,200]}
                                self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+2]:[self.position+600,200]}
                                self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+3]:[self.position+600,200]}
                                self.ai_prevous_card_point2.update(self.cache)#为{path:position}
                                self.position += 50
                                self.cache = {key_list[g+4]:[self.position+600,200]}
                                self.ai_prevous_card_point2.update(self.cache)#为{path:position}

                                line()
                                print(self.ai_prevous_card2)
                                return True
                            else:pass
                        else:pass
                    else:return False
                else:return False

######################################################################################################################################################################

    def check_hand(self):
        self.current_card.clear()
        self.card_play_point.clear()
        # 可以试试删除字典里所有东西，然后重新写入来更新，反正是用侦测坐标来获取所选卡牌
        for e in self.card_blit_point.keys():#为{path:position}
            if self.card_blit_point[e][1] == 700:
                self.cache = {e:self.user_choosed_poker[e]}
                self.current_card.update(self.cache)#为{path:surface}
        ans = Game_algorithm.check_ranks_suits(self)
        return ans
        
######################################################################################################################################################################

    def check_ranks_suits(self):
        self.key_dict.clear()
        self.key_dict2.clear()
        key_list = list(self.current_card.keys())
        if self.feedback2 == False and self.feedback1 == False:
            self.free_hand = True
            target_key_list = []
        elif self.feedback2 == False and len(self.ai_prevous_card1) != 0:
            target_key_list = list(self.ai_prevous_card1.keys())#path
        elif self.feedback2 == False and len(self.ai_prevous_card1) == 0:
            self.free_hand = True
            target_key_list = []
        else:
            target_key_list = list(self.ai_prevous_card2.keys())#path

        for tkl in range(len(target_key_list)):
            self.cache = {tkl:int(target_key_list[tkl][0:2])}
            self.key_dict2.update(self.cache)#{num:card rank}

        for kl in range(len(key_list)):
            self.cache = {kl:int(key_list[kl][0:2])}
            self.key_dict.update(self.cache)#{num:card rank}
        #开始算法
        if self.free_hand == True:
            if len(self.key_dict) == 1:
                return True
            elif len(self.key_dict) == 2:
                if self.key_dict[0] == self.key_dict[1]:
                    return True
                elif self.key_dict[0] + self.key_dict[1] == 51:
                    return True
                else:return False
            elif len(self.key_dict) == 4:
                if self.key_dict[0] == self.key_dict[1] == self.key_dict[2] == self.key_dict[3]:
                    return True
                elif (self.key_dict[0] == self.key_dict[1] == self.key_dict[2]) or (self.key_dict[1] == self.key_dict[2] == self.key_dict[3]):
                    return True
                else:return False
            elif len(self.key_dict) >= 5:
                for num in range(len(self.key_dict)):
                    if num != len(self.key_dict)-1:
                        if self.key_dict[num] != self.key_dict[num+1]:
                            if self.key_dict[num] + 1 == self.key_dict[num + 1]:
                                pass
                        elif (self.key_dict[0] == self.key_dict[1] == self.key_dict[2] and self.key_dict[3] == self.key_dict[4]) or (self.key_dict[0] == self.key_dict[1] and self.key_dict[2] == self.key_dict[3] == self.key_dict[4]):
                            return True
                        elif len(self.key_dict)%2 == 0:
                            if num%2 == 0:
                                if self.key_dict[num] == self.key_dict[num + 1]:
                                    pass
                                else:return False
                            else:pass
                        else:return False
                    elif num == len(self.key_dict)-1:
                        if self.key_dict[num] != self.key_dict[num-1]:
                            if self.key_dict[num] - 1 == self.key_dict[num - 1]:
                                return True
                            else:return False
                        elif (self.key_dict[0] == self.key_dict[1] == self.key_dict[2] and self.key_dict[3] == self.key_dict[4]) or (self.key_dict[0] == self.key_dict[1] and self.key_dict[2] == self.key_dict[3] == self.key_dict[4]):
                            return True
                        elif len(self.key_dict)%2 == 0:
                            if self.key_dict[num] == self.key_dict[num - 1] ==  self.key_dict[num - 2] + 1:
                                return True
                            else:return False  
                        else:return False
            else:
                return False    
        elif self.free_hand == False:
            if len(self.key_dict2.keys()) == 1 and len(self.key_dict.keys()) == len(self.key_dict2.keys()):
                if self.key_dict[0] > self.key_dict2[0]:
                    return True
                else:return False
            elif len(self.key_dict2.keys()) == 2 and len(self.key_dict.keys()) == len(self.key_dict2.keys()):
                if self.key_dict[0] == self.key_dict[1] and self.key_dict[0] > self.key_dict2[0]:
                    return True
                else:return False
            elif len(self.key_dict2.keys()) == 4 and len(self.key_dict.keys()) == len(self.key_dict2.keys()):
                if self.key_dict[0] == self.key_dict[1] == self.key_dict[2] == self.key_dict[3] and self.key_dict[0] > self.key_dict2[0]:
                    return True
                elif self.key_dict2[0] != self.key_dict2[1] and self.key_dict2[2] == self.key_dict2[3] == self.key_dict2[4] or self.key_dict2[2] != self.key_dict2[3] and self.key_dict2[0] == self.key_dict2[1] == self.key_dict2[2]:
                    if self.key_dict[0] == self.key_dict[1] == self.key_dict[2] and self.key_dict[2] != self.key_dict[3] or self.key_dict[1] == self.key_dict[2] == self.key_dict[3] and self.key_dict[1] != self.key_dict[1]:
                        if self.key_dict[1] > self.key_dict2[self.key_dict2[1]]:
                            return True
                        else:return False
                    else:return False
                else:pass
            elif len(self.key_dict2.keys()) >= 5 and len(self.key_dict.keys()) == len(self.key_dict2.keys()):
                if self.key_dict2[0] == self.key_dict2[1] and self.key_dict2[2] == self.key_dict2[3] == self.key_dict2[4] or self.key_dict2[0] == self.key_dict2[1] and self.key_dict2[2] == self.key_dict2[3] == self.key_dict2[4]:
                    if self.key_dict[0] == self.key_dict[1] and self.key_dict[2] == self.key_dict[2] == self.key_dict[3] or self.key_dict[0] == self.key_dict[1] == self.key_dict[2] and self.key_dict[3] == self.key_dict[4]:
                        if self.key_dict[2] > self.key_dict2[2]:
                            return True
                        else:return False
                    else:return False
                elif self.key_dict2[0]+4 == self.key_dict2[1]+3 == self.key_dict2[2]+2 == self.key_dict2[3]+1 == self.key_dict2[4]:
                    if self.key_dict[0]+4 == self.key_dict[1]+3 == self.key_dict[2]+2 == self.key_dict[3]+1 == self.key_dict[4]:
                        if self.key_dict[0] > self.key_dict2[0]:
                            return True
                        else:return False
                    else:return False
                else:return False
    def check_winner(self):
        if len(self.choosed_poker01) == 0 or len(self.choosed_poker02) == 0:
            self.winner = False
            self.round = 0
            return self.winner

        else:pass
        if len(self.user_choosed_poker) == 0:
            self.winner = True
            self.round = 0
            return self.winner
            
        else:pass
