# 나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    answer = []
    templ = []
    for i in range(len(arr)):
        temp = arr[i]

        if (temp % divisor) == 0:
            templ.append(temp)
    print(templ)
    templ.sort()
    if len(templ) == 0:
        answer.append(-1)
    else:
        answer = templ
    return answer
