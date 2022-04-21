## 백준 10430번
## 나머지
## 입출력, 사칙연산, 수학, 구현

import sys

A,B,C = map(int, sys.stdin.readline().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
