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


print(array_rotation([1, 2, 3, 4, 5], 2))
