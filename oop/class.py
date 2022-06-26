class PlayerCharacter:
    # Class Attribute
    membership = True # static
    def __init__(self, name) -> None:  # constructor method
        if self.membership:
            self.name = name # property

    def shout(self):
        print(f'my name is {self.name}')

p1 = PlayerCharacter('mike') # when run (), the __init__ is invoked
p2 = PlayerCharacter('kevin')

print(p1.name)
print(p2.name)

p1.shout()

p2.attack = 50
print(p2.attack)  # 50

print(p1.membership) # True
p1.membership = False
print(p1.membership) # changed to False
print(p2.membership) # still True
