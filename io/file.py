# using with, no need to manually close the file after read
with open('app/sad.txt', mode='w') as f:
    text = f.write(':(')
    print(text)
