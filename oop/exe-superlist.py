class Superlist(list):
    def __len__(self) -> int:
        return 1000


li = Superlist()
li.append('a')
li.append('b')
li.append('c')

print(li)
print(li[0])
print(len(li))  # returns 1000 now

print(issubclass(Superlist, list))  # True
