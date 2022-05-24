# 2071 _ 평균값 구하기
# 10개의 수를 입력 받아 평균값을 출력

# input
# 1) T:테스트케이스 수
# 2) 테스트 케이스 입력,,,,

# output
# #1 24
# #2 29 ..

T = int(input())
avg_list = []
for i in range(T):
    temp_list = list(map(int, input().split()))
    sum_temp = sum(temp_list)
    temp = sum_temp / len(temp_list)
    avg_list.append(temp)
# print(avg_list)

c = 1
for i in avg_list:
    i = round(i)
    print(f'#{c} {i}')
    c += 1