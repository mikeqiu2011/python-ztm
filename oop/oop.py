# OOP

class PlayerCharacter:
    def __init__(self, name) -> None:  # constructor method
        self.name = name

    def run(self):
        print('run')

p1 = PlayerCharacter('mike') # when run (), the __init__ is invoked
# p1.run()
print(p1)