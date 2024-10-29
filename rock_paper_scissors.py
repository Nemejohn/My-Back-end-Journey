import random
choice = ['rock ', 'paper ', 'scissors ']
players_choice = None
while players_choice != 'quit':
    players_choice = input('enter rock, paper or scissors (or quit)... ').lower()
    if players_choice == "quit":
        break
    computer_choice = random.choice(choice)
    print (f'computer chose {computer_choice}')
    if players_choice == computer_choice:
        print ('there is a Tie')
    elif players_choice == 'rock' and computer_choice == 'scissors' or players_choice == 'scissors' and computer_choice == 'papper'  or players_choice == 'papper' and computer_choice == 'rock':
        print ('You won.')
    else:
        print ('You lose.')