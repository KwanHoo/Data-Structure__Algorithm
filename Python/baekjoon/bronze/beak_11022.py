# 문제집) Python 배우기 (1~50)
## 11022_A+B-8
# 브론즈 5

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    sumV = A+B
    print(f'Case #{tc+1}: {A} + {B} = {sumV}')
