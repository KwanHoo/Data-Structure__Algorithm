# 평균구하기


def solution(arr):
    answer, sumt = 0, 0
    for i in range(len(arr)):
        sumt += arr[i]
    answer = sumt / len(arr)
    return answer