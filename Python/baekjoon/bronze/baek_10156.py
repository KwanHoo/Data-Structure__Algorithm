# 문제집) Python 배우기 (1~50)
## 10156_과자
# 브론즈 4
## K : 과자 한개의 가격
## N : 사려고하는 과자의 개수
## M : 동수가 가진 돈

## result : 동수가 부모님께 받아야하는 돈의 액수

K, N, M = map(int, input().split())

needM = K * N

if needM <= M:
    result = 0
else:
    result = needM - M

print(result)