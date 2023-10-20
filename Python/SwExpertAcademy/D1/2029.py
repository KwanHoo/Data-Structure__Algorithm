# 2029 몫과 나머지 출력하기

# 2개의 수 a,b를 입력 받아 a를 b로 나눈 목과 나머지를 출력

# sol) 몫연산자, 나머지 연산자 이용
T = int(input()) # 입력 받는 개수
Num = 1

for i in range(T):
    F, S = map(int, input().split())
    result_m = F // S
    result_n = F % S
    print(f'#{Num} {result_m} {result_n}')
    Num += 1