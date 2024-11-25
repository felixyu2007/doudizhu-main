from menu_page import *
def refresh(round):
    screen.fill(green)
    if round == 0:
        mixed_poker_number = random.randint(0,53)
        choosed_poker = poker_data[mixed_poker_number]
        choosed_poker_data.append(choosed_poker)
        print(choosed_poker)
        return choosed_poker_data
    else:
        pass