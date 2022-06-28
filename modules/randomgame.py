import sys
import random

min = int(sys.argv[1])
max = int(sys.argv[2])

# print(min, max)

target = random.randint(min, max)
# print(target)
count = 0
while True:
    try:
        answer = int(input(f'guess a number between {min} and {max} pls \n'))
        if answer == target:
            print('correct!')
            break
        elif answer > target:
            print('too big!')
        else:
            print('too small')

        count += 1
        print(f'you guessed {count} times')
    except ValueError:
        print('must be a number')