def solution(num_list):
    result = 1
    for x in num_list:
        result *= x
    return 1 if result < sum(num_list)**2 else 0