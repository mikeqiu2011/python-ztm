# non handled errors will crash our program


while True:
    try:
        age = int(input('enter your age:\n'))
        10/age
        # explicitly raise error
        raise Exception('hey something bad happen, cut it out')
    except ValueError:
        print('Pls enter a number')
        continue
    except ZeroDivisionError:
        print('zero is not allowed')
        break
    else:
        print('thank you')
        break
    finally:
        print(f'user entered! activity logged!')  # age might not be accessible

    print('can you hear me')  # code is not reachable

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# result = sum('1', 2)  # error caught, None
# print(result)

# sum(1, 0)
