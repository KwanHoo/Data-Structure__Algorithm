# 없는 숫자 더하기

def solution(numbers):
    answer = -1
    nlist = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        temp = numbers[i]
        if temp in nlist:
            nlist.remove(temp)
    answer = sum(nlist)
    return answer