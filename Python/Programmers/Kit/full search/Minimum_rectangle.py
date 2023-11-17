# 알고리즘 고득점 KIT _ 완전탐색
# 최소직사각형

# input : [[60, 50], [30, 70], [60, 30], [80, 40]]
# result : 4000

# 가로 눕혀 수납?? -> 가로 세로 변경 => 지갑의 크기 최적화 (가로 세로)
## 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기



def solution(sizes):
    firMax = 0
    secMax = 0

    # 앞에 큰거오게
    for m in range(len(sizes)):
        if sizes[m][0] <= sizes[m][1]:
            temp = sizes[m][0]
            sizes[m][0] = sizes[m][1]
            sizes[m][1] = temp

    for n in range(len(sizes)):
        if sizes[n][0] > firMax:
            firMax = sizes[n][0]

    for l in range(len(sizes)):
        if sizes[l][1] > secMax:
            secMax = sizes[l][1]


    answer = firMax * secMax
    return answer