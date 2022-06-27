# non handled errors will crash our program


while True:
    try:
        age = int(input('enter your age:\n'))
        10/age

    except ValueError:
        print('Pls enter a number')
        print(age)
    except ZeroDivisionError:
        print('zero is not allowed')
    else:
        print('thank you')
        break
    finally:
        print(f'user entered {age}! activity logged!')


# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# result = sum('1', 2)  # error caught, None
# print(result)

# sum(1, 0)
