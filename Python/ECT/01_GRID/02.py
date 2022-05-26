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

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1

    if M == 0:
        break
    result += second
    M -= 1

print(result)