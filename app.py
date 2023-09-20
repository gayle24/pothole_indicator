def solution(R):
    maximum_indicator = 0
    current_size = 0
    max_depth = 0

    for i in range(len(R)):
        if R[i] != 0:
            pass
            current_size += 1
            max_depth = R[i]
        else:
            current_indicator = current_size * max_depth
            maximum_indicator = max(maximum_indicator, current_indicator)
            current_size = 0
            max_depth = 0

    return maximum_indicator

lst = [1,2,4,0,0,2,0,5,0]
print(solution(lst))