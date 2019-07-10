def calling_function(arr_list, key):
    temp = dict()
    for i in arr_list:
        temp[str(i)] = i

    for i in arr_list:
        key = key - i
        if temp.get(str(key), None) is not None:
            return True
        else:
            key += i
    return False


print(calling_function([1, 2, 4, 5], 3))
