def recursive_function(store, d_store, key, count, init_key):

    if len(d_store) != 0 and d_store.get(str(key+1)) is not None:
        count = count+d_store.get(str(key+1))
        return count
    elif store.get(str(key+1)) is not None:

        return recursive_function(store, d_store, key+1, count+1, init_key)

    else:
        d_store[str(init_key)] = count
        return count


def calling_function(arr_list):
    store = dict()
    dynamic_store = dict()
    for arr in arr_list:
        store[str(arr)] = arr
    max = 0
    for k in store:
        value = store.get(k)
        count = 1
        count = recursive_function(store, dynamic_store, value, count, value)

        if count > max:
            max = count

    return max


print(calling_function([6, 1, 5, 4]))
