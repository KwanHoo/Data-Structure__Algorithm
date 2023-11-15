# 6730_장애물 경주 난이도

# 난이도 : 차가 가장 큰 부분

T = int(input())

for tc in range(T):
    N = int(input())
    nlist = list(map(int, input().split()))

    ol = 0
    ne = 0

    for i in range(N-1): # 마지막까지 안가도됨
        fir = nlist[i]
        sec = nlist[i+1]

        if fir == sec:
            continue
        elif fir < sec:
            temp = sec - fir
            if ol < temp:
                ol = temp
        elif fir > sec:
            temp = fir - sec
            if ne < temp:
                ne = temp

    print(f'#{tc+1} {ol} {ne}')

# 체점은 python은 안됨