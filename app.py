def solution(R):
    maximum_indicator = 0
    current_size = 0
    max_depth = 0
    current_depth = 0

    for i in range(len(R)):
        if R[i] != 0:
            current_size += 1
            current_depth = R[i]
            max_depth = max(max_depth, current_depth)
        else:
            current_indicator = current_size * max_depth
            maximum_indicator = max(maximum_indicator, current_indicator)
            current_size = 0
            max_depth = 0

    return maximum_indicator

lst = [0, 2, 1, 1, 0, 4, 1]
print(solution(lst))