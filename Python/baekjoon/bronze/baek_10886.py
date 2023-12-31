# 문제집) Python 배우기 (1~50)
## 10886_0 = not cute / 1 = cute
# 브론즈 3

## 설문조사 통해 판단

N = int(input())

one = 0
zero = 0

## 설문조사
for _ in range(N):
    temp = int(input())

    if temp == 1:
        one +=1
    elif temp == 0:
        zero +=1

## 조사결과 판별
if one > zero:
    print("Junhee is cute!")
elif one < zero:
    print("Junhee is not cute!")

