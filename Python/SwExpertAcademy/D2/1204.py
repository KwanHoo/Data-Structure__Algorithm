# 1204 [S/W 문제해결 기본] 1일차 - 최빈수 구하기

# count이용 큰거 출력

T = int(input())

for tc in range(T):
    testcase = int(input())
    scoreL = list(map(int, input().split()))

    checkC = 0

    maxV = scoreL[0]

    for i in range(len(scoreL)):
        temp = scoreL[i]

        nowC = scoreL.count(temp)

        if checkC < nowC:
            checkC = nowC
            maxV = temp
        # print(i, temp, nowC, checkC)
    print(f'#{testcase} {maxV}')