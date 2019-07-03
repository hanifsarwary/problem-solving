
def search_in_sorted(array_list, item):
    first = 0

    last = len(array_list)-1
    found = False
    while(first <= last and not found):
        mid = (first + last)//2
        if array_list[mid] == item:
            found = True
            return mid
        else:
            if item < array_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return None


print(search_in_sorted([1, 2, 3, 4, 5, 6], 6))
