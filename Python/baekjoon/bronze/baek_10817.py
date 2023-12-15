# 문제집) Python 배우기 (1~50)
## 10817_세 수
# 브론즈 3

A, B, C = list(map(int, input().split()))

awesome = []

awesome.append(A)
awesome.append(B)
awesome.append(C)

orderl = sorted(awesome)    # 오름차순
print(orderl[1])            # 두번째 큰수

