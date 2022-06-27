class MyRange:
    def __init__(self, first, last) -> None:
        self.current = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num

        raise StopIteration  # there is no item left, stop iteration


for i in MyRange(0, 100):
    print(i)
