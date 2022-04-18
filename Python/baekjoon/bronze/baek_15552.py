## 백준 15552번
## 빠른 A+B
## [반복문], 구현, 사칙연산, 수학
import sys

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        
        print(A+B)


'''참고 숏코드
for l in[*open(0)][1:]:
    print(sum(map(int,l.split())))

----------------------------------------------------------------
open(0) 자체는 파일 오브젝트를 돌려줌
파일 오브젝트의 redlines 메소드는 다 읽어서 리스트에 담아줌
for i in open(0)는 이터레이터에 대한 이해가 필요함
결과적으로 readlines()와 비슷하게 한줄씩 돔
'''
