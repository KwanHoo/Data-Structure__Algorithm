# 3431_준환이의 운동관리

# 1주일에 L분이상 U분이하 운동
# 이번주는 x분만큼 운동

T = int(input())

for tc in range(T):
    L, U, X = map(int, input().split())

    if X>U :
        result = -1
    elif L<= X <=U:
        result = 0
    elif X<L:
        result = L - X

    print(f'#{tc+1} {result}')