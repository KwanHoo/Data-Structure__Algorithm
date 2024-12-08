# 하샤드 수

## 하샤드 수 : x의 자리수의 합으로 x가 나누어져야함

def solution(x):
    answer = True
    temp = 0

    for i in str(x):
        temp += int(i)
    print(temp)

    if (x % temp) != 0:
        answer = False

    return answer