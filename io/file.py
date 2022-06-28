# using with, no need to manually close the file after read
with open('sad.txt', mode='w') as f:
    text = f.write(':(')
    print(text)
