# 문제집) Python 배우기 (1~50)
## 10102_개표
# 브론즈 3

## 어떤 사람이 우승하는지 구하는 프로그램

V = int(input())
vote = str(input())
acount = 0
bcount = 0

for i in range(V):
    if vote[i] == 'A':
        acount +=1
    else:
        bcount +=1

if acount > bcount:
    print("A")
elif acount < bcount:
    print("B")
elif acount == bcount:
    print("Tie")