# 2001 _ 파리 퇴치
# 최대한 많은 파리 죽이기 __ 2차원 리스트 컴프리헨션, 5중 for문 사용.. ㅎㄷ

#! N은 5이상 15이하 : 영역의 크기
#! M은 2이상 N 이하 : 파리 죽이는 범위

#st) 합이 제일 큰거 , 2차원 배열 이용
T = int(input()) # 테스트 케이스

for i in range(T):
    N, M = list(map(int, input().split())) #  N, M 입력

    # N*N의 2차원 배열 초기화
    temp = [[0 for l in range(N)] for m in range(N)]
    # print(temp)
    ## 영역 입력 받는 부분

    for x in range(N):
        temp_input = list(map(int, input().split()))
        # print(temp_input)
        for y in range(N):
            temp[x][y] = temp_input[y]
            # print(temp[x])
    # temp[x][y] 에 영역 값 넣음

    max_result = 0

    for f in range(N-M+1): # 0~3
        for g in range(N-M+1): # 0~3
            temp_result = 0

            for c in range(M): # 0~1
                for h in range(M): # 0~1
                    temp_result += temp[f+c][g+h] # M*M 의 원소들 temp에 더해줌

            ## M*M 영역 최대값 갱신 해주는 부분
            if temp_result > max_result:
                max_result = temp_result

    print(f'#{i+1} {max_result}')



## 참고) 리스트 컴프리헨션 이용해서 2차원 배열 초기화
# cols = 5
# rows = 4
# arr = [[0 for j in range(cols)] for i in range(rows)] #리스트 컴프리헨션 이용
# print(arr)

