# non handled errors will crash our program


# while True:
#     try:
#         age = int(input('enter your age:\n'))
#         10/age

#     except ValueError:
#         print('Pls enter a number')
#     except ZeroDivisionError:
#         print('zero is not allowed')
#     else:
#         print('thank you')
#         break


def sum(num1, num2):
    return num1 + num2


result = sum('1', '2')  # '12' !!
print(result)
