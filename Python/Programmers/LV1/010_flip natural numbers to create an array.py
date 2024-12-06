# 자연수 뒤집어 배열 만들기

def solution(n):
    answer = []
    stackt = []
    temp = str(n)

    for i in temp:
        stackt.append(int(i))
    answer = list(reversed(stackt))
    return answer