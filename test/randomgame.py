import sys
import random

min = 1
max = 10


def check_answer(answer, target):
    if 1 < answer < 10:
        if answer == target:
            print('correct!')
            return True
        elif answer > target:
            print('too big!')
        else:
            print('too small')

        return False
    else:
        print('number exceed range')
        return False


def guess_a_num(min, max):
    target = random.randint(min, max)
    count = 0
    while True:
        try:
            answer = int(
                input(f'guess a number between {min} and {max} pls \n'))

            if check_answer(answer, target):
                break

            count += 1
            print(f'you guessed {count} times')
        except ValueError:
            print('must be a number')


if __name__ == '__main__':
    guess_a_num(min, max)
