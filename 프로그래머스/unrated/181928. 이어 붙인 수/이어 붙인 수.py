def solution(num_list):
    odd_list = []
    even_list = []

    for num in num_list:
        if num % 2 == 0:
            even_list.append(str(num))
        else:
            odd_list.append(str(num))

    odd_sum = int("".join(odd_list))
    even_sum = int("".join(even_list))

    return odd_sum + even_sum
