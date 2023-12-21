# 문제집) Python 배우기 (1~50)
## 1789_수들의 합
# 실버 5

## 서로 다른 N개의 자연수의 합이 S라고 할때 S가주어지면 N의 최대값음?
## 1부터 N까지 더하다 S넘게 되면 그이전 N값이 정답임

S = int(input())

N = 1
sumV = 0

# while S > sumV:
#     print(sumV, N , sumV+N)
#     ## 초과되는 경우
#     if sumV+N+1 > S:
#         print('break')
#         break
#     else:
#         print('else')
#         sumV = sumV + N
#         N += 1

while S >= sumV+N:
    sumV +=N
    N += 1
    # print(sumV, N, sumV+N)

N -= 1
print(N)


