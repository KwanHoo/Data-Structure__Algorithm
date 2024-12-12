# 최소직사각형

#!가로 눕혀 수납?? -> 가로 세로 변경 => 지갑의 크기 최적화 (가로 세로)
## 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기

def solution(sizes):
    firMax = 0
    secMax = 0
    # print(sizes)
    # 앞에 큰거오게
    # for m in range(len(sizes)):
    #     if sizes[m][0] <= sizes[m][1]:
    #         temp = sizes[m][0]
    #         sizes[m][0] = sizes[m][1]
    #         sizes[m][1] = temp
    ## swap
    for m in range(len(sizes)):
        if sizes[m][0] <= sizes[m][1]:
            sizes[m][0], sizes[m][1] = sizes[m][1], sizes[m][0]

    # print(sizes)
    for n in range(len(sizes)):
        if sizes[n][0] > firMax:
            firMax = sizes[n][0]

    for l in range(len(sizes)):
        if sizes[l][1] > secMax:
            secMax = sizes[l][1]
    # print(firMax)
    # print(secMax)
    answer = firMax * secMax
    return answer