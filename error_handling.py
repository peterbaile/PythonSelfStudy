# error handling try-except block
try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("input is 0 which is not valid")
except ValueError:
    print("input is not a valid number")
