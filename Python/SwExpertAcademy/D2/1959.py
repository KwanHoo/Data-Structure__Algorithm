# 1959_두 개의 숫자열

# N - Ai (i : 1~N)
# M - Bj (j : 1~M)

T = int(input())

for tc in range(T):
    N,M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = -9999999999

    if N >= M:
        big_l = A
        sml_l = B
        big = N
        sml = M
    else:
        big_l = B
        sml_l = A
        big = M
        sml = N

    ## 곱하면서 판별 부분
    for i in range(big-sml+1):
        temp_sum = []
        for j in range(sml):
            ### big_l 는 i부터 i+j만큼 sml은 0~j까지 각 자리 곱해서 더한값은 temp_sum에
            temp = big_l[i+j] * sml_l[j]
            temp_sum.append(temp)
        #     print(i, j, temp)
        #
        # print(i)
        # print(j)
        # print(temp_sum)
        pan_sum = sum(temp_sum)
        if pan_sum >= max_sum:
            max_sum = pan_sum

    print(f'#{tc+1} {max_sum}')



