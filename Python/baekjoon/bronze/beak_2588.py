# 문제집) Python 배우기 (1~50)
## 2588_곱셈
# 브론즈 3

## 방법1
# A = int(input())
# B = input()
#
# result1 = A * int(B[-1])
# result2 = A * int(B[-2])
# result3 = A * int(B[-3])
# result4 = A * int(B)
#
#
# print(result1)
# print(result2)
# print(result3)
# print(result4)

## 방법2 range for 문 이용
A = int(input())
B = input()

for i in range(2, -1, -1):
    print(A*int(B[i]))
print(A*int(B))