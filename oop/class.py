class PlayerCharacter:
    # Class Attribute
    membership = True # static
    def __init__(self, name) -> None:  # constructor method
        self.name = name # property

    def run(self):
        print('run')

p1 = PlayerCharacter('mike') # when run (), the __init__ is invoked
p2 = PlayerCharacter('kevin')

print(p1.name)
print(p2.name)

p1.run()

p2.attack = 50
print(p2.attack)  # 50

print(p1.membership) # True