# 1974_스도쿠 검증

# 입력된 배열 스두쿠 검증

T = int(input())

# sol) 정렬시켜 target과 같은지 확인
target = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for tc in range(T):
    result = 1
    tc_break = True
    tc_break2 = True
    tc_break3 = False
    ## 리스트 컴프리헨션
    # arr = [[0 for j in range(9)] for i in range(9)]
    # # print(arr)
    # ## arr에 입력 담는 부분
    #
    # for l in range(9):
    #     temp = list(map(int, input().split()))
    #     # print(temp)
    #     arr[l] = temp
    # print(arr)

    ## 위 리스트 컴프리헨션 입력 받는 부분 1줄로 가능
    data = [list(map(int, input().split())) for _ in range(9)]
    # print(data)

    ## 가로판별
    for i in range(9):
        temp = data[i]
        sort_temp = sorted(temp)
        # print(sort_temp)

        if sort_temp != target:
            result = 0
            print(f'#{tc+1} {result}')
            tc_break = False
            break

    if tc_break:
        ## 세로판별
        for i in range(9):
            temp =[]
            for j in range(9):
                temp.append(data[j][i])
            sort_temp = sorted(temp)

            if sort_temp != target:
                result = 0
                print(f'#{tc+1} {result}')
                tc_break2 = False
                break

        if tc_break2:
            ## 격자판별 (0,0) ~ (6,6) 9번
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    temp = []
                    # print(i,j)
                    for m in [i, i+1, i+2]:
                        for n in [j, j+1, j+2]:
                            temp.append(data[m][n])
                            # print(m, n)
                    # print(temp) ## 여기 들어옴 격자 데이터
                    sort_temp = sorted(temp)
                    # print(sort_temp)
                    if sort_temp != target:
                        result = 0
                        print(f'#{tc+1} {result}')
                        tc_break3 = True
                        break
                if tc_break3: ####!! 2중 포문 탈출위해
                    break
    if result == 1:
        print(f'#{tc+1} {result}')


## 참고 코드드
N = int(input()) # TC 갯수
for k in range(1, N + 1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 입력
    rowArr = arr #가로 배열은 입력받은 배열과 동일
    colArr = [[arr[i][j] for i in range(9)] for j in range(9)] #새로 배열 변환 !!!
    sqrArr = [[arr[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)] # 3 * 3 사각형 각각을 1차원 배열로 변환 !!!!!!
    answer = 1 #출력할 정답
    for row, col, sqr in zip(rowArr, colArr, sqrArr): # 2차원배열에서 각각 1차원 배열을 꺼내서
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9: # 집합으로 변환했을때 길이가 모두 9이면
            continue # 통과
        else: #아니면 (스도쿠 조건 충족 X)
            answer = 0 #정답 0으로 설정
            break # 반복 중단
    print("#", k, " ", answer, sep="") #정답 출력

# 더해서 모두 45가 되는지 확인?? -> 이거는 반례가 있을수 있음 222+666+~~~