class PlayerCharacter:
    # Class Attribute
    membership = True  # static, not change for different obj

    def __init__(self, name='anonymous', age=0) -> None:  # constructor method
        self.name = name  # object property, dynamic for different obj
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


# class method does not require instance
print(PlayerCharacter.adding_things(3, 4))
# p1 = PlayerCharacter('tom', 10)  # when run (), the __init__ is invoked
# # adding_things() takes 2 positional arguments but 3 were given
# print(p1.adding_things(2, 3))
