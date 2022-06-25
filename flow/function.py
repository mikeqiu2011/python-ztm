def say_hello(name, emoji):
    print(f'hello {name} {emoji}')

say_hello('mike', ':)') # position argument

say_hello(':)', 'mike') # not working

say_hello(emoji=':)', name='mike') # keyword argument, tell function explicitly

say_hello(name='mike', emoji=':)') # good practice, follow the definition order

# default parameter, increase the readbility and usability of your program
def say_hello2(name='kevin', emoji=':-|'):
    print(f'hello {name} {emoji}')

say_hello2() # hello kevin :-|
say_hello2('mike') # hello mike :-|
say_hello2('mike', ':)') # hello mike :)
say_hello2(emoji=':)') # hello kevin :)