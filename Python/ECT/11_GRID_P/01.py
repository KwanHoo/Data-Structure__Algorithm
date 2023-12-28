# 01_모험가 길드

## 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여

# 최대 몇개의 모험가 그룹을 만들 수 있는지??
## 낮은 공포도 부터 묶는게  최대 그룹 만드는 해법임

N = int(input())
mgroup = list(map(int, input().split()))
gcount = 0
## 오름 차순 정렬
mgroup.sort()
# print(mohumga) # [1, 2, 2, 2, 3]

tgroup = []
for i in range(N):
    temp = mgroup[i]
    tgroup.append(temp)

    if temp > len(tgroup):
        pass
        # print('if',i, temp, tgroup, gcount)
    ## 모험 그룹 출발 가능
    else:
        tgroup.append(temp)
        gcount += 1
        # print('else',i, temp, tgroup, gcount)
        ## temp 그룹 초기화
        tgroup = []

    # N 까지옴 종료
    if i == N-1:
        break

print(gcount)


### 23.12.28 solve : 12m