import bgdata
import random
import os

poker_image_path = r'PNG-cards-1.3'
imgs = os.listdir(poker_image_path)
poker_data = []
choosed_poker_data = []

class Game_algorithm():
    def __init__(self):
        for p in imgs:
            poker_data.append(p)
    def run():
        if round == 0:
            bgdata.poker_data
    # if card_sended == False:
    #     rs.draw_refreshed()
    #     if start_coordinate[0] <= end_coordinate[0] or start_coordinate[1] <= end_coordinate[1]:
    #         screen.blit(cardback,(900,200))
    #         start_coordinate[0] += distance[0]*10
    #         start_coordinate[1] += distance[1]*10
    #         screen.blit(cardback,(start_coordinate[0],start_coordinate[1]))
    #     else:
    #         screen.blit(cardback,(900,200))
    #         keep_show.append('i')
    #         last_coordinate[0] = start_coordinate[0]
    #         last_coordinate[1] = start_coordinate[1]
    #         start_coordinate = [900,200]
    #         end_coordinate = [1100,600]
    #         round += 1
    #         if keep_show[17] == 'i':
    #             quit
    #     if round != 0:
    #     screen.blit(cardback,(last_coordinate[0],last_coordinate[1]))
if __name__ == '__main__':
    Game_algorithm()
    print(poker_data)