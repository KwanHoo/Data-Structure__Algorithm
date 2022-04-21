## 백준 2588번
## 곱셈
## 입출력, 사칙연산, 수학

A = int(input())
B = input()

for i in range(2, -1, -1):
    print(A*int(B[i]))
print(A*int(B))