import random
# create a function that picks a random item from a list
# create a function that checks if a number is even or odd
# create a function that gives the cube of a number
# create a function that checks if a letter is vowel or consonant

def shopping_cart():
    list_items = ['iPhone 15pro', 'Table water', 'Football', 'Table-tennis', 'Biscuit']
    return random.choice(list_items)
print(shopping_cart())

def even_odd_numbers(number):
    if number % 2 ==0:
        return(print(f'{number} is an even number'))
    else:
        print(f'{number} is an odd number')
even_odd_numbers(15)

def alphabet():
    vowel = ['a', 'e', 'i', 'o', 'u']
    value = input('enter any letter ')
    if value in vowel:
        print(f'{value} is a vowel letter')
    else :
        print(f'{value} is a consonant letter.')
alphabet()