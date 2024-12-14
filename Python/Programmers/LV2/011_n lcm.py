# N개의 최소공배수

import math


# 최소공배수 함수
## 최소공배수 =  두수 곱한값 // 최소공약수
def lcm(a, b):
    return a * b // math.gcd(a, b)


def solution(arr):
    answer = 0

    n = arr[0]

    for i in arr[1:]:
        print(n, i)
        n = lcm(n, i)

    answer = n
    return answer