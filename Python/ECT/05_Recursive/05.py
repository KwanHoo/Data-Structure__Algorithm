## 재귀구현 _팩토리얼

# 소스코드를 반복적(iterative)으로 구현한다는 말은 반복문을 이용한다는 의미이며,
# 흔히 재귀적(recursive)으로 구현한다는 말과 대비되는 의미로 사용됨
# 1) 반복적으로 구현한 N!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 2) 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))