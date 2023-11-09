# 1285_아림이의 돌 던지기

# 돌을 던져 원하는 지점에 최대한 가깝게 돌을 던지는 게임
# 0에 가깝게 돌이 떨어진 위치

T = int(input())

for tc in range(T):
    N = int(input()) ## 돌을 던지는 사람의 수
    pos = 100000        # max
    count = 0           # min

    in_list = list(map(int, input().split()))

    for i in range(len(in_list)):
        temp = in_list[i]
        if temp < 0:
            temp *= -1

        if temp == pos:
            count += 1
        elif temp < pos:
            count = 1
            pos = temp

    print(f'#{tc+1} {pos} {count}')

## 참고) 제출은 c++만 됨