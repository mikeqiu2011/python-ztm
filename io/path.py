try:
    with open('app/sad1.txt') as f:
        print(f.readlines())
except FileNotFoundError as err:
    print(err)
except IOError as err:
    print(err)
    raise err
