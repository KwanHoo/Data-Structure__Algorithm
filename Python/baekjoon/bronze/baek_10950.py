## 백준 10950번
## A + B -3
## 반복문, 수학, 구현, 사칙연산

import sys

def sum_3(a,b):
    return a+b

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        A,B = map(int, sys.stdin.readline().split())
        print(sum_3(A,B))


''' 참고 exec() 내장함수
exec('print(eval("+".join(input())));'*int(input()))
'''

''' 참고
for a,_,c,_ in[*open(0)][1:]:print(int(a)+int(c))
'''