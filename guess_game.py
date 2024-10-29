import random
target_number = random.randint(1,100)
guess = None
while guess != target_number:
    guess = int(input('enter any number between 1 to 100... '))
    if guess < target_number:
        print ('choose a bigger number')
    elif guess > target_number:
        print ('choose a lesser number')
    elif guess == target_number:
        print (f'hurray the number guessed is {target_number}')
    else:
        print ('input a valid number')