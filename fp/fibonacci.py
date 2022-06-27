# class FibGen:
#     def __init__(self, num):
#         self.cur_index = 0
#         self.num = num
#         self.x = 0
#         self.y = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.cur_index < self.num:
#             result = self.x + self.y
#             self.x = self.y
#             self.y = result

#             self.cur_index += 1
#             return result

#         raise StopIteration


# for i in FibGen(20):
#     print(i)


def fib(num):
    x = 0
    y = 1
    for i in range(num):
        result = x + y
        x = y
        y = result

        yield result


for i in fib(20):
    print(i)
