my_file = open('test.txt')
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(my_file.read())  # content in test.txt
print(my_file.read())  # blank
print(my_file.read())  # blank, but why?
