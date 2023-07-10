import random

def get_money_interval(dif):
    money_rate = random.uniform(3.2, 3.7)
    print(f'USD rate: {money_rate}')
    sum_dol = random.randint(1, 100)
    print(f'amount of USD: {sum_dol}')
    usd_to_ils = sum_dol*money_rate
    money_interval = (usd_to_ils-(5-dif), usd_to_ils+(5-dif))
    return money_interval


def get_guess_from_user():
    while True:
        guess_from_user = input('How much ILS is it: ')
        if guess_from_user.isdigit():
            return int(guess_from_user)
        else:
            print('Invalid input.Only numbers')
#
def play(dif):
    money_interval = get_money_interval(dif)
    guess_from_user = get_guess_from_user()
    if money_interval[0] <= guess_from_user <= money_interval[1]:
        print("Good job! Your answer is correct")
        return True
    else:
        print("Sorry, it's incorrect answer")
        return False