# 11387_몬스터 사냥

## 식 : D*(1+n * L(1/100))


T = int(input())

for tc in range(T):
    D, L, N = map(int,input().split())
    totalD = D
    for i in range(1, N):
        damage = D * (1 + i * L * 0.01)
        totalD += damage

    result = int(totalD)
    print(f'#{tc+1} {result}')