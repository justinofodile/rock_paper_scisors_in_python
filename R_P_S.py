import random

user_win = 0
computer_win = 0
ties = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Rock, Paper, Scissors or Q to Quit? ").lower()
    if user_input == 'q':
        break
    elif user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_picked = options[random_number]
    print(f'Computer picked {computer_picked}')

    if user_input == 'rock' and computer_picked == 'paper':
        print("You won!")
        user_win += 1
    elif user_input == 'paper' and computer_picked == 'scissors':
        print("You won!")
        user_win +=1
    elif user_input == 'scissors' and computer_picked == 'rock':
        print("You won!")
        user_win +=1
    elif user_input == computer_picked:
        print("There is a tie!")
        ties += 1
    else:
        print("Computer won!")
        computer_win += 1
print("You won {} times. Weldone".format(user_win))
print("Computer won {} times. Try harder next time".format(computer_win))
print("Computer and user had {} times".format(ties))

