my_file = open('test.txt')
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(my_file.readlines())  # ['hi, my name is mike\n', ':)\n', 'how are you']

my_file.close()
