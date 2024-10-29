import math 
# Create a function that squares a number
# Create a function that finds the average of the list of numbers
# Create a function that reverses a list
# Create a function that convert a string to a uppercase
# Create a function that removes a duplicate from a list
# Create a function that joins two list
# Create a quiz game using function
# Create a function that allows user to register, login and logout

'''Here is a code of a function that squares a number'''
def number_to_be_squared():
    integer = float(input('enter a number '))
    result = integer**2
    print(f'The square of {integer} is equal {result}')
number_to_be_squared()
# or

def sqr(x):
    print(x * x)
sqr(10)


'''The average number of a list'''
def average_list(list):
    average = sum(list) / len(list)
    print(f'The average of {list} is equal {average}')
average_list([0,1,2,3,4])


'''Reversing a list'''
def reverse(list):
    print(list[::-1])
    return
reverse([1,2,3,4,5])


'''Converting a string to uppercase'''
def strings():
    string = input('enter any string ').upper()
    return (print(string))
strings()


'''Remove a duplicate for a list'''
def dup_removal(list_1):
    set1 = set(list_1)
    print(list(set1))
    return

dup_removal([1,2,2,3,4,5,5,6,7,8,8])


'''Joining two list'''
def combine(list1, list2):
    print(set(list1) | set(list2))
    return

combine([1,2,3,4,5], [6,7,8,9,10])


'''Quiz Game'''
def quiz_game():
    first_question = input('''Choose the correct answer:
Q.1 Full meaning of HTML is ____
a.) Hyper Text Markup Language.
b.) Hollow Text Mark Language.
c.) Hpper Text Markup Language.
d.) Hyper Text Markdown Language.
''')
    if first_question == 'a':
        print('Excellent, answer is (a.) Hyper Text Markup Language. (1 of 3)')
    elif first_question == 'b':
        print(f"Wrong answer !!! You chose '{first_question}' the correct answer is (a.) Hyper Text Markup Language.")
    elif first_question == 'c':
        print(f"Wrong answer !!! You chose '{first_question}' the correct answer is (a.) Hyper Text Markup Language.")
    elif first_question == 'd':
        print(f"Wrong answer !!! You chose '{first_question}' the correct answer is (a.) Hyper Text Markup Language.")
    else:
        print('Enter a valid option')

    second_question = input('''Q.2 Capital of Lagos is ____
a.) Abuja.
b.) Ikeja.
c.) Delta.
d.) Imo.
''')
    if second_question == 'a':
        print(f"Wrong answer !!! You chose '{second_question}' The correct answer is (b.) Ikeja.")
    elif second_question == 'b':
        print('Excellent, answer is (b.) Ikeja.')
    elif second_question == 'c':
        print(f"Wrong answer !!! You chose '{second_question}' The correct answer is (b.) Ikeja.")
    elif second_question == 'd':
        print(f"Wrong answer !!! You chose '{second_question}' The correct answer is (b.) Ikeja.")
    else:
        print('Enter a valid option')
    
    third_question = input('''Q.3 The server side is called the ____
a.) Backup.
b.) Frontend.
c.) Frontside
d.) Backend.
''')
    if third_question == 'a':
        print(f"Wrong answer !!! You chose '{third_question}' The correct answer is (d.) Backend.")
    elif third_question == 'd':
        print('Excellent, answer is (b.) Ikeja.')
    elif third_question == 'b':
        print(f"Wrong answer !!! You chose '{third_question}' The correct answer is (d.) Backend.")
    elif third_question == 'c':
        print(f"Wrong answer !!! You chose '{third_question}' The correct answer is (d.) Backend.")
    else:
        print('Enter a valid option')
    
    overall_answer = {'a, b, d'}
    if [first_question, second_question, third_question] == overall_answer:
        return(print('Congratulations you scored all three answers.'))
quiz_game()