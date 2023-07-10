import random
import time
import os

def generate_sequence(dif):
    random_list = [random.randint(1, 101) for _ in range(dif)]
    return random_list

def get_list_from_user(dif):
    user_list = []
    for _ in range(dif):
        while True:
            user_number = input("Enter a number(from 1 to 100): ")
            if user_number.isdigit():
                user_list.append(int(user_number))
                break
            else:
                print("Invalid input. Please enter a number.")
    return user_list

def is_list_equal(random_list, user_list):
    if random_list == user_list:
        return True
    else:
        return False

def play(dif):
    random_list = generate_sequence(dif)
    print(random_list)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_list = get_list_from_user(dif)
    result = is_list_equal(random_list, user_list)
    if result:
        print("Good job! You win!")
        return True
    else:
        print(f'Sorry, you are lost! The list was: {random_list} ,and you type: {user_list}')
        return False
