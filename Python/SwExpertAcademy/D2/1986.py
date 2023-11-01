# 1986_지그재그

# 1부터 N까지 홀수 더하고 짝수는 뺌

#! 1이상 10이하 정수

T = int(input())

for k in range(T):
    L = int(input())
    sum_result = 0
    for i in range(1, L+1):
        # print(i)
        check = i%2
        if check == 0:
            sum_result -= i
        else:
            sum_result += i
    print(f'#{k+1} {sum_result}')
