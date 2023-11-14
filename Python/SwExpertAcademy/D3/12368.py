# 12368_24시간

## 자정 0시

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    nowTime = 0

    temp = A + B

    if temp >= 24:
        nowTime = temp -24
    else:
        nowTime = temp
    print(f'#{tc+1} {nowTime}')