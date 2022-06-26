class Toy():
    def __init__(self, color, age) -> None:
        self._color = color
        self._age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self) -> str:
        return f'color is {self._color}, age is {self._age}'

    def __len__(self) -> int:
        return len(self._color)

    def __del__(self) -> None:
        print('deleted!')

    def __call__(self):
        return 'yess??'

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 1)

# by default, it returns the obj's memory location
print(action_figure.__str__())
# you can rewrite the __str__ to return the customized string you want
print(str(action_figure))

print(len(action_figure))

print(action_figure())  # object can be called after your define the __call__

print(action_figure['name'])  # yoyo
# del action_figure  # not recommended to use
