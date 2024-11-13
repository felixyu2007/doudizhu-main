from cache import *
def refresh(round):
    if started == True:
        screen.fill(green)
        if round == 0:
            for i in range(0,5):
                mixed_poker_number = random(54)
                choosed_poker = poker_data[mixed_poker_number]
                choosed_poker_data[i] = choosed_poker
                return choosed_poker_data
        else:
            pass
    else:
        pass