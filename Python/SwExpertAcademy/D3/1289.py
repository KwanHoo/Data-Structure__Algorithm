# 1289_원재의 메모리 복구하기

# 메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리 끝까지 덮어쒸우는 문제발생
#! 초기값은 모든 비트가 0
#! 원래 값으로 복구하기 위한 최소 수정 횟수출력

T = int(input())

for tc in range(T):
    initV = list(input())
    gil = len(initV)
    # cho = []
    # for i in range(gil):
    #     cho.append('0')
    flag = '0' # 0, 1 선택
    count = 0

    for i in range(gil):
        if initV[i] == flag:
            flag = initV[i]
        else:
            count +=1
            flag = initV[i]
    print(f'#{tc+1} {count}')
