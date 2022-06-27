# non handled errors will crash our program


while True:
    try:
        age = int(input('enter your age:\n'))
        10/age

    except:
        print('Pls enter a number')
    else:
        print('thank you')
        break
