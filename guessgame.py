import random

def generate_number(dif):
    secret_number = random.randint(1, dif)
    return secret_number

def get_guess_from_user():
    while True:
        user_choice = input('Input your choice: ')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 1 and user_choice <= 5:
                return user_choice
            else:
                print('Please choose a number between 1 and 5')
        else:
            print("can't use string")

def compare_results(secret_number, user_choice):
    if secret_number == user_choice:
        return True
    else:
        return False

def play(dif):
    secret_number = generate_number(dif)
    user_choice = get_guess_from_user()
    result = compare_results(secret_number, user_choice)
    if result:
        print("Good job! You win!")
        return True
    else:
        print(f'Sorry, you are lost! Secret number was {secret_number}')
        return False

