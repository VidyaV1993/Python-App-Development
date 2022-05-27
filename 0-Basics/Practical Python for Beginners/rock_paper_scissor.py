import random

list1 = ['scissors', 'rock', 'paper']
computer_choice = random.choice(list1)

user_choice = input('Do you want - rock, paper or scissors?\n')

if computer_choice == user_choice:
    print('TIE')
    print('Computer choice was ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
    print('Computer choice was ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
    print('Computer choice was ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')
    print('Computer choice was ' + computer_choice)
else:
    print('You lose :( Computer wins :D')
    print('Computer choice was ' + computer_choice)
