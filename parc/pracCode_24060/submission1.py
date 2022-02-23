from random import randint
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
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list[0])  
            right_list.pop(0)  
        else:
            merged_list.append(left_list[0])
            left_list.pop(0)

    if len(left_list) > 0:
        merged_list += left_list
    if len(right_list) > 0:
        merged_list += right_list
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
