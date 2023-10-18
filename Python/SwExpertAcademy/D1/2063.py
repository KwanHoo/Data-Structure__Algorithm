# 2063 _ 중간값 찾기
# 입력으로 N개가 주어졌을 때 중간값 출력

# input
# 1) N 점수의 갯수
# 2) 점수들 입력 입력,,,,

# output
# 58

## solve) 중간값출력 방법은 sort() 이용해서 정렬시키고 입력된 개수(N)의 중간 인덱스(나누기2) 해서 출력

N = int(input())
list_N = list(map(int, input().split()))
list_N.sort() # 오름차순으로 정렬하는 부분

# print(list_N)
## N값이 홀수, 짝수인 경우 다르게 인덱싱 해서 중간값 출력하게
if N % 2 == 1: # 홀수인경우
    #print('홀수')
    idx = int(N / 2)
else:
    #print('짝수') ##! 문제에서 짝수인 경우가 없다고 이야기 해줌!!
    idx = int(N / 2)
# print(f'인덱스{idx}')
result_v = list_N[idx]
print(result_v)