def solution(name, yearning, photo):
    answer = []
    for pic in photo:
        score = 0
        for person in pic:
            if person in name:
                index = name.index(person)
                score += yearning[index]
        answer.append(score)
    return answer