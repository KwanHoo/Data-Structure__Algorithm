## 백준
## 2263번 : 트리의 순회
## 트리, 분할 정복, 재귀
##* 중위, 후위 => 전위순회

import sys
sys.setrecursionlimit(10**5)
# print(sys.getrecursionlimit())
##! 10**4(기본)로 하면 런타임 에러..
##! 10**6 이상 으로하면 메모리 초과가뜸..

def in_post_to_pre(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    root = post_order[post_r]
    mid = pos[root]
    # mid = in_order.index(root)
    left = mid - in_l
    right = in_r - mid
    print(root, end=" ")
    in_post_to_pre(in_l, in_l + left - 1, post_l, post_l + left - 1)
    in_post_to_pre(in_r - right + 1, in_r, post_r - right, post_r - 1)


if __name__ == "__main__":
    n = int(input())

    in_order = list(map(int, sys.stdin.readline().split()))
    post_order = list(map(int, sys.stdin.readline().split()))

    N = len(in_order)
    pos = [0] * (N + 1)

    for i in range(N):
        pos[in_order[i]] = i

    in_post_to_pre(0, N - 1, 0, N - 1)

