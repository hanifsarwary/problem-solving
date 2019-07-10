def with_division(arr_list, index):
    prod = 1
    for i in arr_list:
        prod *= i

    prod = prod/arr_list[index]
    return prod


def with_out_division(arr_list, index):
    right_prod = 1
    for i in range(index+1, len(arr_list)):
        right_prod *= arr_list[i]

    left_prod = 1
    for i in range(0, index):
        left_prod *= arr_list[i]

    prod = right_prod * left_prod

    return prod


print(with_out_division([2, 4, 8], 2))
