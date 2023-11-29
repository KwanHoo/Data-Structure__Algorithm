# 6692_다솔이의 월급 상자

T = int(input())

for tc in range(T):
    N = int(input())
    te = []

    for i in range(N):
        k, v = map(float, input().split())
        temp = [k, v]
        te.append(temp)

    result = 0
    # print(te) ##[[0.3, 100.0], [0.7, 1.0]]
    for j in range(N):
        temp = te[j][0] * te[j][1]

        result += temp

    print(f'#{tc+1} {result}')