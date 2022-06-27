# non handled errors will crash our program


while True:
    try:
        age = int(input('enter your age:\n'))
        print(age)

    except:
        print('Pls enter a number')
    else:
        print('thank you')
        break
