i = 0
while i<10:
    print(i)
    i += 1
else:  # will be executed only when there is no break!
    print('all work done!')

i = 0
while i<10:
    print(i)
    break # break the whole while/ else loop
else:
    print('all work done!') # will not be printed out

