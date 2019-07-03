import time


def array_rotation(array_list, rotation_count):
    start_time = time.time()

    try:
        for i in range(0, rotation_count):
            last_element = array_list[-1]
            for j in range(2, len(array_list)+1):
                array_list[-j+1] = array_list[-j]
            array_list[0] = last_element

    except:
        pass
    print("--- %s seconds ---" % (time.time() - start_time))
    return array_list


def array_rotation_recursive(array_list, rotation_count):

    if rotation_count == 0:
        return array_list

    last_element = array_list[-1]
    for j in range(2, len(array_list)+1):
        array_list[-j+1] = array_list[-j]
    array_list[0] = last_element

    return array_rotation_recursive(array_list, rotation_count-1)


print(array_rotation_recursive([1, 2, 3, 4, 5], 10))

# the same code can be used for reversing array by passing len(array_list) as rotation count
