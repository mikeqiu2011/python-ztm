some_list = ['a','b','c','b','d','m','n','n']

def find_dup_in_list(li):
    result = []

    temp_dict = {}
    for item in li:
        if item not in temp_dict:
            temp_dict[item] = 1
        else:
            result.append(item)

    return result

print(find_dup_in_list(some_list))