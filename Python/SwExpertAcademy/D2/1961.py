# 1961_ 숫자 배열 회전

# N*N 행렬 주어지고 -> 시계방향으로 횐전한 모양을 출력
## 90 -> 180 -> 270

#! N은 3이상 7이하

T = int(input())

for tc in range(T):
    N = int(input())

    # 리스트 컴프리헨션 데이터
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data) [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = [[0 for j in range(3)] for i in range(N)] ##! 결과값 저장 배열 90,180,270 저장해야함으로 열값 3개면 됨
    # print(result) [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    ## 90도 회전 저장 (0,0) (1,0) (2,0)
    ### 741 (2,0) (1,0) (0,0)  852 (2,1) (1,1) (0,1)
    for w in range(N):
        temp = ''
        for v in range(N-1, -1, -1): # 2 1 0
            temp += str(data[v][w])
        # print(temp)
        result[w][0] = temp
    # print(result) [['741', 0, 0], ['852', 0, 0], ['963', 0, 0]]


    ## 180도 회전 저장 (0,1) (1,1) (2,1)
    ### 987 (2,2) (2,1) (2,0)
    for w in range(N):
        temp = ''
        for v in range(N-1, -1, -1):
            temp += str(data[N-1-w][v])     #! (N-1) -w => N 크기 3~7사이임으로 변수로

        result[w][1] = temp
    # print(result) [['741', '987', 0], ['852', '654', 0], ['963', '321', 0]]

    ## 270도 회전 저장 (0,2) (1,2) (2,2)
    ### 369 (0,2) (1,2) (2,2) 258 (0,1) (1,1) (2,1)

    for w in range(N):
        temp = ''

        for v in range(N):
            temp += str(data[v][N-1-w])

        result[w][2] = temp
    # print(result) [['741', '987', '369'], ['852', '654', '258'], ['963', '321', '147']]


    print(f'#{tc+1}')
    for k in range(N):
        print(*result[k])