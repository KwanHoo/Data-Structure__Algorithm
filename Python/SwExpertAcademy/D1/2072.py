# 2072 _ 홀수만 더하기
# 10개의 수 입력 받아 그 중 홀수만 더한 값을 출력

# input
# 1) T:테스트케이스 수
# 2) 테스트 케이스 입력,,,,

# output
# #1 200
# #2 208 ..

T = int(input())
sum_list = []
for i in range(T):
    sum_temp = []
    temp_list = list(map(int, input().split()))
    for j in temp_list:
        if j % 2 == 1:
            sum_temp.append(j)
    temp = sum(sum_temp)
    sum_list.append(temp)

c = 1
for i in sum_list:
    print(f'#{c} {i}')
    c += 1
