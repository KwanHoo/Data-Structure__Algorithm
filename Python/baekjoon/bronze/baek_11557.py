# 문제집) Python 배우기 (1~50)
## 11557_Yangjojang of the Year
# 브론즈 1

## 학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력

T = int(input())

for tc in range(T):
    N = int(input())

    best = ''
    maxs = 0
    for _ in range(N):
        s, p = input().split()

        if maxs < int(p):
            best = s
            maxs = int(p)

    print(best)
