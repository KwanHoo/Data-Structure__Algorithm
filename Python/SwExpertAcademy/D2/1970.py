# 1970_쉬운 거스름돈

# 높은 금액 먼저 거스름돈으로

#! 마지막 자릿수는 항상 0이다 -> 10의 배수임

target = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(T):
    value = int(input())
    count = []
    for i in range(len(target)):
        temp = int(value//target[i])    ## 몫
        count.append(temp)

        value = value%target[i]         ## 나머지

    print(f'#{tc+1}')
    print(*count)           ## 리스트 요소 한번에 출력하기 print(*arr)


