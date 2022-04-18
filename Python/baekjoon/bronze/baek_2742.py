## 백준 2742
## 기찍 N
## [반복문], 구현

def loopN(n):
    for i in range(n,0,-1):
        print(i)

if __name__ == '__main__':
    N = int(input())
    loopN(N)

''' 참고 숏코드
print(*range(int(input()),0,-1))
'''