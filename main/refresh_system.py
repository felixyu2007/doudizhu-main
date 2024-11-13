from cache import *
def refresh(round):
    while started == True:
        if round == 0:
            for i in range(5):
                mixed_poker_number = random(54)
                choosed_poker = poker_data[mixed_poker_number]
                choosed_poker_data = choosed_poker
                screen.blit(choosed_poker,cards_points[i])
        else:
            pass
    else:
        pass