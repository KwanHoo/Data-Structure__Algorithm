##* 참고 링크 : https://8iggy.tistory.com/112

pre_order = [1, 2, 4, 7, 3, 5, 6]
in_order = [4, 7, 2, 1, 5, 3, 6]
post_order = [7, 4, 2, 5, 6, 3, 1]


N = len(in_order)
pos = [0] * (N + 1)
for i in range(N):
    pos[in_order[i]] = i
 
def pre_in_to_post(pre_l, pre_r, in_l, in_r):
    if pre_l > pre_r or in_l > in_r:
        return
    root = pre_order[pre_l]
    mid = pos[root] # in order에서의 root 좌표값
    # mid = in_order.index(root)
    # print(mid)
    left = mid - in_l # 좌측 서브트리 노드 개수
    right = in_r - mid # 우측 서브트리 노드 개수
    pre_in_to_post(pre_l + 1, pre_l + left, in_l, in_l + left - 1)
    pre_in_to_post(pre_r - right + 1, pre_r, in_r - right + 1, in_r)
    print(root, end=" ")
 
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
 
pre_in_to_post(0, N - 1, 0, N - 1)
print()
# in_post_to_pre(0, N - 1, 0, N - 1)
