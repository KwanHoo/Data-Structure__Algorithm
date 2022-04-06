import math

##* case1 math.pow
num  = int(input())
for _ in range(num):
    a,b = map(int, input().split())
    temp = math.pow(a,b)
    comnum = int(temp % 10)
    print(comnum)
#! OverflowError: math range error

##* case2 다른풀이
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)
