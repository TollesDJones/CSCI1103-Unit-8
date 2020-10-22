import random
import math

# UNIT 7 EXAMPLES REVIEW
#
# print("Hello World!")
# a=10
# b=50
#
# print(a+b) # <-- This is a statement
#
# if a < b:
#     print(a, " is less than ", b) # <-- Notice the indentation this is how python
#                                   # understands where statements start and stop
#
# print("This is text ")
#
# print("!!!") # <-- This is function python has many builtin functions but you can also create your own.





# UNIT 8 MATERIAL & EXAMPLES

"""
STRINGS
"""

# "string"
# "500"
#
# "500" + "500"
# "500500"
# "1000"
#
# sum = "500" # String
# num = "500" # String
#
# print(int(num) + int(sum)) # Cast to Integer
#
# num1 = 300
# num2 = 300
# print(str(num1) + str(num2)) # Cast to String



"""
VARIABLES & CONSTANTS 
"""

# COLORS = ["blue", "red", "green"]
#
# PI = 3.14
# PI = 14.3


"""
INPUTS & OUTPUTS
"""


#
# name = input('Enter student\'s name: ')
# grade1 = float(input('Enter the 1st test grade: '))
# grade2 = float(input('Enter the 2nd test grade: '))
# grade3 = float(input('Enter the 3rd test grade: '))
#
#
# sum_grades = grade1 + grade2 + grade3
# average_grade = sum_grades / 3
#
#
# print('The average test score for', name, 'is', average_grade)




"""
COMMENTS 

"""

# single line
# /* */
# Multi Line
"""
//////// """"""" '''''''
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |  ____  ____  | || |   ______     | || |  _________   | |
| | |  _   _  |  | || | |_  _||_  _| | || |  |_   __ \   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |   \ \  / /   | || |    | |__) |  | || |   | |_  \_|  | |
| |     | |      | || |    \ \/ /    | || |    |  ___/   | || |   |  _|  _   | |
| |    _| |_     | || |    _|  |_    | || |   _| |_      | || |  _| |___/ |  | |
| |   |_____|    | || |   |______|   | || |  |_____|     | || | |_________|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
"""
# Escape Sequences
#print("Line1\tLine2\n\'Line3\'\\")






"""
MATH OPERATORS 
()  Parenthesis 
+   Addition 
-   Subtraction 
*   Multiplication
/   Division (True)
//  Division (integer)
%   Modulus
**  Exponent
"""
exp = 3**3
print(exp)

division = 10/3
print(division)

intDiv = 10//3
print(intDiv)

mod = 10%2
print(mod)

stringA = "." * 10 # Python Only
print(stringA)

print(math.pi)

print(math.pow(3, 3))