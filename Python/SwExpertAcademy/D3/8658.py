# 8658_Summation

# 동욱이 문제 통과해여 거래 시작 (3개의 시련)
## 첫번째 관문에서 10개 자연수 주어짐

## 주어진 수의 각자리수를 더하고 리스트중 최대값 최소값 답

T = int(input())

for tc in range(T):
    testcase = list(map(str, input().split()))
    minV = 9999999
    maxV = 0
    for i in testcase:
        # print(i)
        sumTemp = 0
        for j in range(len(i)):
            jari = i[j]
            sumTemp += int(jari)

        if sumTemp > maxV:
            maxV = sumTemp
        if sumTemp < minV:
            minV = sumTemp

    print(f'#{tc+1} {maxV} {minV}')

# 파이썬 제출 X