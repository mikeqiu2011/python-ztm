class User():
    def __init__(self, name) -> None:
        self._name = name

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power) -> None:
        super().__init__(name)
        self._power = power

    def attack(self):
        # User.attack(self)
        super().attack()
        print(f'attack with power {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows) -> None:
        super().__init__(name)
        self._num_arrows = num_arrows

    def attack(self):
        print(f'attack!, now have {self._num_arrows} arrows left!')
        self._num_arrows -= 1


wizard1 = Wizard('gandof', 10)
archer1 = Archer('Robin', 30)

# print(isinstance(wizard1, Wizard))  # True
# print(isinstance(wizard1, User))   # True
# print(isinstance(wizard1, object))   # True
# print(isinstance(wizard1, Archer))  # False

# wizard1.sign_in()
# wizard1.attack()

# archer1.sign_in()
# archer1.attack()
# archer1.attack()

# Polymorphism


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

# object introspection
print(dir(wizard1))
