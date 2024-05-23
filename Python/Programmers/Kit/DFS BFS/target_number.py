# 알고리즘 고득점 KIT _ 깊이/너비 우선 탐색
# 타겟 넘버

def solution(numbers, target):
    answer = 0
    array = [0]
    for i in numbers:
        temp = []
        for j in array:
            temp.append(j + i)
            temp.append(j - i)
        array = temp
    # print('array', array)
    for i in array:
        if i == target:
            answer += 1
    # print('answer', answer)
    return answer