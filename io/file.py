# using with, no need to manually close the file after read
with open('test.txt', mode='a') as f:
    text = f.write(':)')
    print(text)
