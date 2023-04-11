## 동적계획법
# 피보나치 함수 소스코드
# 시간 복잡도 : O(2^N)

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(10))

# 동일한 함수가 반복적으로 호출됨, 비효율적임

