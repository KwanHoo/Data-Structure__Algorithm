# 1945_간단한 소인수분해

# N = 2^a * 3^b * 5^c * 7^d * 11^e

T = int(input())

for tc in range(T):
    value = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while value%2 == 0:
        a +=1
        value = int(value/2)
    while value%3 == 0:
        b +=1
        value = int(value/3)
    while value%5 == 0:
        c +=1
        value = int(value/5)
    while value%7 == 0:
        d +=1
        value = int(value/7)
    while value%11 == 0:
        e +=1
        value = int(value/11)
    #print(a,b,c,d,e)
    print(f'#{tc+1} {a} {b} {c} {d} {e}')