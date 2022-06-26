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

    def check_arrows(self):
        print(f'{self._num_arrows} arrows left!')

    def run(self):
        print('ran very fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows) -> None:
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


hb = HybridBorg('simon', 20, 100)
hb.attack()
# hb.check_arrows()
