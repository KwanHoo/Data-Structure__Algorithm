import sys
import math

def merge_sort(mylist):
    if len(mylist) <= 1: 
        return mylist

    half = math.ceil(len(mylist) / 2)
    left_list = merge_sort(mylist[:half])
    right_list = merge_sort(mylist[half:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    merged_list = []
    global temp_list

    i = 0
    j = 0

    L_count = len(left_list)
    R_count = len(right_list)
    while i < L_count and j < R_count:
        if left_list[i] > right_list[j]:
            merged_list.append(right_list[j])
            j += 1
        else:
            merged_list.append(left_list[i])
            i += 1
    if i != L_count:
        for l in range(i, L_count):
            merged_list.append(left_list[l])
    if j != R_count:
        for m in range(j, R_count):
            merged_list.append(right_list[m])

    temp_list += merged_list
    return merged_list


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    temp_list = []
    sorted_data = merge_sort(A)
    if len(temp_list) < K:
        print(-1)
    else:
        print(temp_list[K-1])
