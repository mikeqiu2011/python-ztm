def highest_even(li):
    sorted_li = sorted(li, reverse=True)
    for item in sorted_li:
        if item % 2 == 0:
            return item

print(highest_even([10,2,20,4,8])) # shall be 20