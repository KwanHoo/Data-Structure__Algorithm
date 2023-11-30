# 4466_최대 성적표 만들기

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    nlist = list(map(int, input().split()))
    # print(nlist)
    nlist.sort(reverse=True) # 내림차순으로 정렬함

    # print(nlist)
    sumv = 0

    for i in range(K):
        sumv += nlist[i]

    print(f'#{tc+1} {sumv}')
