# 문제집) Python 배우기 (1~50)
## 10214_Baseball
# 브론즈 3

## 주어진 실황 기록문서에서 어떤 팀이 이겼는지를 알아내는 프로그램

T = int(input())

for _ in range(T):
    ys = 0
    ks = 0
    for _ in range(9):
        y, k = map(int, input().split())

        ys += y
        ks += k
    if ys == ks :
        print("Draw")
    elif ys > ks:
        print("Yonsei")
    elif ys < ks:
        print("Korea")