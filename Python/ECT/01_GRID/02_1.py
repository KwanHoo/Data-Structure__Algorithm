# 큰수의 법칙
# 난이도 하
# 그리드

# 입력
# 1) N, M, K
# N: 배열의 크기
# M: 더해지는 횟수
# K: K번 초과 연속 X


N, M, K = map(int, input().split())
# N, M, K = map(int, sys.stdin.readline().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수를 정렬
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산ㅊ
count = int(M / (K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M - count) * second # 두번째로 큰 수 더하기

## 풀이방법 2
print(result) # 최종 답안 출력