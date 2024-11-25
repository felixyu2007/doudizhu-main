from menu_page import *
def refresh(round):
    screen.fill(green)
    if round == 0:
        for i in range(0,54):
            choosed_poker = random.choice(poker_data)
            if choosed_poker not in choosed_poker_data:
                choosed_poker_data.append(choosed_poker)
            else:
                pass
            return choosed_poker_data
    else:
        pass