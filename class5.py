'''Loop'''
'''Types of loop'''
'''* for loop'''
'''* while'''
# for variable in sequence:

names = ['Bola', 'Tunde', 'Neme']
for name in names:
    print(f'hello {name}')
strings = 'bola'
for letters in strings:
    print(letters)
for numbers in range(1, 10):
    print(numbers)


person = {'name' : 'bola', 'age' : 40,}
for key, value in person.items():
    print(f'{key}: {value}')

for anum in range(1, 10):
    if (anum % 2) == 0:
        print(anum)

'''While'''
'''While condition:
        code to be executed'''


# Write a guessing Game

'''count = 100
while count >= 1:
    print(count)
    count -= 1'''

# secret_number = 54
# guess = 0
# while guess 54 = secret_number
#    print()

'''temperature = int(input('Enter your temperature... '))
if temperature > 30 and temperature <= 100:
    print ("it's a hot day, try to get cold.")
elif temperature < 10:
    print ("it's a cold day, take some coffee.")
else:
    print ("it's neither hot nor cold.")

name = input('enter your full name: ')
if name < int(3):
    print ('name must be at least 3 characters.')'''


for python in range(10):
    print ('I love Python')

my_bio = {'name' : 'John', 'age' : '25 years', 'state' : 'Anambra State'}
for key, value in my_bio.items():
    print (f' {key} is {value}')

for random in range (100):
    if random % 2 == 0:
        print (random)


# no.2  nested loops are loops in another loop

classes = ['class1', 'class2', 'class3',]
students = ['student1', 'student2', 'student3']
for classs in classes:
    for rep in students:
        print (classs , rep)

grade_a = ['A1', 'A2', 'A3',]
grade_b = ['B1', 'B2', 'B3']
grade_c = ['C1', 'C2', 'C3']
for grade1 in grade_a:
    for grade2 in grade_b:
        for grade3 in grade_c:
            print (grade1 , grade2, grade3)


'''time_table = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]
multple_six = [ 6 ]
for tables in time_table:
    for times_six in multple_six:
        print (tables * times_six)'''

for number in range (1,6):
    for num in range (1,6):

        product = number * num
        print (f'{number} * {num} = {product}')
        print ()


records = [
    {'user_name' : 'Neme', 'password' : 22466,},
    {'user_name' : 'John', 'password' : 55667,},
    {'user_name' : 'Chuks', 'password' : 33445,},
]
for record in records:
    for key, value in record.items():
        print (f'{key} : {value}')

for number in range(1,5):
    if number == 4:
        break
    print (number)

digits = 0
while digits < 13:
    print (digits)
    digits += 1

