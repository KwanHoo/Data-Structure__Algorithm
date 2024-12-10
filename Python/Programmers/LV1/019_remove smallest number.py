# 제일 작은 수 제거

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]

def solution2(arr):
    answer = []
    arr.sort(reverse=True)
    temp = arr[-1]
    arr.remove(temp)

    if len(arr) == 0:
        arr.append(-1)
    answer = arr
    return answer