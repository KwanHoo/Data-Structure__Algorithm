# 1948_날짜 계산기

# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

T = int(input())

# 딕셔너리 활용
end = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(T):
    fm, fd, sm, sd = map(int, input().split())

    # print(fm, fd, sm, sd)
    result = 0
    temp = 0
    ## 같은 월
    if fm == sm:
        temp = sd - fd
    ## 다른월
    else:
        for i in range(fm, sm):
            temp += end[i]

        ## 전달 처리
        temp -= fd
        ## 뒷달 처리
        temp += sd
    result = temp +1
    print(f'#{tc+1} {result}')