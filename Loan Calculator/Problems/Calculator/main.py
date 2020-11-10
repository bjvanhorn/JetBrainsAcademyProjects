# Previous attempt at 'cleaning' code to make the linter happy
#
# def addition(x, y):
#     print(x + y)
#
#
# def subtraction(x, y):
#     print(x - y)
#
#
# def division(x, y):
#     if not is_zero(y):
#         print(x / y)
#
#
# def multiplication(x, y):
#     print(x * y)
#
#
# def modulus(x, y):
#     if not is_zero(y):
#         print(x % y)
#
#
# def raise_to_power(x, y):
#     print(x ** y)
#
#
# def integer_division(x, y):
#     if not is_zero(y):
#         print(x // y)
#
#
# def is_zero(x):
#     if x == 0.0:
#         print("Division by 0!")
#         return True
#     else:
#         return None
#
#
# first_number, second_number, operation = float(input()), float(input()), input()
#
# if operation == '+':
#     addition(first_number, second_number)
# elif operation == "-":
#     subtraction(first_number, second_number)
# elif operation == "/":
#     division(first_number, second_number)
# elif operation == "*":
#     multiplication(first_number, second_number)
# elif operation == "mod":
#     modulus(first_number, second_number)
# elif operation == "pow":
#     raise_to_power(first_number, second_number)
# elif operation == "div":
#     integer_division(first_number, second_number)

first_number, second_number, operation = float(input()), float(input()), input()

if operation in ['/', 'mod', 'div'] and second_number == 0.0:
    print("Division by 0!")
elif operation == '+':
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "mod":
    print(first_number % second_number)
elif operation == "pow":
    print(first_number ** second_number)
elif operation == "div":
    print(first_number // second_number)
