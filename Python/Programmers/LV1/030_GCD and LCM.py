# 최대공약수와 최소공배수

import math


def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    # 최소공배수
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer


## 유클리드 호제법 이용
# * 유클리드->최대공약수
# * 두 개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘
# * 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 할 때
# ** A, B의 최대공약수는 B와 R의 최대공약수와 같다
def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def solutiongcd(n, m):
    answer = [gcd(m, n), n * m // gcd(m, n)]
    return answer