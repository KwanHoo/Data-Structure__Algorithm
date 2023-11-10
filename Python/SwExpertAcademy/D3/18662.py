# 18662_등차수열 만들기

# abc 주어져있는데 하나의 값에 x를 더하거나 뺄 수 있음!!!


T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())

    firM = b - a
    secM = c - b

    minV = (a+c) /2

    if minV == b:
        result = 0.0
    elif minV < b:
        cha = b - minV
        result = cha
    elif minV > b:
        cha = minV - b
        result = cha
    print(f'#{tc+1} {result}')


## 뺀다는 가정하에 잘못된 풀이 (문제 잘못 이애함)
# for tc in range(T):
#     temp = list(map(int, input().split()))
#     sort_temp = sorted(temp)
#
#     a, b, c = sort_temp[0], sort_temp[1], sort_temp[2]
#     # b - a = c - b
#     fst = b-a
#     sec = c-b
#     if fst == sec:
#         result = 0
#     elif fst > sec:
#         result = fst - sec
#     elif fst < sec:
#         result = sec - fst
#
#     print(f'#{tc+1} {result}')
