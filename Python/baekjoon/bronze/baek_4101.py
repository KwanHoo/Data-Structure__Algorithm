# 문제집) Python 배우기 (1~50)
## 4101_크냐?
# 브론즈 5

# 첫번째 수가 두번째 보다 큰지 판별

while True:
    A, B = map(int, input().split())
    if( A==0 and B==0):
        break

    if A > B:
        print('Yes')
    else:
        print('No')