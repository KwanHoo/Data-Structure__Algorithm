# 05 볼링공 고르기

import itertools

# A,B : 사람 /  N:볼링갯수
#! 같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주함
#! 볼링공의 무게는 1부터 M까지의 자연수
#! 두 사람은 서로 무게가 다른 볼링공을 고르려고함!!!

## 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성

N, M = map(int, input().split())

Nlist = list(map(int, input().split()))

result = itertools.combinations(Nlist, 2)

#print(list(result)) [(1, 3), (1, 2), (1, 3), (1, 2), (3, 2), (3, 3), (3, 2), (2, 3), (2, 2), (3, 2)]

count = 0
for i in list(result):
    x,y = i

    if x != y:
        count +=1

print(count)

## 24.01.01 solve : 15m