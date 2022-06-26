class Cat:
    species = 'mammal'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('tom', 1)
cat2 = Cat('jerry', 3)
cat3 = Cat('kate', 2)

cats = []
cats.append(cat1)
cats.append(cat2)
cats.append(cat3)


# 2 Create a function that finds the oldest cat
def oldest_cat(cats):
    result = cats[0]

    for cat in cats:
        if cat.age > result.age:
            result = cat

    return result


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = oldest_cat(cats)

print(f'the oldest cat is {oldest_cat.age} years old')
