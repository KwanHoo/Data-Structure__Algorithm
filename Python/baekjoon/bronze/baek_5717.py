# 문제집) Python 배우기 (1~50)
## 5717_상근이의 친구들
# 브론즈 4

endbreak = True

while endbreak:
    M, F = map(int, input().split())

    if M == 0 and F == 0:
        endbreak = False
        break

    result = M + F

    print(result)