'''operators'''
# a = 5
# b = 6
# d = a + b
# print (f'the addition of a and b is {d}')
# f = a - b
# print (f'the substraction of a and b is {f}')
# c = a * b
# print (f'the multiplication of a and b is {c}')
# h = a / b
# print (f'the division of a and b is {h}')


# (Heading) Comparism Operators

# no Equal
# u = a > b
# print(f'is a greater than b... {u}')
# j = a < b
# print(f'is a lesser than b... {j}')
# p = a >= b
# print(f'is a greater than equal to b... {p}')
# o = a <= b
# print(f'is a lesser than equal to b... {o}')


# (Heading) Logical Operators
# y = 6 > 9
# z = 7 > 6
# o = 6 == 6
# m = 5 >= 3

# print (z and y)
# print (z or y)
# print (not y)
# print (o and m)


# g = 12
# g/= 6 * 3
# print (g)


# (Heading) Conditional Statement

'''if condition:
    ConnectionAbortedError
    code'''

# x = 12
# if x < 6 :
#     print('x is greater than 6')
# else :
#     print('not in alignment... Kindly recheck')


# Write a python program is the account balance is sufficient for withdrawal
'''1 -- My own work'''
# accountbalance = 20,000
# withdrawal = 15,000

# if accountbalance > withdrawal :
#     print('withdraw successful')
# else :
#     print('insufficient fund...')

'''2 -- The teachers work'''
# deposit = int (input('boss deposit your money'))
# get_cash = int (input('get cash'))
# if deposit >= get_cash:
#     print('take your money')
# else:
#     print('guy you are broke')
# balance = deposit - get_cash
# print(f'your balance is now {balance}')


'''Login Page'''
# username = input('Enter your Username ')
# password1 = int (input('Enter your Password '))
# password2 = int (input('Confirm your password '))

# if password1 == password2:
#     print('log in successful')
# else :
#     print('Please rematch your password')


# Dictionary - My biodata 

# user_biodata = {}

# user_biodata['username'] = input('input your name')
# user_biodata['state'] = input('input your state')
# user_biodata['password1'] = int(input('enter any password'))
# user_biodata['password2'] = int(input('enter same password'))
# print(user_biodata)
# if user_biodata['password1'] == user_biodata['password2']:
#     print('your biodata has been collected')
# else:
#     print('correct your password')

# write a python program to check if a number is even or odd.
# write a python code to check a student grade base on there score.
# write a python program to check is a number is positve, negative or zero.
# write a python program to check if a year is a leap year.

print('n   n')

# name = input('What is your name: ')
# age = input('How old are you: ')
# patient = input('are you a new patient ')
# summation = name + " you're " + age + " of age, and " + patient + " you're a new patient "
# print ('Hi ' + summation)

# year = int(input('What year where you born? '))
# present_year = 2024
# new_age = present_year - year
# print (new_age)


random = int(input ('add any number '))
if (random % 2) == 0:
    print("{0} is an even number".format(random))
else:
    print("{0} is an odd number".format(random))

    # OR

random = int(input ('add any number '))
if (random % 2) == 0:
    print("This number is an even number")
else:
    print("This number is an odd number")



score = int(input('input a score '))
if score >= 70 and score <= 100:
    print('A')
elif score >= 60 and score < 70:
    print('B')
elif score >= 50 and score < 60:
    print('C')
elif score >= 40 and score < 50:
    print('D')
elif score >= 0 and score < 40:
    print('F')
else:
    print('Enter a valid score')