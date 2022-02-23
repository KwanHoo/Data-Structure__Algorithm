from random import randint

def merge_sort (mylist):
    if len(mylist) <= 1: return mylist
    
    half = len(mylist) // 2
    left_list = merge_sort(mylist[:half])  
    right_list = merge_sort(mylist[half:])

    merged_list = []                    

    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list[0])
            right_list.pop(0)
        else:
            merged_list.append(left_list[0])
            left_list.pop(0)

    # * while문은 재귀 호출로 merge_sort()를 실행한 후에 left_list나 right_list에 데이터가 남아 있다면,
    # * 그 데이터는 이미 정렬된 상태로 남아 있기 때문에 최종적으로 정렬된 리스트에 해당하는 merged_list에 추가함
    if len(left_list) > 0 : merged_list += left_list
    if len(right_list) > 0 : merged_list += right_list
    return merged_list

if __name__ == '__main__':
    data = []
    input_n = input("정렬할 데이터의 수 : ")
    data = [ randint(1, 99) for x in range(int(input_n))]
    print("<정렬전>")
    print(data)
    sorted_data = merge_sort(data)
    print("<정렬후>")
    print(sorted_data)