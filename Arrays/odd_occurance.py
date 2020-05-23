def solution(A):
    # write your code in Python 3.6
    track_dict = dict()
    for i in A:
        if track_dict.get(i,0):
            track_dict[i] = track_dict.get(i) + 1
        else:
            track_dict[i] = 1
    for key, value in track_dict.items():
        if value % 2:
            return key 
    return 0
    