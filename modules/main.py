from audioop import mul
# do not import *, be explicity to avoid name collision
from utility import sum, multiply, max
from shopping.more_shopping import shopping_cart

print(multiply(2, 4))

print(shopping_cart.buy('apple'))

# print(max([1, 2, 3])) # name collision
