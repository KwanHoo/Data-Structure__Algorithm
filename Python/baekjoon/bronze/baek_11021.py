## 백준 11021
## A + B - 7
## [반복문], 수학, 구현, 사칙연산

import sys

if __name__ == '__main__':
    T = int(input())

    for i in range(1,T+1) :
        A,B = map(int,sys.stdin.readline().split())

        sums = A + B
        print('Case #{}: {}'.format(i,sums))


''' 참고 숏코드
i=0
for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',int(a)+int(c))
'''