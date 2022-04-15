## 백준 13910번
## 개업
## 다이나믹 프로그래밍
## (짜장면 데이)

'''
##! ex) N = 4,  5그릇 이상 요리 X, 4사이즈 윅에 3그릇 이하 요리 X  => 4윅에 4개
##* ex) N = 5, 윅 사이즈 1,3 / first : 1+3 = 4 그릇, second : 1 => 5 그릇 --> 2번의 요리로 주문 처리


##* 주문 받은 짜장면의 수, 가지고 있는 윅의 크기 => 주문 처리 
# In1 ) N M  : (주문 받은 짜장면의 수) N  | (가지고 있는 윅의 수) M
# In2 ) S    : 윅의 크기 S가 M개 만큼 주어짐 (같은 크기의 윅을 여러개 가지고 있을 수 있음)
# out ) 혜빈이가 모든 주문을 처리하기 위해 해야 하는 최소 요리수  | 주문 처리 못할시 -1

'''

'''
 ex1I) 5주문 2개윅
 ex1I) 1과 3사이즈
 out ) 2

 ex2I) 6주문 2개윅
 ex2I) 1과 3사이즈
 out ) 2

5 2
2 4
=> 4|1  1<2  : -1

13 3

'''

import sys

## 프로토타입
def cooking(N,M,wig):
    count = 0
    temp = N
    breakpoint = False

    while temp != 0:
        for i in range(M-1, -1, -1):
            if wig[i] < temp or wig[i] == temp:
                temp -= wig[i]
                count += 1
            else:
                continue
            if i == 0:
                k = wig[0]
                if temp % k == 0:
                    count = count + (temp//k)
                else:
                    breakpoint = True
                    count = -1
        if breakpoint == True:
            break
    return count

## 테스트 1 성공, 2 실패
def cooking2(N, M, wig):
    temp = N
    count = 0

    while temp != 0:
        ## 기저 조건
        if wig[0] > temp:
            count = -1
            break

        for i in range(M-1, -1, -1):  ## M-1인덱스 부터 0 까지
            if wig[i] < temp or wig[i] == temp:
                temp -= wig[i]
        count += 1
    return count

## 미완성
def cooking4(N, M, wig):
    temp = N
    count = 0

    while temp != 0:
        ## 기저 조건
        if wig[0] > temp:
            count = -1
            break


        for j in range(M-1, -1, -1):
            ## 반복
            if temp % wig[j] > 1: ## 7 = 3*2 + 1  ## 8 = 3*2 + 1*2

                if temp % wig[j] == 0:  ## 6 = 3*2
                    count += temp // wig[j]
                    temp = 0
                    break
            
            else:
                ## 반복 고려 X
                for i in range(M-1, -1, -1):  # M-1인덱스 부터 0 까지
                    if wig[i] < temp or wig[i] == temp:
                        temp -= wig[i]
                count += 1

    return count




if __name__ == "__main__":
    print('hello')

    N, M = map(int, sys.stdin.readline().split())
    wig = list(map(int, sys.stdin.readline().split()))
    wig.sort()# 정렬 때리기

    # print(wig)
    # print(cooking(N, M, wig)) ## 제대로 안나옴
    # print(cooking2(N,M,wig))  ## 테스트 케이스 2 반복 처리 안됨
    print(cooking4(N,M,wig)) ## 미완성