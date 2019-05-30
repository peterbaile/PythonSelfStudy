# Python is case-sensitive

import math

a = 3.1
flag = False
c = '*' * 10

# get user input and dynamic concatenation
# name = input("please enter your name: ")
# color = input("enter your favorite color: ")

# type conversion and type checking
d = type(str(1))

# multi-line string
course = '''Hi John,

Thank you
'''

# square bracket of a string
course = 'Python for beginners'
a = course[:]
b = type(course[0:3])

# formatted string
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
boolean = 'John' in first  # check if 'John' is a substring of first

# Math Modules
math.pow(2, 3)

# # if Statements
# is_hot = False
# is_cold = True
# if is_hot:
#     print("today is hot")
# elif is_cold:
#     print("today is cold")
# else:
#     print("today is lovely")
#
# # or(||) and(&&) not(!)

# # continue and break
# # while loop
# i = 0
# while i <= 3:
#     if i == 0:
#         continue  # creates an infinite loop because continue will ignore all remaining codes
#     if i == 1:
#         break
#     i += 1
# print(i)

# # for loop
# # forEach loop on a string
# for item in 'hello':
#     print(item)
# # forEach loop in an array
# for item in [1, 2, 3, 4]:
#     print(item)
#
# for item in range(5, 10, 1):  # starts from 5 and ends at 9 but 10 is not included, step is 1
#     print(item)

# Data Structure: lists/ matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numbers = [5, 2, 1, 7, 4, 5]
boolean = 5 in numbers  # check if 5 is in numbers
numbers = [1, 2, 3]
x, y, z = numbers

# Data Structure: tuples (immutable)
numbers = (1, 2, 3)
x, y, z = numbers  # similar to const {x,y,z} = numbers

# Dictionaries/ JSON Object
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

age = customer["age"]  # cannot use customer.age
# gender = customer["gender"]  # will report error
gender = customer.get("gender")  # will return the None Object that represents the absence of a value
gender = customer.get("gender", "male")  # gender = male, will not change customer


# functions
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")


greet_user("Peter", "Chen")
greet_user(last_name="Peter", first_name="Chen")
