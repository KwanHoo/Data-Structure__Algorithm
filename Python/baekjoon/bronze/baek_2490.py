# 백준 _바킹독 기초코드 작성요령 2
# 2490번 : 윷놀이
# 브론즈 3

## 배 : x 0, 등 - 1
## 도 x--- A
## 개 xx-- B
## 걸 xxx- C
## 윷 xxxx D
## 모 ---- E

T = 3

for _ in range(T):
    numl = list(map(int, input().split()))

    countx = 0
    for i in range(len(numl)):
        if str(numl[i]) == '0':
            countx += 1

    if countx == 0:
        print('E')
    elif countx == 1:
        print('A')
    elif countx == 2:
        print('B')
    elif countx == 3:
        print('C')
    elif countx == 4:
        print('D')