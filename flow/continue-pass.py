my_list = [1,2,3]

for item in my_list:
    print(item)
    break  # works in for as well

for item in my_list:
    if item == 2:
        continue
    print(item)


for i in range(10):
    for j in range(5):
        if j == 3:
            break # break current level of loop, back to parent loop
        print(j)

for i in range(10):
    for j in range(5):
        if j == 3:
            continue # continue to next item of current loop
        print(j)

for i in range(10):
    pass  # a place holder before you start the work
