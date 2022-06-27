from audioop import mul
# do not import *, be explicity to avoid name collision
from utility import sum, multiply
from shopping.more_shopping import shopping_cart

print(multiply(2, 4))

print(shopping_cart.buy('apple'))


# '__main__' is given to the specific file that we run
print(__name__)


if __name__ == '__main__':
    # only run file when this is the main file instead of a module
    print('pls run this')
