# for loop under the hood

def special_for(iterable):
    # turn the iterable into iterable, so that we can call next
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break  # there is no item left, exit the loop


special_for([1, 2, 3])
