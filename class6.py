import random
'''Function Statement In Python:
    It's a block of organised re-usable code.
'''

def my_name(john):
    message = f'hello {john}'
    return message

print (my_name ('John'))
print (my_name ('Mike'))
print (my_name ('Luke'))

    # OR

def my_name(john):
    print(f'hello {john}')
    return 

my_name ('John')
my_name ('Peter')
my_name ('Saint')


def add(a,b):
    sum = a + b
    return sum
print (add (10,9))

# write a function that checks for even number
# write a function that sums all the numbers in a list
# Function that gets the maximum number in a list
# calculate the area of a circle using function
# write a function to find the common difference between two (2) list
# A function that performs a rolling dile in a game 

# numbers = 11
# def random_number(numbers):
#     number = range(10)
#     return number
#     print(f'{(numbers % 2 == 0)} This is an even number')
# else: 
# print(f'{(numbers % 2 == 0)} This ia an odd number')


number = 12
def is_even(number):
    if number % 2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is an odd number')
    
is_even(9)

def area_of_circle (radius):
    pi = 3.142
    return pi * radius**2

print (area_of_circle(7))

def common_diff(list1, list2):
    return list(set(list1) & set(list2))
print(common_diff([1,4,5], [3,4,5]))

def dice_roll():
    return random.randint(1,6)

print(dice_roll())


def looper():
    list_of_item = ['iphone11', '#20', '1harmstar', '#1,000,000']
    return random.choice(list_of_item)
print (looper())


# def shop():
#     cash_at_hand = 100
#     item_price = int(input('price of item in dollars__ '))
#     if cash_at_hand >= item_price:
#         balance = cash_at_hand - item_price
#         print(f'Transaction gone, Balance is ${balance}')
#     else:
#         print(f'Please kindly fund your wallet, Balance is ${balance}')

# shop()

user = {'username': 'john'}

def registration_of_user():
    user['username'] = input('enter your user name ')
    if user == user:
        print ('username already exist')
        user['username'] = input('enter a new username ')
        user['password'] = input('enter password ')
    else:
        print('registration done')
    
registration_of_user()

# second assignment: A Calculator


def calculator():
    option = input('''Select an operator:                 
plus - for Addition
take_away - for Substraction
multiply - for Multiplication
divide - for Division
square - for square 
    ''')
    num1 = float(input('enter first number '))
    num2 = float(input('enter second number '))
    if option == 'plus':
        addition = num1 + num2
        print(f'{num1} + {num2} is equal {addition}')
    elif option == 'take_away':
        sub = num1 - num2
        print(f'{num1} - {num2} is equal {sub}')
    elif option == 'multiply':
        multi = num1 * num2
        print(f'{num1} x {num2} is equal {multi}')
    elif option == 'divide':
        divide = num1 / num2
        print(f'{num1} / {num2} is equal {divide}')
    elif option == 'square':
        square = num1**num2
        print(f'The square of {num1} is equal {square}')
    else:
        print('Kindly enter a valid operator')

calculator()
print (eval(input('enter ')))


