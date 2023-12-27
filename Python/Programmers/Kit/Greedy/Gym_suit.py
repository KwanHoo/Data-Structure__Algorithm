# 알고리즘 고득점 KIT _ 탐욕법
# 체육복

## 앞뒤 번호 사람에게만 빌릴 수 있음
#! 여벌 가지고 있는 학생이 도난 당하는 경우도 있음
#! lost, reserve 리스트가 정렬되어 있다고 제시가 안되어 잇음
#!-> 정렬 시켜놓자

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))


## 내 풀이~~
def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    ## 여벌있는아이가 도난당한경우
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    answer += n-len(lost)

    ## 잃어버린 애들 빌리는거 가능 개수 판별
    for i in range(len(lost)):
        temp = lost[i]

        if len(reserve) != 0:
            for j in range(len(reserve)):
                temp2 = reserve[j]

                if temp2-1 == temp or temp2+1 == temp:
                    answer +=1
                    reserve.remove(temp2)
                    break
    return print(answer)

solution(n, lost, reserve)


### 참고 다른 사람 풀이

def solution2(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()

    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)