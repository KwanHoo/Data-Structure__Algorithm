# 피보나치 수

# 1234567 로 나누는 이유 :
# int 자료형의 범위 내에 항상 값이 있을 수 있도록 한 배려이며

def solution(n):
    dp = [0] * 100001
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567