# 문제집) Python 배우기 (1~50)
## 2525_오븐 시계
# 브론즈 3

A, B = map(int, input().split())
C = int(input())

rT = 0
rM = 0

if B+C >59:
    rM = (B+C) %60
    temp = (B+C) //60
    rT = A+temp
    if rT >23:
        rT = rT-24
else:
    rM = B+C
    rT = A

print(rT, rM)