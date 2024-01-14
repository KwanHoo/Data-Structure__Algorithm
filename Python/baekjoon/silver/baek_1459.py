## 백준_1459번
## 걷기
## 실버3
# 그리드문제

## 테스트 케이스 걸림
# X, Y, W, S = list(map(int, input().split()))
#
# time = 0
#
# # 큰값, 작은값
# if X > Y:
#     bv = X
#     sv = Y
# else:
#     bv = Y
#     sv = X
#
# # S랑 W 최솟값 판단
# if sv != 0:
#     t1 = sv * 2 * W
#
#     print(t1, S*sv)
#     if t1 > S*sv:
#         # 가로지르는게 이득
#         time += S*sv        # 10 * 16
#         time += (bv-sv) * W # 8 * 12
#     else:
#         # x,y이동이 이득
#         time += (bv+sv) * W
# else:
#     if W > S:
#         time = bv * S
#     else:
#         time = bv * W
# print(time)


## 참고 풀이
x, y, w, s = map(int, input().split())

#평행으로만 이동
m1 = (x+y) * w

#대각선으로만 이동
if (x + y) % 2 == 0:
    m2 = max(x, y) * s
#대각선이동 + 평행이동 1번
else:
    m2 = (max(x, y) - 1) * s + w

#평행이동 + 대각선이동
m3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(m1, m2, m3))