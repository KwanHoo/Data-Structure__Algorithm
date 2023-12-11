# 문제집) Python 배우기 (1~50)
## 2530_인공지능 시계
# 브론즈 4

## 입력
H, M, S = map(int, input().split())
D = int(input())


# print('1st', H ,M, S, D)
S += D % 60
D = D // 60
# 초 60 보다 큰 경우 분으로
if S >= 60:
    S -= 60
    M += 1
# print('2st', H ,M, S, D)

M += D % 60
D = D // 60
# 분 60 보다 큰 경우 시로
if M >= 60:
    M -= 60
    H += 1
# print('3st', H ,M, S, D)

H += D % 24
# 자정 넘은 경우
if H >= 24:
    H -= 24
# print('4st', H ,M, S, D)

print(H,M,S)