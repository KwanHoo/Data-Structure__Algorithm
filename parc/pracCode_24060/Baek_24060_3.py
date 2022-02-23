import sys
import math

def merge_sort(mylist):
    if len(mylist) <= 1: # 배열크기 1개시 그대로 리턴
        return mylist

    half = math.ceil(len(mylist) / 2)
    print('half :', half)                # 중간값
    left_list = merge_sort(mylist[:half])
    print('left_list', left_list)  # 전반부 , 각 런의 가장 왼쪽 데이터 의미
    right_list = merge_sort(mylist[half:])
    print('right_list', right_list)  # 후반부 , 각 런의 가장 오른쪽 데이터 의미
    
    return merge(left_list, right_list)

def merge(left_list, right_list):
    merged_list = []
    global temp_list   
    # breakValue = True                    
    # for i in range(len(left_list)):
    #     for j in range(len(right_list)):
    #         if i == 0 and j ==0 :
    #             break
    #             breakValue = False
    #         if left_list[j] > right_list[i]:
    #             merged_list.append(right_list[i])
    #             break
    #         else:
    #             merged_list.append(left_list[j])
    #     if breakValue == False:
    #         break
    # [4, 3] ,[5, 2]
    i = 0
    j = 0
    # print('함수안 R',right_list)
    # print('함수안 L',left_list)

    L_count = len(left_list)
    R_count = len(right_list)
    while i < L_count and j < R_count:
        if left_list[i] > right_list[j]:
            merged_list.append(right_list[j])
            j += 1
        else:
            merged_list.append(left_list[i])
            i += 1
    # print('while 뒤 리스트',merged_list)
    if i != L_count:
        for l in range(i,L_count):
            merged_list.append(left_list[l])
    if j != R_count:
        for m in range(j,R_count):
            merged_list.append(right_list[m])
    # print('if뒤 리스트', merged_list)

    temp_list += merged_list
    print('return전 temp', temp_list)
    return merged_list


# ! K 번째 저장되는 숫자 출력
# ! 특수조건 : -1 출력
# * N: 배열 A의 크기 / K: 저장횟수 / A: 배열

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    temp_list = []
    sorted_data = merge_sort(A)
    print('result list',sorted_data)
    if len(temp_list) < K:
        print(-1)
    else:
        print(temp_list[K-1])
