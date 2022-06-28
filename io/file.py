my_file = open('test.txt')
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(my_file.read())  # content in test.txt

my_file.seek(0)  # restart the cursor from offset 0
print(my_file.read())  # blank

my_file.seek(4)  #
print(my_file.read())  # my name is mike
