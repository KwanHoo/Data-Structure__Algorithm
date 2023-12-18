# 문제집) Python 배우기 (1~50)
## 2476_주사위 게임
# 브론즈 3


T = int(input())
maxV = 0

for tc in range(T):
    F, S, T = map(int, input().split())

    if F == S == T:
        result = 10000 + F * 1000
    elif F == S or S == T:
        result = 1000 + S *100
    elif F == T:
        result = 1000 + F *100
    else:
        temp = []
        temp.append(F)
        temp.append(S)
        temp.append(T)
        ot = sorted(temp)
        maxot = ot[2]
        result = maxot * 100

    if maxV < result:
        maxV = result

print(maxV)