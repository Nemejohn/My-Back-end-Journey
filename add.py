def addition(a,b):
    return(print(a + b))
addition(4 , 5)

def multiply(a,b):
    return(print(a * b))
multiply(3 , 2)

# matrix = [
#     [1, 2, 4],
#     [3, 5, 7],
#     [9, 8, 6]
# ]
# for row in matrix:
#     for items in row:
#         print(items * 3 / 4 * 29)

patient_name = 'John Smith'
patient_age = '20 yrs'
is_new = True
name = input('enter name here... ')
age = (input('enter your age... '))
long_stayed = input('are you new or not... ')
if long_stayed == is_new:
    print(name +" you're a new patient and you're "+ age)
else:
    print(f"{name} you're an odd patient and you're {age}")
