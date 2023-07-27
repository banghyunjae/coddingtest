def solution(num_list):
    k = num_list[-1]
    j = num_list[-2]
    if k > j:
        num_list.append(k-j)
    else:
        num_list.append(k*2)
    return num_list