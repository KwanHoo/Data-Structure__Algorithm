# 2068 _ 최대수 구하기
# 10개의 수를 입력 받아 그중 가장 큰 수를 출력

# input
# 1) T:테스트케이스 수
# 2) 테스트 케이스 입력,,,,

# output
# #1 99
# #2 123 ..


T = int(input()) # 테스트케이스 수 입력 부붑ㄴ

result_list = []
for i in range(T):
    temp_list = list(map(int, input().split()))
    max_list_value = max(temp_list)             # 리스트의 최대값 뽑는 함수인 max() 이용
    result_list.append(max_list_value)

num_temp = 1
for i in result_list:
    print(f'#{num_temp} {i}')
    num_temp += 1
