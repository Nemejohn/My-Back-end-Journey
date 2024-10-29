'''Modules: are python file that contain python code
a file is also called a module.
'''
#built in modules
import math
import add
import substract
import task
from add import multiply
# renaming a module
import math as perform_calculation
# getting all modules in a file
from math import *
from math_utils.basic_operation import *
from math_utils.advanced_operation import div, mul

print(math.sqrt(144))
print(perform_calculation.sqrt(68))
print(add(6,5))
print(substract.substract(9,7))
print(multiply(4,5))
# task.alphabet('a')
print(add(3,4))
print(sub(10,1))
print(div(10,7))
print(mul(2,3))

'''Selecting Import'''



