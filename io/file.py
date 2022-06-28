# using with, no need to manually close the file after read
with open('test.txt', mode='r+') as f:
    print(f.readlines())
    text = f.write('hi, it is me!!')
    print(text)
