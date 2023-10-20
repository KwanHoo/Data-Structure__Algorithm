# 2025 N줄 덧셈

# 1부터 주어진숫자만큼 더하기

# sol) for문 이용해서 1씩 중가하며 값들 더해주기

N = int(input())

sum_result = 0
for j in range(1,N+1):
    sum_result += j
print(sum_result)