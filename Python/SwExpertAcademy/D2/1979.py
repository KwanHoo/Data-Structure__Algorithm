# 1979_어디에 단어가 들어갈 수 있을까

## 2차원 배열 이용

# T = int(input())

### not in 활용 풀이 테스트케이스 통과 못함
### -> 111 0 1111 -> 이거 K 3개로 맞는 케이스 지만 count 자체가 1 이상으로 카운팅하므로
# for tt in range(T):
#     N, K = map(int, input().split())
#     result = 0
#     # 리스트 컴프리헨션
#     arr = [[0 for c in range(N)] for r in range(N)]
#
#     ## arr에 입력 담는 부분
#     for i in range(N):
#         temp = list(map(int, input().split()))
#         # print(temp)
#         arr[i] = temp
#     #print(arr)
#
#
#
#     ## 세로 탐지: 딱 K여야함
#     for s in range(N):
#         # x,y축 스위치함
#         temp_arr = []
#         for l in range(N):
#             # arr[l][s] 일자로 확인
#             temp_arr.append(arr[l][s])
#             # print(l, s)
#             # print(temp_arr)
#         #print(temp_arr)
#
#         ## 여기서도 슬라이싱 해서 꽉인지 판별
#         count_r = 0
#         for m in range(N-K+1):
#             temp_arr2 = temp_arr[m:m+3]
#             # print(temp_arr2)
#             test_T = False
#             if 0 not in temp_arr2:
#                 test_T =True
#
#             if test_T:
#                 count_r += 1
#         # print(count_r)
#         if count_r ==1:
#             result += 1
#     # print(result)
#
#
#     ## 가로 탐지: 슬라이싱, not in
#     for g in range(N):
#         count_r = 0
#         for t in range(N-K+1):
#             # arr[t:t+3] 모두 1이고 그 줄에 1번이어야함
#             temp_arr = arr[g][t:t+3]
#             # print(temp_arr)
#             test_T = False
#             if 0 not in temp_arr: # 모두 1인지
#                 test_T = True
#
#             # 3개 1 인지 판별
#             if test_T:
#                 count_r += 1
#         # print(g)
#         # print(count_r)
#         if count_r == 1:
#             result +=1 # 가로 탐지 굿
#
#
#     print(f'#{tt+1} {result}')
#
t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    # 가로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
            if data[i][j] == 0 or j == n - 1:   # 현재값이 0 이거나 마지막 열인경우
                if cnt == k:                    # cnt 값 확인 k와 같은경우 result 1 증가
                    result += 1
                if data[i][j] == 0:
                    cnt = 0

    # 세로 확인
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[j][i] == 1:
                cnt += 1
            if data[j][i] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                if data[j][i] == 0:
                    cnt = 0

    print('#%d %d' % (tc, result))