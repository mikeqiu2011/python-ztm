class PlayerCharacter:
    # Class Attribute
    membership = True # static, not change for different obj
    def __init__(self, name='anonymous', age=0) -> None:  # constructor method
        if age > 18:
            self.name = name # object property, dynamic for different obj
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

p1 = PlayerCharacter('tom', 10) # when run (), the __init__ is invoked

print(p1.name) # object has no attribute 'name'



