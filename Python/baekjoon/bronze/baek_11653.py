# 문제집) Python 배우기 (1~50)
## 11653_소인수분해
# 브론즈 1

## 소인수 분해 프로그램 만들기

N = int(input())

s = 2

while N != 1:
    # 나머지 0
    if N%s == 0:
        print(s)
        N = N/s
    else:
        s += 1
