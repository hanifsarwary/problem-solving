# Binary Gap Problem Codility
def solution(N):
    binary_str = format(N, 'b')
    print(binary_str)
    max_count = 0
    temp_count = 0
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            if temp_count > max_count: 
                max_count = temp_count
            temp_count = 0
        else:
            temp_count += 1
    return max_count